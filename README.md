# KOREAN LONG IMAGE OCR TOOL LITE

> **AGENT SKILL / SKILL-ONLY PLUGIN PACKAGE — NOT AN OCR APPLICATION**
>
> 이 저장소는 OCR 실행 프로그램, API 래퍼, 이미지 슬라이서, 로컬 서버가 아닙니다. `GEMINI_API_KEY`, EasyOCR, Tesseract 또는 별도 OCR 스크립트를 요구하지 않습니다. 설치되는 호스트(ChatGPT/Codex/Gemini)가 제공하는 vision·file·connector 기능을 더 안전하고 일관되게 사용하도록 만드는 작업 프로토콜입니다.

한국어 장문 스크린샷·다중 이미지 OCR/복원 작업을 위한 경량 Agent Skill 배포판입니다.

**Current repository version: v0.1.4**

- [설치 가이드](./INSTALL.md)
- [v0.1.4 릴리스 노트](./RELEASE_NOTES_v0.1.4.md)
- [변경 이력](./CHANGELOG.md)
- [MIT License](./LICENSE)

## Quick install

### Gemini — Markdown direct install first

가장 단순한 Gemini 배포 파일:

```text
dist/long-image-ocr-gemini-lite.md
```

이 파일은 canonical `skills/long-image-ocr-gemini-lite/SKILL.md`와 동일한 내용을 담습니다.

현재 환경에 Agent Skill / `SKILL.md` / Markdown 등록 기능이 있으면 다음 이름으로 직접 등록하는 방식을 최우선으로 사용합니다.

```text
long-image-ocr-gemini-lite
```

복붙용 요청문:

```text
dist/GEMINI_INSTALL_PROMPT.txt
```

### Gemini CLI fallback

```bash
gemini skills install https://github.com/legendrlabs/KOREAN-LONG-IMAGE-OCR-TOOL-LITE.git --path skills/long-image-ocr-gemini-lite --scope user
```

또는 current `.skill` package:

```text
dist/long-image-ocr-gemini-lite-v0.1.4.skill
```

설치 후 실행 중인 Gemini CLI 세션에서는 `/skills reload` 후 `/skills list`로 확인합니다.

### ChatGPT / Codex — GPT Lite

GPT 경로는 **v0.1.1과 동일하게 유지**합니다. 현재 ChatGPT Work 테스트 운용 중인 GPT skill 본문과 plugin package는 v0.1.4에서 변경하지 않습니다.

```text
dist/LongImageOCR-GPT-Lite-v0.1.1-plugin.zip
skills/long-image-ocr-gpt-lite/SKILL.md
```

Codex / ChatGPT Desktop marketplace:

```bash
codex plugin marketplace add legendrlabs/KOREAN-LONG-IMAGE-OCR-TOOL-LITE --ref main
codex plugin marketplace list
```

## Included skills

| Variant | Canonical path | Focus |
|---|---|---|
| GPT Lite | `skills/long-image-ocr-gpt-lite/SKILL.md` | 소배치, 숫자 진행률, 체크포인트, 중단 후 재개 |
| Gemini Lite | `skills/long-image-ocr-gemini-lite/SKILL.md` | native vision, source modality/coverage, literal identity lock, arithmetic verification, anti-fabrication |

## Gemini Lite v0.1.4 highlights

v0.1.4는 실제 금융 스크린샷 회귀테스트에서 확인된 두 종류의 오류를 직접 차단합니다.

### 1. Literal Identity Lock

티커·회사명·상품명·계정명·식별자 같은 고유명사는 **보이는 글리프를 그대로 전사**합니다.

금지 예:

```text
QQQI → QQQ
GPIQ → UPRO
ROCQ → RDVY
```

도메인 지식은 재검토 신호로만 사용할 수 있고, 원문을 더 익숙한 이름으로 교체하는 근거가 될 수 없습니다. 흐리면 `AMBIGUOUS` 또는 `UNREADABLE`로 남깁니다.

### 2. Arithmetic Consistency Gate

화면에 산술적으로 연결된 값이 함께 표시되면 실제로 검산합니다.

예:

```text
62,966,337 - 65,578,190 = -2,611,853
```

불일치하면 재판독 또는 불확실성 표시가 필요하며, 근거 없이 `수수료`, `제비용`, `반올림`, `환율`, `결제시차` 등으로 합리화하면 안 됩니다.

### 3. Confidence follows evidence

흐릿한 ticker/name을 문맥상 그럴듯하다는 이유로 `양호`, high-confidence, verified로 표시할 수 없습니다.

## Core guarantees

1. 픽셀을 직접 확인하지 않았으면 시각 검증했다고 주장하지 않습니다.
2. 합계·반복 패턴으로 누락 상세행을 만들어내지 않습니다.
3. 화면 표시값과 계산값을 분리합니다.
4. 일부만 검증하고 전체 완료라고 말하지 않습니다.
5. 순환 검산을 인정하지 않습니다.
6. 고유명사를 익숙한 티커/회사명으로 자동 교정하지 않습니다.
7. 산술 불일치를 근거 없는 비용/반올림 이야기로 설명하지 않습니다.

## Distribution layout

```text
KOREAN-LONG-IMAGE-OCR-TOOL-LITE/
├─ plugin.json                     # GPT portable plugin metadata (v0.1.1)
├─ .agents/plugins/marketplace.json
├─ skills/
│  ├─ long-image-ocr-gpt-lite/
│  │  └─ SKILL.md
│  └─ long-image-ocr-gemini-lite/
│     └─ SKILL.md                  # current Gemini skill
├─ dist/
│  ├─ LongImageOCR-GPT-Lite-v0.1.1-plugin.zip
│  ├─ long-image-ocr-gemini-lite-v0.1.1.skill
│  ├─ long-image-ocr-gemini-lite-v0.1.3.skill
│  ├─ long-image-ocr-gemini-lite-v0.1.4.skill
│  ├─ long-image-ocr-gemini-lite.md
│  └─ GEMINI_INSTALL_PROMPT.txt
├─ README.md
├─ INSTALL.md
├─ CHANGELOG.md
├─ LICENSE
├─ VERSION
├─ RELEASE_NOTES_v0.1.0.md
├─ RELEASE_NOTES_v0.1.1.md
├─ RELEASE_NOTES_v0.1.2.md
├─ RELEASE_NOTES_v0.1.3.md
└─ RELEASE_NOTES_v0.1.4.md
```

Legacy top-level skill folders remain for v0.1.x compatibility and are kept in sync with the canonical Gemini skill.

## Status vocabulary

- `IN_PROGRESS`
- `COMPLETE_VERIFIED`
- `PARTIAL_VERIFIED`
- `INTERRUPTED_RESUMABLE`
- `DATA_HOLD`

Gemini Lite uses `COMPLETE_VERIFIED / PARTIAL_VERIFIED / DATA_HOLD` for final task state. GPT Lite additionally uses `IN_PROGRESS / INTERRUPTED_RESUMABLE` for long-running checkpoint workflows.

## What this repository is not

이 저장소는 자체 OCR 엔진, Gemini/OpenAI API 앱, EasyOCR/Tesseract 설치 프로그램, 이미지 자동 분할 실행기, 백그라운드 서버를 제공하지 않습니다.

실제 이미지 접근, OCR/vision 성능, Drive 원본 접근 가능 여부는 설치되는 호스트와 그 호스트가 노출하는 도구 경로에 따라 달라집니다.

## Version

**v0.1.4 — Gemini literal-identity and arithmetic-consistency hardening**

GPT skill/package remains unchanged from v0.1.1 while GPT testing continues.

See [`CHANGELOG.md`](./CHANGELOG.md) and [`RELEASE_NOTES_v0.1.4.md`](./RELEASE_NOTES_v0.1.4.md).

## License

MIT — see [`LICENSE`](./LICENSE).
