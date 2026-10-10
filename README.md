# KOREAN LONG IMAGE OCR TOOL LITE

> **AGENT SKILL / SKILL-ONLY PLUGIN PACKAGE — NOT AN OCR APPLICATION**
>
> 이 저장소는 OCR 실행 프로그램, API 래퍼, 이미지 슬라이서, 로컬 서버가 아닙니다. `GEMINI_API_KEY`, EasyOCR, Tesseract 또는 별도 OCR 스크립트를 요구하지 않습니다. 설치되는 호스트(ChatGPT/Codex/Gemini)가 제공하는 vision·file·connector 기능을 더 안전하고 일관되게 사용하도록 만드는 작업 프로토콜입니다.

한국어 장문 스크린샷·다중 이미지 OCR/복원 작업을 위한 경량 Agent Skill 배포판입니다.

**Current repository version: v0.1.3**

- [설치 가이드](./INSTALL.md)
- [v0.1.3 릴리스 노트](./RELEASE_NOTES_v0.1.3.md)
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

현재 호스트가 영구 스킬 등록 기능을 제공하지 않으면, Markdown을 현재 대화에 로드해 사용할 수는 있어도 영구 설치했다고 표현하면 안 됩니다.

### Gemini CLI fallback

```bash
gemini skills install https://github.com/legendrlabs/KOREAN-LONG-IMAGE-OCR-TOOL-LITE.git --path skills/long-image-ocr-gemini-lite --scope user
```

또는 current `.skill` package:

```text
dist/long-image-ocr-gemini-lite-v0.1.3.skill
```

설치 후 실행 중인 Gemini CLI 세션에서는:

```text
/skills reload
```

### ChatGPT / Codex — GPT Lite

GPT 경로는 **v0.1.1과 동일하게 유지**합니다. 현재 ChatGPT Work 테스트 운용 중인 GPT skill 본문과 plugin package는 v0.1.3에서 변경하지 않습니다.

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
| Gemini Lite | `skills/long-image-ocr-gemini-lite/SKILL.md` | native vision, source modality/coverage, 7-phase OCR workflow, anti-fabrication, structured-output validation |

## Gemini Lite v0.1.3 highlights

Gemini Lite는 이제 **instruction-only, evidence-only native-vision protocol**로 명시됩니다.

핵심 규칙:

- 외부 OCR/Python/MCP/API/Cloud Run/로컬 실행기/`GEMINI_API_KEY` 앱으로 재해석 금지
- image pixels와 Drive/workspace indexed text를 구분
- `DIRECT_PIXEL_VERIFIED / TEXT_INDEX_ONLY / METADATA_ONLY / UNAVAILABLE` per-source 상태 유지
- 모든 접근 가능한 source를 확인하기 전 완료 선언 금지
- 반복 패턴이나 계좌 합계로 누락 상세행 생성 금지
- 화면 표시값을 계산값으로 덮어쓰기 금지
- 7-phase workflow:
  1. Layout reconnaissance
  2. Segmented reading
  3. Boundary reconciliation
  4. Precision pass
  5. Low-confidence pass
  6. Reconstruction
  7. Audit
- CSV quoting / spreadsheet cell boundary / formula-reference 검증
- 합계는 final structured rows에서 재계산하고 include/exclude 기준을 명시
- 검증은 결과물이 아니라 gate이며, 검증 후 사용자가 요청한 실제 결과물까지 계속 생성

## Core guarantees

두 배포판 모두 다음 원칙을 공유합니다.

1. 원본 이미지 픽셀을 직접 확인하지 않았으면 시각 검증했다고 주장하지 않습니다.
2. 종목/행/항목 상세를 모르면 계좌 합계나 요약값으로 상세 데이터를 만들어내지 않습니다.
3. 화면에 표시된 수치와 계산·추정 수치를 구분합니다.
4. 일부만 검증한 결과를 전체 완료라고 표현하지 않습니다.
5. 집계값을 그대로 복사한 뒤 다시 비교하는 순환 검산을 인정하지 않습니다.

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
└─ RELEASE_NOTES_v0.1.3.md
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

이 저장소는 다음을 제공하지 않습니다.

- 자체 OCR 엔진
- Gemini/OpenAI API 호출 애플리케이션
- EasyOCR/Tesseract 설치 프로그램
- 이미지 자동 분할 실행기
- 백그라운드 서버

실제 이미지 접근, OCR/vision 성능, Drive 원본 접근 가능 여부는 설치되는 호스트와 그 호스트가 노출하는 도구 경로에 따라 달라집니다.

## Version

**v0.1.3 — Gemini native-vision workflow merge**

GPT skill/package remains unchanged from v0.1.1 while GPT testing continues.

See [`CHANGELOG.md`](./CHANGELOG.md) and [`RELEASE_NOTES_v0.1.3.md`](./RELEASE_NOTES_v0.1.3.md).

## License

MIT — see [`LICENSE`](./LICENSE).
