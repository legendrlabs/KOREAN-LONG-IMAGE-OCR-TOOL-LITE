# Golden regression tests

This directory contains a small, dependency-free benchmark for Gemini Lite OCR/restoration regressions.

## Fixture

`fixtures/financial_screenshot_118x2048_v1.json` is a user-verified answer key derived from a compressed 118×2048 financial screenshot. The original screenshot is intentionally not bundled.

The fixture covers six summary fields, seven domestic holding rows, and the first twenty overseas holding rows.

## Why row-first scoring exists

A matching subtotal is not enough. Independent row errors can cancel out and still produce the exact subtotal. The evaluator therefore scores row identity, row value, row exactness, summary arithmetic, and aggregate agreement separately.

## Run tests

```bash
python -m unittest discover -s tests -p 'test_*.py' -v
```

## Score a candidate extraction

Candidate JSON should use the same high-level structure as the fixture.

```bash
python tests/evaluate_golden_fixture.py \
  tests/fixtures/financial_screenshot_118x2048_v1.json \
  candidate.json \
  --report report.json
```

Exit code is `0` only when the candidate passes all enforced checks.

Important failure classes include `accidental_cancellation`, `semantic_identity_mismatch`, `summary_arithmetic_mismatch`, `false_complete_verified`, and row-level domestic/foreign mismatches.
