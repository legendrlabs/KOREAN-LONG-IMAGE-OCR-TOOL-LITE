# Golden regression tests

This directory contains a dependency-free benchmark for Gemini Lite OCR/restoration regressions.

## Fixture

`fixtures/financial_screenshot_118x2048_v1.json` is a user-verified answer key derived from a compressed 118×2048 financial screenshot. The original screenshot is intentionally not bundled.

The fixture covers summary fields, seven domestic rows, and the first twenty overseas rows. v0.1.6 adds row-level quantity/P&L data and detailed QQQI/GPIQ/ROCQ fields so patch-only corrections can be detected.

## What the scorer checks

- literal summary values and financial arithmetic;
- row identity and every expected row field;
- accidental cancellation;
- semantic ticker substitution;
- prior-output anchoring during a re-read;
- row atomicity;
- current-pass verification completeness;
- false `COMPLETE_VERIFIED`.

## Run tests

```bash
python -m unittest discover -s tests -p 'test_*.py' -v
```

## Score a candidate extraction

```bash
python tests/evaluate_golden_fixture.py \
  tests/fixtures/financial_screenshot_118x2048_v1.json \
  candidate.json \
  --report report.json
```

Optional audit metadata for correction/re-read evaluations:

```json
{
  "verification_audit": {
    "reread_requested": true,
    "clean_room_reread": true,
    "previous_output_used_as_evidence": false
  }
}
```

Rows that explicitly claim `"verified": true` may provide `current_pass_verified_fields`; if reported expected fields were not all re-observed, the scorer returns `current_pass_verification_incomplete`.
