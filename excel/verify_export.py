"""Read-only, independent XLSX acceptance check using the Python standard library."""
import collections
import json
import sys
from pathlib import Path
import xml.etree.ElementTree as ET
from zipfile import ZipFile

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else ROOT / 'outputs' / '01a081c4-9e73-7812-9912-01732d231aa3'
rows = json.loads((OUT / 'synthetic-orders.json').read_text(encoding='utf-8'))
ids = [str(row[0]).strip().upper() for row in rows]
duplicates = collections.Counter(ids)
totals = collections.Counter()
ready = 0
for order_id, (_, team, units) in zip(ids, rows):
    team = team.strip().title()
    if (order_id and duplicates[order_id] == 1 and team in {'Assembly', 'Dispatch', 'Packing'}
            and type(units) in {int, float} and units > 0 and units % 1 == 0):
        totals[team] += units
        ready += 1
assert (len(rows), ready, dict(totals), sum(totals.values())) == (18, 12, {'Packing': 31, 'Assembly': 32, 'Dispatch': 14}, 77)
ns = {'s': 'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
with ZipFile(OUT / 'order-quality-demo.xlsx') as archive:
    sheets = [ET.fromstring(archive.read(f'xl/worksheets/sheet{i}.xml')) for i in (1, 2)]
    errors = [cell.attrib['r'] for sheet in sheets for cell in sheet.findall('.//s:c', ns) if cell.attrib.get('t') == 'e']
    assert not errors, errors
    formula_count = sum(len(sheet.findall('.//s:f', ns)) for sheet in sheets)
    assert formula_count == 82, formula_count
    cells = {cell.attrib['r']: cell for cell in sheets[0].findall('.//s:c', ns)}
    expected = {'A8': 18, 'B8': 12, 'C8': 6, 'B10': 77, 'C14': 32, 'C15': 14, 'C16': 31}
    for address, value in expected.items():
        actual = float(cells[address].find('s:v', ns).text)
        assert actual == value, (address, actual, value)
    assert not any('vbaProject' in name or name.startswith('xl/externalLinks/') for name in archive.namelist())
result = {'result': 'PASS', 'independent_recomputed_rows': len(rows), 'ready_rows': ready, 'review_rows': len(rows)-ready, 'ready_units': sum(totals.values()), 'cached_result_checks': expected, 'live_formula_count': formula_count, 'error_cells': errors, 'macros': False, 'external_workbook_links': False, 'limitations': 'Reads XLSX XML and cached values. Does not run Microsoft Excel.'}
(OUT / 'excel-export-verification.json').write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
print(json.dumps(result))
