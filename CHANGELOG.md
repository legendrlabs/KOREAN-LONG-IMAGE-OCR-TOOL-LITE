# Changelog

All notable changes to this project will be documented in this file.

The format is based on Keep a Changelog and this project uses semantic versioning where practical.

## [0.1.3] - 2026-10-11

### Changed

- Gemini Lite is now a self-contained **instruction-only, evidence-only native-vision protocol**.
- Merged the stronger production OCR workflow from the field-tested Gemini draft into the existing source-state/completion-state framework.
- Added a seven-phase workflow: layout reconnaissance, segmented reading, boundary reconciliation, precision pass, low-confidence pass, reconstruction, and audit.
- Added explicit source-coverage requirements so every accessible image/page must be checked before completion is claimed.
- Added structured-output safeguards for CSV quoting, spreadsheet cell boundaries, formula errors, and wrong-row references.
- Added summary/aggregation rules requiring totals to be recomputed from final structured rows with explicit include/exclude decisions.
- Added Auto, Exact transcription, and Structured extraction operating modes.
- Clarified that verification is a gate, not a substitute for the requested deliverable.

### Fixed

- Explicitly blocks Gemini from reinterpreting this skill as a `GEMINI_API_KEY`, Python, MCP, Cloud Run, EasyOCR/Tesseract, local executable, or image-slicing application unless the user explicitly supplied and requested such tooling.
- Preserves `DIRECT_PIXEL_VERIFIED / TEXT_INDEX_ONLY / METADATA_ONLY / UNAVAILABLE` source states, anti-fabrication rules, screen-value preservation, independent validation, and completion gating.

### Distribution

- Updated canonical Gemini skill: `skills/long-image-ocr-gemini-lite/SKILL.md`.
- Updated direct Markdown artifact: `dist/long-image-ocr-gemini-lite.md`.
- Added current Gemini CLI package: `dist/long-image-ocr-gemini-lite-v0.1.3.skill`.
- Kept GPT/ChatGPT Work skill and v0.1.1 GPT plugin ZIP unchanged while GPT testing is in progress.

## [0.1.2] - 2026-10-11

### Added

- Direct Gemini Markdown distribution: `dist/long-image-ocr-gemini-lite.md`.
- Copy-paste installer prompt: `dist/GEMINI_INSTALL_PROMPT.txt`.

### Changed

- Gemini installation guidance now prioritizes direct Markdown / `SKILL.md` registration when the current host exposes a skill-registration flow.
- Gemini CLI Git/`.skill` installation remains as a fallback and compatibility path.
- GPT installation artifacts and guidance are intentionally unchanged because the GPT/ChatGPT Work path is already working in testing.

### Fixed

- Reduced host confusion where the Gemini skill repository was misread as an executable OCR application requiring `npm`, `pip`, `GEMINI_API_KEY`, custom servers, or local OCR scripts.
- Clarified the difference between persistent skill installation and temporarily loading the Markdown instructions into the current conversation.

## [0.1.1] - 2026-10-11

### Added

- Portable OpenAI plugin manifest at `plugin.json` using the Agent Plugins schema.
- Canonical portable skill layout under `skills/`:
  - `skills/long-image-ocr-gpt-lite/SKILL.md`
  - `skills/long-image-ocr-gemini-lite/SKILL.md`
- Repo marketplace at `.agents/plugins/marketplace.json` for supported ChatGPT Desktop/Codex marketplace flows.
- Prebuilt ChatGPT/Codex skill-only plugin archive: `dist/LongImageOCR-GPT-Lite-v0.1.1-plugin.zip`.
- Prebuilt Gemini CLI skill package: `dist/long-image-ocr-gemini-lite-v0.1.1.skill`.
- Installation guidance that clearly separates ChatGPT plugin upload, ChatGPT Skills upload, GitHub marketplace, Codex skill-only, and Gemini CLI flows.

### Changed

- Repository is now packaged as an installable Agent Skill/plugin distribution rather than only a source repository containing standalone `SKILL.md` files.
- Canonical install paths moved to `skills/<skill-name>/SKILL.md`; the original top-level skill folders are retained for v0.1.x compatibility.
- README now states prominently that this project is an Agent Skill/plugin package, not an OCR executable, API wrapper, slicing script, or server application.

### Fixed

- Reduced the chance that hosts misinterpret the repository as a local OCR application requiring `GEMINI_API_KEY`, EasyOCR, custom servers, or separate OCR scripts.
- Added direct package artifacts so eligible ChatGPT/plugin and Gemini CLI environments do not need to manually reconstruct package structure before installation.

## [0.1.0] - 2026-10-11

### Added

- Initial dual-distribution Lite release.
- `long-image-ocr-gpt-lite` skill for bounded batch processing, numeric progress reporting, checkpointing, timeout recovery, and resumable OCR workflows.
- `long-image-ocr-gemini-lite` skill for source-modality enforcement, direct-pixel verification, Drive/indexed-text separation, independent validation, and anti-fabrication safeguards.
- `INSTALL.md` with ChatGPT, Codex, and Gemini installation guidance.
- MIT license.
- Explicit completion states including `COMPLETE_VERIFIED`, `PARTIAL_VERIFIED`, `INTERRUPTED_RESUMABLE`, and `DATA_HOLD`.
- Regression-oriented safeguards against synthetic aggregate rows such as `PORTFOLIO`, circular validation, and completion overstatement.

### Notes

This project provides model-execution guidance rather than an OCR engine. It is intended to improve source fidelity, progress visibility, and interruption resilience in image-based extraction and reconstruction tasks.
