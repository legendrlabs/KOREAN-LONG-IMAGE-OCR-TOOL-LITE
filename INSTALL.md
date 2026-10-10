# Installation Guide / 설치 가이드

> 이 저장소는 **Agent Skill / skill-only plugin 배포판**입니다. OCR 실행 프로그램이 아니며 `GEMINI_API_KEY`, EasyOCR, Tesseract, npm/pip 또는 별도 OCR 서버가 필요하지 않습니다.

Repository: `https://github.com/legendrlabs/KOREAN-LONG-IMAGE-OCR-TOOL-LITE`

Current repository version: **v0.1.6**

## 1. 설치 대상

| 환경 | 설치 대상 | 권장 방식 |
|---|---|---|
| ChatGPT 웹/앱 | `long-image-ocr-gpt-lite` | 기존 v0.1.1 Plugin/Skill |
| ChatGPT Desktop / Codex | GPT plugin 또는 `long-image-ocr-gpt-lite` | 기존 v0.1.1 marketplace/plugin |
| Gemini 계열 | `long-image-ocr-gemini-lite` | **단일 Markdown 직접 등록 우선** |
| Gemini CLI | `long-image-ocr-gemini-lite` | Markdown/Git/`.skill` 중 지원 경로 |

Canonical skill paths:

```text
skills/long-image-ocr-gpt-lite/SKILL.md
skills/long-image-ocr-gemini-lite/SKILL.md
```

Gemini direct-distribution file: `dist/long-image-ocr-gemini-lite.md`

---

## 2. Gemini — Markdown 직접 등록 우선

```text
dist/long-image-ocr-gemini-lite.md
```

등록 이름:

```text
long-image-ocr-gemini-lite
```

이 파일은 canonical `skills/long-image-ocr-gemini-lite/SKILL.md`와 동일한 내용입니다.

복붙용 요청문:

```text
dist/GEMINI_INSTALL_PROMPT.txt
```

현재 환경에 Agent Skill 생성, `SKILL.md` 업로드, Markdown에서 Skill 생성, 사용자/워크스페이스 Skill 등록 기능이 있으면 이 방식을 우선합니다.

- **영구 Skill registry가 있음** → `long-image-ocr-gemini-lite`로 등록
- **파일 읽기만 가능하고 Skill registry가 없음** → 현재 대화에 지침을 로드한 상태일 뿐 영구 설치가 아님
- **Gemini CLI 사용 가능** → 아래 fallback 사용

저장소를 `npm`/`pip`, `GEMINI_API_KEY`, EasyOCR/Tesseract 서버, MCP/Cloud Run OCR 서비스, 이미지 분할 실행기로 재해석하지 않습니다.

## 3. Gemini CLI fallback

사용자 전체:

```bash
gemini skills install https://github.com/legendrlabs/KOREAN-LONG-IMAGE-OCR-TOOL-LITE.git --path skills/long-image-ocr-gemini-lite --scope user
```

현재 workspace:

```bash
gemini skills install https://github.com/legendrlabs/KOREAN-LONG-IMAGE-OCR-TOOL-LITE.git --path skills/long-image-ocr-gemini-lite --scope workspace
```

Current package:

```text
dist/long-image-ocr-gemini-lite-v0.1.6.skill
```

설치 예:

```bash
gemini skills install ./long-image-ocr-gemini-lite-v0.1.6.skill --scope user
```

설치 후:

```text
/skills reload
/skills list
```

`long-image-ocr-gemini-lite`가 보이는지 확인합니다.

## 4. v0.1.6 동작 확인

테스트 요청:

```text
이 금융 스크린샷을 원본 픽셀 기준으로 복원해줘.
티커/회사명은 보이는 글자 그대로 적고 익숙한 종목으로 자동 교정하지 마.
이전 OCR 답변이 틀렸다면 그 답변을 패치하지 말고 원본 픽셀에서 요청 범위를 clean-room으로 다시 읽어.
한 행에서 하나라도 다시 읽으면 그 행의 종목명/수량/평가액/손익/수익률을 전부 현재 visual pass에서 다시 확인해.
각 행을 먼저 독립 검증한 다음 합계를 확인하고, 합계가 맞더라도 행이 틀리면 검증 성공으로 처리하지 마.
총자산·원금·손익처럼 산술적으로 연결된 값은 실제로 검산해.
```

기대 동작:

- Literal Identity Lock 유지
- `QQQI → QQQ`, `GPIQ → UPRO`, `ROCQ → RDVY` 금지
- row identity/value/association 우선 검증
- matching subtotal은 secondary cross-check일 뿐 row proof가 아님
- accidental cancellation 가능성 고려
- 산술 불일치 시 재판독/불확실성 표시
- unsupported fees/rounding/FX explanation 금지

## 5. Golden regression benchmark

```bash
python -m unittest discover -s tests -p 'test_*.py' -v
```

후보 OCR JSON 채점:

```bash
python tests/evaluate_golden_fixture.py \
  tests/fixtures/financial_screenshot_118x2048_v1.json \
  candidate.json
```

---

## 6. ChatGPT 웹 / 앱

GPT Lite plugin ZIP과 canonical skill은 v0.1.1에서 그대로 유지합니다.

```text
dist/LongImageOCR-GPT-Lite-v0.1.1-plugin.zip
skills/long-image-ocr-gpt-lite/SKILL.md
```

현재 ChatGPT Work 테스트 운용 중인 GPT skill 본문은 v0.1.6에서 수정하지 않았습니다.

---

## 7. ChatGPT Desktop / Codex marketplace

```bash
codex plugin marketplace add legendrlabs/KOREAN-LONG-IMAGE-OCR-TOOL-LITE --ref main
codex plugin marketplace list
```

지원 환경에서 **Legendr Labs OCR Tools** source의 `korean-long-image-ocr-tool-lite`를 설치합니다. GPT OCR 작업에는 `long-image-ocr-gpt-lite`가 선택되어야 합니다.

---

## 8. 이 스킬이 새로 만들어주지 않는 기능

스킬 설치 자체가 Drive 원본 접근 권한, 모델 vision 기능, OCR 엔진, 인터넷/connector 권한, 백그라운드 실행 기능을 새로 만들지는 않습니다. 스킬은 호스트에 이미 존재하는 기능을 어떻게 사용하고 근거·누락·식별자·행 검증·재판독 provenance·산술검산·완료 상태를 어떻게 관리할지 정의합니다.

---

## 9. 업데이트

- Gemini Markdown: `dist/long-image-ocr-gemini-lite.md`로 교체
- Gemini CLI Git install: update/reinstall 후 `/skills reload`
- Gemini `.skill`: `dist/long-image-ocr-gemini-lite-v0.1.6.skill` 사용
- GPT: 기존 v0.1.1 설치 유지


---

## 10. Compatibility

v0.1.x 호환을 위해 legacy 경로와 이전 패키지도 유지합니다.

```text
long-image-ocr-gpt-lite/
long-image-ocr-gemini-lite/
skills/long-image-ocr-gpt-lite/
skills/long-image-ocr-gemini-lite/
dist/LongImageOCR-GPT-Lite-v0.1.1-plugin.zip
dist/long-image-ocr-gemini-lite-v0.1.1.skill
dist/long-image-ocr-gemini-lite-v0.1.3.skill
dist/long-image-ocr-gemini-lite-v0.1.4.skill
dist/long-image-ocr-gemini-lite-v0.1.5.skill
```

Gemini 신규 설치는 `dist/long-image-ocr-gemini-lite.md` 또는 `dist/long-image-ocr-gemini-lite-v0.1.6.skill`을 우선합니다.
