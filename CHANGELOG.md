# Changelog

All notable changes to this project will be documented in this file.

The format is based on Keep a Changelog and this project uses semantic versioning where practical.

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
