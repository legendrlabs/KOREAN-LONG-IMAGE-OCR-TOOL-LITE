# v0.1.3 — Gemini native-vision workflow merge

This release updates **Gemini Lite only**. GPT/ChatGPT Work skill content and the v0.1.1 GPT plugin package remain unchanged while GPT testing continues.

## Why this release

A field-tested Gemini workflow exposed two practical failure classes:

1. Gemini could misread the repository as an executable OCR/API application and invent `GEMINI_API_KEY`, Python, MCP, Cloud Run, EasyOCR/Tesseract, or local-server setup steps that do not exist.
2. Even when source-modality checks were correct, long-image restoration needed a stronger end-to-end reading workflow so verification did not replace the user's requested deliverable.

v0.1.3 merges the strongest parts of that field-tested workflow into the existing Gemini source-state and completion-state model.

## Gemini changes

### Instruction-only native vision

Gemini Lite now explicitly states that it is an **instruction-only, evidence-only native-vision protocol**. It must use only vision/file/connector/rendering capabilities the current host actually exposes.

It must not claim to invoke external OCR engines, Python/MCP processes, APIs, Cloud Run, local executables, image slicers, EasyOCR/Tesseract, or a `GEMINI_API_KEY` application unless the user explicitly supplied and requested those tools.

### Stronger evidence and coverage gates

Preserved and strengthened:

- `DIRECT_PIXEL_VERIFIED`
- `TEXT_INDEX_ONLY`
- `METADATA_ONLY`
- `UNAVAILABLE`
- no visual-verification claim without inspected pixels
- no fake detail from totals or recurring patterns
- displayed screen values outrank inferred values for restoration
- per-source coverage before completion claims
- environment/tool limitations must not be generalized into universal Drive limitations

### Seven-phase workflow

1. Layout reconnaissance
2. Segmented reading
3. Boundary reconciliation
4. Precision pass
5. Low-confidence pass
6. Reconstruction
7. Audit

This prevents the model from stopping after a readable subset, skipping screenshot boundaries, silently resolving ambiguous digits, or treating a verification report as the final deliverable.

### Structured-output safety

Added explicit rules for:

- CSV quoting/escaping for commas, quotes, and newlines
- native spreadsheet cell boundaries
- wrong-row/cross-row formula checks
- spreadsheet error scans (`#REF!`, `#DIV/0!`, `#VALUE!`, `#NAME?`, `#N/A`)
- summary/rollup recomputation from final structured rows
- explicit include/exclude decisions for duplicates, reversals, funding/top-ups, and free/zero-value rows

### Operating modes

- Auto
- Exact transcription
- Structured extraction

## Distribution

Updated Gemini artifacts:

```text
skills/long-image-ocr-gemini-lite/SKILL.md
dist/long-image-ocr-gemini-lite.md
dist/long-image-ocr-gemini-lite-v0.1.3.skill
long-image-ocr-gemini-lite/SKILL.md
```

The canonical skill, direct Markdown artifact, and legacy Gemini skill path use the same skill content.

## GPT status

Unchanged in v0.1.3:

```text
skills/long-image-ocr-gpt-lite/SKILL.md
dist/LongImageOCR-GPT-Lite-v0.1.1-plugin.zip
plugin.json
```

This avoids disturbing the ChatGPT Work test installation while Gemini-specific behavior is refined.
