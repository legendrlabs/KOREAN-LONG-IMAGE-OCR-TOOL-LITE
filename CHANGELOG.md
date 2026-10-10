# Changelog

All notable changes to this project will be documented in this file.

## [0.1.5] - 2026-10-11

### Added
- **Row-First Validation**: detailed rows must be verified before aggregate/subtotal reconciliation.
- **Accidental Cancellation Guard**: a matching subtotal no longer upgrades incorrect or uncertain rows when row errors cancel numerically.
- Golden regression fixture `tests/fixtures/financial_screenshot_118x2048_v1.json` based on a user-verified 118×2048 financial screenshot answer key.
- Dependency-free evaluator `tests/evaluate_golden_fixture.py` and four regression tests.

### Changed
- Aggregate agreement is explicitly secondary evidence; validation order is row identity/value/association → row confidence → aggregate calculation → displayed subtotal cross-check.
- Completion status accounts for unresolved row-level mismatches and possible accidental cancellation.

### Fixed
- Prevented a correct subtotal from being treated as proof that every underlying OCR row is correct.
- Prevented low-confidence rows from being upgraded merely because their numeric errors cancel at the aggregate level.

### Distribution
- Updated all Gemini Markdown skill paths.
- Added `dist/long-image-ocr-gemini-lite-v0.1.5.skill`.
- Kept GPT/ChatGPT Work skill and the v0.1.1 GPT plugin ZIP unchanged.

## [0.1.4] - 2026-10-11

- Added Literal Identity Lock, confidence discipline, Arithmetic Consistency Gate, identity regression cases, and unsupported-reconciliation-story blocking.
- Added `dist/long-image-ocr-gemini-lite-v0.1.4.skill`.

## [0.1.3] - 2026-10-11

- Gemini Lite became a self-contained instruction-only, evidence-only native-vision protocol with source coverage, seven-phase workflow, structured-output safeguards, and completion gating.

## [0.1.2] - 2026-10-11

- Added direct Gemini Markdown distribution and Markdown-first installation guidance.

## [0.1.1] - 2026-10-11

- Added portable plugin metadata, canonical `skills/` layout, marketplace metadata, GPT plugin ZIP, Gemini `.skill`, and install documentation.

## [0.1.0] - 2026-10-11

- Initial dual-distribution Lite release.
