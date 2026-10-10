# KOREAN LONG IMAGE OCR TOOL LITE v0.1.0

Initial public Lite distribution for long screenshot and multi-image OCR/reconstruction workflows.

## Included variants

### GPT Lite

Path: `long-image-ocr-gpt-lite/SKILL.md`

Primary focus:

- bounded batch processing
- numeric progress updates
- incremental checkpointing
- timeout/interruption recovery
- exact resume points
- no false background-processing claims

### Gemini Lite

Path: `long-image-ocr-gemini-lite/SKILL.md`

Primary focus:

- source modality separation
- direct pixel verification before visual claims
- Drive/indexed-text vs original-image distinction
- no synthetic detail from aggregate totals
- preservation of displayed source values
- independent validation and completion gates

## Shared invariants

Both variants enforce these principles:

1. Do not claim visual verification without inspecting source pixels.
2. Do not fabricate detailed rows from account/category totals.
3. Keep displayed source values separate from inferred calculations.
4. Do not use circular validation.
5. Do not report partial verification as complete.

## Status

Release level: **v0.1.0 / initial stable Lite distribution**

The repository contains guidance skills, not a standalone OCR engine. Actual image access, OCR capability, and installation behavior depend on the host environment.
