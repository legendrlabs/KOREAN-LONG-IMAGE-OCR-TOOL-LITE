# Release Notes — v0.1.6

Gemini Lite v0.1.6 hardens re-read and correction workflows against **Prior Output Anchoring / Patch-Only Correction**.

## New hard gates

### Clean-room Re-read
When a prior OCR answer is disputed or corrected, the previous extraction is not source evidence. The requested scope must be read again from the source pixels before comparison with earlier output.

### Row Atomicity Lock
A structured row is an atomic evidence unit. If one field is corrected or re-read, every field reported for that row must be re-observed in the current visual pass.

Forbidden example:

```text
previous: QQQ / 19 shares / $9,738.01 / +$1,165.25 / +13.6%
patch:    QQQI / 19 shares / $9,738.01 / +$1,165.25 / +13.6%
```

The golden answer for that row is `QQQI / 180 shares / $9,738.00 / +$149.56 / +1.5%`; changing only the ticker is not verification.

### Current-pass Verification
`VERIFIED` means every reported field was independently observed in the current visual pass. Verification and confidence cannot be inherited from a previous answer.

## Regression benchmark expansion

The existing 118×2048 financial fixture now also covers:

- valuation date `9월 17일`;
- domestic quantities and P&L for all seven rows;
- QQQI/GPIQ/ROCQ quantity, valuation, P&L, and return percentage;
- clean-room audit metadata;
- row atomicity and current-pass provenance failures.

Run:

```bash
python -m unittest discover -s tests -p 'test_*.py' -v
```

## Distribution

- `skills/long-image-ocr-gemini-lite/SKILL.md`
- `dist/long-image-ocr-gemini-lite.md`
- `dist/long-image-ocr-gemini-lite-v0.1.6.skill`

GPT/ChatGPT Work artifacts remain unchanged from v0.1.1.
