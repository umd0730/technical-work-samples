# Work samples — umd0730

Three focused examples for Python, Excel and responsive-web work. AI-assisted using Codex; claims below refer to executed checks, not client endorsements or paid engagements.

## 1. Order quality workbook — self-initiated

**Problem:** inconsistent IDs, duplicate rows and missing quantities can distort a routine operations summary.

**Delivery:** an editable two-sheet Excel workbook with 18 synthetic input rows, preserved originals, normalized IDs/teams, explicit review reasons and live summary formulas. Every occurrence of a duplicate ID is excluded until resolved. Missing quantities remain blank in the source.

**Result:** 12 ready rows, six review rows, 77 ready units. Twelve calculation/edge checks passed. An independent standard-library Python check recomputed the answer and inspected the exported XLSX: 82 live formulas, matching cached totals, no formula error cells, no macros or external workbook links. Both sheets were visually inspected.

**Limits:** this is a fixed 18-row demonstration; extending it requires extending the source/formula/summary ranges. Checked using artifact-tool and XLSX XML, not a native Microsoft Excel session. All data is fictional; no customer spreadsheet was processed.

Open `excel/order-quality-demo.xlsx`. To independently check the delivered file from this kit's root: `python excel/verify_export.py excel` (Python 3, no third-party packages).

## 2. Fieldnotes responsive repair — self-initiated

**Problem:** a deliberately introduced 1080px fixed-width layout causes horizontal overflow on small viewports.

**Delivery:** original HTML/CSS/JavaScript workshop concept, repaired responsive layout, mobile menu with expanded state and Escape focus restoration, native FAQ controls, and local form validation. The comparison page switches between before/after at four widths. CSS illustration is original and needs no downloaded assets.

**Result:** 17 browser checks passed in Edge Chromium 152.0.4191.66, including widths 320, 390, 768 and 1280px. The broken fixture overflows at the three smaller widths; the repaired page does not. Keyboard menu/FAQ, invalid fields, local preview and no unintended submission request were checked. Desktop and mobile screenshots were visually inspected. The internal Codex browser also reproduced the before overflow and repaired layout.

**Limits:** the workshop is fictional, the baseline bug was intentionally constructed, and this is not a previous customer's site. No physical iOS/Safari test. The form has no backend, booking or payment. It does not transmit or save its inputs.

Open `web/index.html` directly for the repaired page. For the before/after comparison, serve the kit locally with `python -m http.server 8769 --bind 127.0.0.1`, then open `http://127.0.0.1:8769/web/compare.html`. Stop the server with Ctrl+C.

## 3. Omi Python CLI timeout — unaccepted contribution candidate

**Problem:** Developer API operations need a configurable timeout while keeping documented defaults and existing retry behavior.

**Delivery prepared:** a finite positive global `--timeout` option, propagation through the CLI/API client and post-login API verification, documentation and eight new test cases. Based on upstream commit `5d29ea0c35d0f03fbfb02990495921d1cc5245df`.

**Recorded checks (2026-09-09):** eight added tests passed. A real CLI subprocess against a synthetic loopback HTTP server failed with a short timeout and succeeded with a longer one. Full CLI suite: 284 passed, one failure independently reproduced on unchanged upstream and tracked in issue #13191. Formatting, targeted typing and patch application checks passed.

**Status:** proposal [BasedHardware/omi#13218](https://github.com/BasedHardware/omi/issues/13218). No acceptance, award, merge, payment or endorsement. Repository-wide setup/preflight remains incomplete. These results come from the existing local run record; the unchanged suite was not rerun while assembling this portfolio.

## How a small engagement would work

Agree on one reproducible problem, sanitized inputs, acceptance criteria and delivery scope before work starts. Receive the focused deliverable, relevant checks and a short handoff. Fixed-price service drafts are separate from these samples; no order is represented here.

GitHub identity for this portfolio: [umd0730](https://github.com/umd0730). No personal contact, payout or authentication information is included.
