# v0.1.5 — Row-first validation and golden regression benchmark

v0.1.5 hardens Gemini Lite against a failure mode discovered in a verified 118×2048 financial screenshot test: multiple OCR row errors can cancel numerically and still reproduce the correct displayed subtotal.

## New hard gate: Row-First Validation

Detailed rows must be validated before aggregate reconciliation. A matching subtotal is only secondary evidence and cannot upgrade incorrect or uncertain rows to verified.

Validation order is explicit:

```text
row identity/value/association
→ row confidence
→ aggregate calculation
→ displayed subtotal cross-check
```

## Accidental Cancellation Guard

The release includes a concrete regression case where several wrong domestic values still sum to the correct `7,582,477` subtotal. This must fail row-level validation even though the aggregate matches exactly.

## Golden benchmark

Added:

- `tests/fixtures/financial_screenshot_118x2048_v1.json`
- `tests/evaluate_golden_fixture.py`
- `tests/test_evaluate_golden_fixture.py`
- `tests/README.md`

The fixture stores a verified answer key only; the original screenshot is not bundled.

The evaluator independently scores summary fields, summary arithmetic consistency, domestic row identity/value/exactness, overseas top-20 row identity/value/exactness, accidental cancellation, semantic ticker/name substitution, and false `COMPLETE_VERIFIED` status.

## Preserved v0.1.4 safeguards

- Literal Identity Lock
- `QQQI / GPIQ / ROCQ` semantic-substitution regression checks
- Arithmetic Consistency Gate
- no unsupported fees/rounding/FX reconciliation stories
- source modality and source coverage gates
- seven-phase OCR workflow
- structured-output safety

## Distribution

```text
skills/long-image-ocr-gemini-lite/SKILL.md
dist/long-image-ocr-gemini-lite.md
dist/long-image-ocr-gemini-lite-v0.1.5.skill
```

GPT/ChatGPT Work skill and the v0.1.1 GPT plugin package are intentionally unchanged.
