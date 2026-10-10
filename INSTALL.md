# Installation Guide / 설치 가이드

> 이 저장소는 **Agent Skill / skill-only plugin 배포판**입니다. OCR 실행 프로그램이 아니며 `GEMINI_API_KEY`, EasyOCR, Tesseract, npm/pip 또는 별도 OCR 서버가 필요하지 않습니다.

Repository: `https://github.com/legendrlabs/KOREAN-LONG-IMAGE-OCR-TOOL-LITE`

Current repository version: **v0.1.5**

## 1. 설치 대상

| 환경 | 설치 대상 | 권장 방식 |
|---|---|---|
| ChatGPT 웹/앱 | `long-image-ocr-gpt-lite` | 기존 v0.1.1 Plugin/Skill |
| ChatGPT Desktop / Codex | GPT plugin 또는 `long-image-ocr-gpt-lite` | 기존 v0.1.1 marketplace/plugin |
| Gemini 계열 | `long-image-ocr-gemini-lite` | **단일 Markdown 직접 등록 우선** |
| Gemini CLI | `long-image-ocr-gemini-lite` | Markdown/Git/`.skill` 중 지원 경로 |

## 2. Gemini — Markdown 직접 등록 우선

```text
dist/long-image-ocr-gemini-lite.md
```

등록 이름: `long-image-ocr-gemini-lite`

이 파일은 canonical `skills/long-image-ocr-gemini-lite/SKILL.md`와 동일한 내용입니다.

복붙용 요청문: `dist/GEMINI_INSTALL_PROMPT.txt`

영구 Skill registry가 없고 파일 읽기만 가능한 환경은 현재 대화에 지침을 로드한 상태이지 영구 설치 상태가 아닙니다.

## 3. Gemini CLI fallback

```bash
gemini skills install https://github.com/legendrlabs/KOREAN-LONG-IMAGE-OCR-TOOL-LITE.git --path skills/long-image-ocr-gemini-lite --scope user
```

Current package:

```text
dist/long-image-ocr-gemini-lite-v0.1.5.skill
```

설치 후 `/skills reload` 및 `/skills list`로 확인합니다.

## 4. v0.1.5 동작 확인

```text
이 금융 스크린샷을 원본 픽셀 기준으로 복원해줘.
티커/회사명은 보이는 글자 그대로 적고 익숙한 종목으로 자동 교정하지 마.
각 행의 이름과 금액을 먼저 독립 검증한 다음 합계를 확인해.
합계가 맞더라도 행이 틀리면 검증 성공으로 처리하지 마.
총자산·원금·손익처럼 산술적으로 연결된 값은 실제로 검산해.
```

기대 동작: Literal Identity Lock, row-first validation, accidental-cancellation guard, arithmetic consistency, unsupported reconciliation-story 금지.

## 5. Golden regression benchmark

```bash
python -m unittest discover -s tests -p 'test_*.py' -v
```

```bash
python tests/evaluate_golden_fixture.py \
  tests/fixtures/financial_screenshot_118x2048_v1.json \
  candidate.json
```

## 6. ChatGPT / Codex

GPT 쪽은 v0.1.5에서도 변경하지 않습니다.

```text
dist/LongImageOCR-GPT-Lite-v0.1.1-plugin.zip
skills/long-image-ocr-gpt-lite/SKILL.md
```

## 7. 업데이트

- Gemini Markdown: `dist/long-image-ocr-gemini-lite.md`로 교체
- Gemini CLI Git install: update/reinstall 후 `/skills reload`
- Gemini `.skill`: `dist/long-image-ocr-gemini-lite-v0.1.5.skill` 사용
- GPT: 기존 v0.1.1 설치 유지
