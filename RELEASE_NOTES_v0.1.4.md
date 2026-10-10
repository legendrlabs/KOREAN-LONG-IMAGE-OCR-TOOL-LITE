# v0.1.4 — Gemini regression hardening

This release hardens Gemini Lite against two failure modes found in real financial-screenshot testing: semantic identity substitution and unsupported arithmetic reconciliation.

## Literal Identity Lock

For tickers, company/fund/product/account names, identifiers, and other proper nouns, transcribe visible glyphs literally.

Forbidden semantic substitutions include:

```text
QQQI -> QQQ
GPIQ -> UPRO
ROCQ -> RDVY
```

Domain knowledge may trigger reinspection but may not replace the visible source. If the identity remains unclear, return `AMBIGUOUS` or `UNREADABLE`.

Confidence labels must follow visual evidence. A blurry identity cannot be marked high-confidence merely because a chosen interpretation is familiar or plausible.

## Arithmetic Consistency Gate

When the source shows values with an explicit arithmetic relationship, the relationship must be checked before verification is claimed.

Regression example:

```text
assets    = 62,966,337
principal = 65,578,190
P&L       = -2,611,853

62,966,337 - 65,578,190 = -2,611,853
```

A contradictory OCR reading must trigger reinspection or explicit uncertainty.

## No reconciliation storytelling

Do not explain a mismatch as fees, expenses, taxes, rounding, FX effects, settlement timing, `제비용`, or another plausible reconciliation story unless the source explicitly supports that explanation.

A plausible story is not validation.

## Existing safeguards preserved

v0.1.4 retains:

- native-vision / evidence-only operation
- source modality and per-source state
- source coverage gate
- seven-phase long-image workflow
- no fabricated detail from totals
- displayed source values kept separate from calculations
- independent validation
- CSV/spreadsheet safety
- completion states `COMPLETE_VERIFIED / PARTIAL_VERIFIED / DATA_HOLD`

## Distribution

Current Gemini artifacts:

```text
skills/long-image-ocr-gemini-lite/SKILL.md
dist/long-image-ocr-gemini-lite.md
dist/long-image-ocr-gemini-lite-v0.1.4.skill
```

GPT/ChatGPT Work skill and `dist/LongImageOCR-GPT-Lite-v0.1.1-plugin.zip` are intentionally unchanged.
