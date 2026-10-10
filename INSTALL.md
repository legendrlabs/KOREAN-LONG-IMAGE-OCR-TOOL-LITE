# Installation Guide / 설치 가이드

> 이 저장소는 **Agent Skill / skill-only plugin 배포판**입니다. OCR 실행 프로그램이 아니며 `GEMINI_API_KEY`, EasyOCR, Tesseract, 별도 서버 또는 이미지 분할 스크립트를 설치할 필요가 없습니다.

Repository:

`https://github.com/legendrlabs/KOREAN-LONG-IMAGE-OCR-TOOL-LITE`

Current repository version: **v0.1.3**

---

# 1. 설치 대상

| 환경 | 설치 대상 | 권장 방식 |
|---|---|---|
| ChatGPT 웹/앱 | `long-image-ocr-gpt-lite` | 기존 v0.1.1 Plugin/Skill 설치 |
| ChatGPT Desktop / Codex | GPT plugin 또는 `long-image-ocr-gpt-lite` | 기존 v0.1.1 marketplace/plugin |
| Gemini 계열 | `long-image-ocr-gemini-lite` | **단일 Markdown 직접 등록 우선** |
| Gemini CLI | `long-image-ocr-gemini-lite` | Markdown/Git/`.skill` 중 지원 경로 |

Canonical skill paths:

```text
skills/long-image-ocr-gpt-lite/SKILL.md
skills/long-image-ocr-gemini-lite/SKILL.md
```

Gemini direct-distribution file:

```text
dist/long-image-ocr-gemini-lite.md
```

---

# 2. Gemini — Markdown 직접 등록 우선

Gemini 신규 설치에서는 가능한 경우 아래 단일 Markdown을 Agent Skill로 등록합니다.

```text
dist/long-image-ocr-gemini-lite.md
```

등록 이름:

```text
long-image-ocr-gemini-lite
```

이 파일은 canonical Gemini `SKILL.md`와 동일한 내용입니다.

현재 환경에 다음 기능이 있으면 이 방식을 먼저 사용합니다.

- Agent Skill 생성
- `SKILL.md` 업로드
- Markdown에서 Skill 생성
- 사용자/워크스페이스 Skill 등록
- 로컬 Skill directory에 Markdown 저장

복붙용 요청문:

```text
dist/GEMINI_INSTALL_PROMPT.txt
```

## 영구 설치와 현재 대화 로드는 다름

- **영구 Skill registry가 있음** → `long-image-ocr-gemini-lite`로 등록
- **파일 읽기만 가능하고 Skill registry가 없음** → 현재 대화에 지침을 로드해 사용 가능하지만 영구 설치라고 표현하지 않음
- **Gemini CLI 사용 가능** → 아래 CLI fallback 사용

어떤 경우에도 저장소를 다음처럼 재해석하면 안 됩니다.

- `npm install` 앱
- `pip install -r requirements.txt` Python 프로젝트
- `GEMINI_API_KEY` API 프로그램
- EasyOCR/Tesseract 서버
- MCP/Cloud Run OCR 서비스
- 이미지 분할 실행기

Gemini Lite v0.1.3 자체도 **instruction-only, evidence-only native-vision protocol**임을 명시합니다.

---

# 3. Gemini CLI fallback

## GitHub skill directory 설치

사용자 전체:

```bash
gemini skills install https://github.com/legendrlabs/KOREAN-LONG-IMAGE-OCR-TOOL-LITE.git --path skills/long-image-ocr-gemini-lite --scope user
```

현재 workspace:

```bash
gemini skills install https://github.com/legendrlabs/KOREAN-LONG-IMAGE-OCR-TOOL-LITE.git --path skills/long-image-ocr-gemini-lite --scope workspace
```

## `.skill` package

현재 Gemini package:

```text
dist/long-image-ocr-gemini-lite-v0.1.3.skill
```

이전 v0.1.1 package는 호환/기록용으로 남아 있으므로 신규 설치에는 **v0.1.3**을 사용합니다.

설치 예:

```bash
gemini skills install ./long-image-ocr-gemini-lite-v0.1.3.skill --scope user
```

설치 확인:

```bash
gemini skills list
```

이미 Gemini CLI 세션을 열어둔 상태라면:

```text
/skills reload
```

그 후 `/skills list`에서 `long-image-ocr-gemini-lite`가 보이는지 확인합니다.

---

# 4. Gemini v0.1.3 동작 확인

테스트 요청:

```text
이 Drive 폴더의 이미지들을 원본 기준으로 읽어서 상세 데이터를 복원해줘.
색인 텍스트와 실제 이미지 픽셀 확인 여부를 구분하고,
모든 접근 가능한 이미지를 확인한 뒤 요청한 표까지 완성해줘.
원본에서 보이지 않는 상세값은 추정하지 마.
```

기대 동작:

- 외부 OCR/API/runtime를 있다고 꾸며내지 않음
- image pixels와 indexed text를 구분
- `DIRECT_PIXEL_VERIFIED / TEXT_INDEX_ONLY / METADATA_ONLY / UNAVAILABLE` 상태 유지
- 모든 접근 가능한 source를 확인하기 전 완료 선언 금지
- 긴/조밀한 소스에서 7-phase workflow 적용
- 계좌 총액/반복 패턴으로 누락 상세행 생성 금지
- 화면 표시값을 계산값으로 덮어쓰지 않음
- 검증 보고서에서 멈추지 않고 사용자가 요청한 실제 산출물까지 생성
- CSV에서 comma/quote/newline escape, spreadsheet에서 셀/행/수식 참조 검증
- summary는 final structured rows에서 재계산
- 부분 검증이면 `PARTIAL_VERIFIED`, 사용 불가 수준이면 `DATA_HOLD`

---

# 5. ChatGPT 웹 / 앱

GPT 쪽 설치물은 v0.1.3에서 변경하지 않습니다.

GPT Lite plugin ZIP:

```text
dist/LongImageOCR-GPT-Lite-v0.1.1-plugin.zip
```

Canonical skill:

```text
skills/long-image-ocr-gpt-lite/SKILL.md
```

현재 ChatGPT Work 테스트 운용 중인 GPT skill 본문은 v0.1.3에서 수정하지 않았습니다.

---

# 6. ChatGPT Desktop / Codex marketplace

```bash
codex plugin marketplace add legendrlabs/KOREAN-LONG-IMAGE-OCR-TOOL-LITE --ref main
codex plugin marketplace list
```

지원 환경에서 **Legendr Labs OCR Tools** source의 `korean-long-image-ocr-tool-lite`를 설치합니다.

GPT OCR 작업에는 `long-image-ocr-gpt-lite`가 선택되어야 합니다.

---

# 7. 이 스킬이 새로 만들어주지 않는 기능

스킬 설치 자체가 다음 기능을 새로 추가하지는 않습니다.

- Drive 원본 파일 접근 권한
- 모델 vision 기능
- OCR 엔진
- 인터넷/connector 접근 권한
- 백그라운드 실행 기능

스킬은 **호스트에 이미 존재하는 기능을 어떻게 사용하고, 근거·누락·검산·완료 상태를 어떻게 관리할지 정의**합니다.

---

# 8. 업데이트

- **Gemini Markdown direct install**: 새 `dist/long-image-ocr-gemini-lite.md`로 기존 Skill 내용을 교체
- **Gemini CLI Git install**: skill을 업데이트/재설치 후 `/skills reload`
- **Gemini `.skill`**: v0.1.3 package로 교체
- **GPT Plugin/Skill**: 현재 v0.1.1 설치 흐름 유지
- **Codex marketplace**: 기존 marketplace 갱신 절차 사용

---

# 9. Compatibility

v0.1.x 호환을 위해 legacy 경로/이전 패키지도 유지합니다.

```text
long-image-ocr-gpt-lite/
long-image-ocr-gemini-lite/
skills/long-image-ocr-gpt-lite/
skills/long-image-ocr-gemini-lite/
dist/LongImageOCR-GPT-Lite-v0.1.1-plugin.zip
dist/long-image-ocr-gemini-lite-v0.1.1.skill
```

Gemini 신규 설치는 다음 두 항목을 우선합니다.

```text
dist/long-image-ocr-gemini-lite.md
dist/long-image-ocr-gemini-lite-v0.1.3.skill
```
