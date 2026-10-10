# KOREAN LONG IMAGE OCR TOOL LITE

> **AGENT SKILL / SKILL-ONLY PLUGIN PACKAGE — NOT AN OCR APPLICATION**
>
> This repository is an instruction-only workflow package. It does not require `GEMINI_API_KEY`, EasyOCR, Tesseract, npm/pip, a local OCR server, or an external OCR runtime.

한국어 장문 스크린샷·다중 이미지 OCR/복원 작업을 위한 경량 Agent Skill 배포판입니다.

**Current repository version: v0.1.5**

- [설치 가이드](./INSTALL.md)
- [v0.1.5 릴리스 노트](./RELEASE_NOTES_v0.1.5.md)
- [변경 이력](./CHANGELOG.md)
- [Golden regression tests](./tests/README.md)
- [MIT License](./LICENSE)

## Quick install

### Gemini — Markdown direct install first

```text
dist/long-image-ocr-gemini-lite.md
```

이 파일은 canonical `skills/long-image-ocr-gemini-lite/SKILL.md`와 동일한 내용입니다. Agent Skill / `SKILL.md` / Markdown 등록 기능이 있으면 `long-image-ocr-gemini-lite`로 직접 등록합니다.

Gemini CLI fallback:

```bash
gemini skills install https://github.com/legendrlabs/KOREAN-LONG-IMAGE-OCR-TOOL-LITE.git --path skills/long-image-ocr-gemini-lite --scope user
```

Current `.skill` package:

```text
dist/long-image-ocr-gemini-lite-v0.1.5.skill
```

### ChatGPT / Codex — GPT Lite

GPT 경로는 **v0.1.1과 동일하게 유지**합니다.

```text
dist/LongImageOCR-GPT-Lite-v0.1.1-plugin.zip
skills/long-image-ocr-gpt-lite/SKILL.md
```

## Gemini Lite v0.1.5 highlights

### 1. Literal Identity Lock

고유명사·티커를 익숙한 다른 종목으로 의미 보정하지 않습니다.

```text
QQQI → QQQ   # forbidden
GPIQ → UPRO  # forbidden
ROCQ → RDVY  # forbidden
```

### 2. Arithmetic Consistency Gate

```text
62,966,337 - 65,578,190 = -2,611,853
```

불일치를 근거 없이 수수료·제비용·반올림·FX 등으로 합리화하지 않습니다.

### 3. Row-First Validation

**각 행이 맞는지 먼저 검증하고, 합계는 그 다음에 봅니다.**

```text
row identity/value/association
→ row confidence
→ aggregate calculation
→ displayed subtotal cross-check
```

합계가 맞더라도 행이 틀렸다면 검증 실패입니다.

### 4. Accidental Cancellation Guard

독립적인 행 오차가 서로 상쇄되어 정확한 subtotal을 만드는 경우를 명시적으로 잡습니다. `SUM(rows) == subtotal`만으로 행의 confidence를 올릴 수 없습니다.

### 5. Golden regression benchmark

`tests/fixtures/financial_screenshot_118x2048_v1.json`에 검증된 정답지를 저장하고, stdlib-only evaluator로 요약/행/산술/identity를 독립 채점합니다.

```bash
python -m unittest discover -s tests -p 'test_*.py' -v
```

## Core guarantees

1. 픽셀을 직접 확인하지 않았으면 시각 검증했다고 주장하지 않습니다.
2. 합계·반복 패턴으로 누락 상세행을 만들어내지 않습니다.
3. 화면 표시값과 계산값을 분리합니다.
4. 일부만 검증하고 전체 완료라고 말하지 않습니다.
5. 순환 검산을 인정하지 않습니다.
6. 고유명사를 익숙한 티커/회사명으로 자동 교정하지 않습니다.
7. 산술 불일치를 근거 없는 비용/반올림 이야기로 설명하지 않습니다.
8. **행 단위 검증 전에 aggregate match를 정확성 증거로 사용하지 않습니다.**
9. 행 오차가 상쇄되어 subtotal이 맞는 경우도 실패로 취급합니다.

## Status vocabulary

Gemini Lite final state: `COMPLETE_VERIFIED / PARTIAL_VERIFIED / DATA_HOLD`.

GPT Lite additionally uses `IN_PROGRESS / INTERRUPTED_RESUMABLE` for long-running checkpoint workflows.

## What this repository is not

이 저장소는 자체 OCR 엔진, Gemini/OpenAI API 앱, EasyOCR/Tesseract 설치 프로그램, 이미지 자동 분할 실행기, 백그라운드 서버가 아닙니다.

## Version

**v0.1.5 — Gemini row-first validation and golden regression benchmark**

GPT skill/package remains unchanged from v0.1.1 while GPT testing continues.
