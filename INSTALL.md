# Installation Guide / 설치 가이드

이 저장소는 두 개의 독립 Agent Skill을 제공합니다.

- **GPT Lite**: `long-image-ocr-gpt-lite/`
- **Gemini Lite**: `long-image-ocr-gemini-lite/`

저장소 전체를 하나의 스킬로 설치하는 것이 아니라, 사용하는 호스트에 맞는 **하위 스킬 폴더를 선택**하는 것을 권장합니다.

Repository:

`https://github.com/legendrlabs/KOREAN-LONG-IMAGE-OCR-TOOL-LITE`

---

## 1. ChatGPT 웹 / 앱

### 권장: Skill-only Plugin으로 사용

ChatGPT의 Plugin Creator를 사용할 수 있는 계정에서는 GPT Lite를 **외부 앱 연결이 없는 skill-only plugin**으로 만드는 방식이 가장 적합합니다.

1. ChatGPT 사이드바에서 **Plugins**를 엽니다.
2. **Plugin Creator**를 설치하거나 `Add (+)`에서 Plugin Creator 대화를 시작합니다.
3. 다음 파일을 Plugin Creator에 전달합니다.

   `long-image-ocr-gpt-lite/SKILL.md`

4. 다음처럼 요청합니다.

```text
이 SKILL.md를 포함하는 skill-only plugin을 만들어줘.
플러그인 이름은 Long Image OCR GPT Lite로 하고,
외부 앱이나 MCP 연결은 추가하지 마.
다중 이미지 OCR/복원 작업에서 자동으로 사용될 수 있게 해줘.
```

5. 생성된 로컬 플러그인을 테스트합니다.
6. 새 채팅에서 필요하면 `@Long Image OCR GPT Lite`처럼 직접 호출합니다.

> ChatGPT의 플러그인/스킬 이용 가능 범위는 플랜, 계정, 워크스페이스 및 제품 화면에 따라 다를 수 있습니다.

### ChatGPT Skills 기능이 직접 제공되는 계정

Skills 화면이 보이는 계정에서는:

1. **Plugins → Skills**로 이동합니다.
2. **Create** 또는 **Upload from your computer**를 선택합니다.
3. `long-image-ocr-gpt-lite` 스킬을 업로드합니다.
4. 설치 후 새 채팅에서 OCR 작업으로 동작을 확인합니다.

### 중요: GitHub URL만 붙여 넣는 방식

일반 ChatGPT 웹에서는 이 저장소 URL만 대화에 붙여 넣는 것만으로 **항상 영구 스킬 설치가 되는 것은 아닙니다**.

GitHub 링크 자체를 배포 원본으로 사용하되, ChatGPT에서는 Plugin Creator 또는 제공되는 Skills 설치 UI를 사용하는 것을 권장합니다.

---

## 2. Codex

Codex는 GitHub repository의 특정 스킬 경로에서 설치할 수 있습니다.

### 대화형 설치

Codex에서 skill installer를 사용할 수 있다면 다음 GitHub 디렉터리를 설치하도록 요청합니다.

```text
$skill-installer install https://github.com/legendrlabs/KOREAN-LONG-IMAGE-OCR-TOOL-LITE/tree/main/long-image-ocr-gpt-lite
```

또는 자연어로:

```text
Install the skill from:
https://github.com/legendrlabs/KOREAN-LONG-IMAGE-OCR-TOOL-LITE/tree/main/long-image-ocr-gpt-lite
```

설치 후 Codex가 새 스킬을 인식하도록 **Codex를 재시작**하는 것을 권장합니다.

### 수동 설치

GPT Lite 스킬 폴더를 Codex skills 디렉터리 아래에 배치할 수도 있습니다.

예시:

```text
~/.codex/skills/long-image-ocr-gpt-lite/SKILL.md
```

프로젝트 단위 Agent Skills를 사용하는 환경이라면 호스트가 지원하는 `.agents/skills/` 구조에 배치할 수 있습니다.

---

## 3. Gemini CLI

Gemini Lite는 **Gemini CLI의 Git repository skill 설치 기능**을 기준으로 배포합니다.

### 사용자 전체에 설치

```bash
gemini skills install https://github.com/legendrlabs/KOREAN-LONG-IMAGE-OCR-TOOL-LITE.git --path long-image-ocr-gemini-lite --scope user
```

### 현재 workspace에만 설치

```bash
gemini skills install https://github.com/legendrlabs/KOREAN-LONG-IMAGE-OCR-TOOL-LITE.git --path long-image-ocr-gemini-lite --scope workspace
```

설치 확인:

```bash
gemini skills list
```

이미 Gemini CLI 대화형 세션을 열어둔 상태에서 설치했다면 다음 명령으로 다시 읽습니다.

```text
/skills reload
```

또는:

```text
/skills refresh
```

그 후:

```text
/skills list
```

으로 `long-image-ocr-gemini-lite`가 보이는지 확인합니다.

### 개발 중 로컬 링크

저장소를 clone한 뒤 로컬 스킬을 바로 테스트할 수도 있습니다.

```bash
git clone https://github.com/legendrlabs/KOREAN-LONG-IMAGE-OCR-TOOL-LITE.git
cd KOREAN-LONG-IMAGE-OCR-TOOL-LITE

gemini skills link ./long-image-ocr-gemini-lite --scope user
```

---

## 4. 설치 확인 테스트

설치 후 아래 정도의 요청으로 동작을 확인할 수 있습니다.

### GPT Lite 테스트

```text
이 스크린샷 여러 장을 날짜 순서대로 읽어서 표로 복원해줘.
긴 작업이면 작은 배치로 나누고, 배치마다 진행률과 체크포인트를 알려줘.
원본에서 확인되지 않은 상세값은 추정하지 마.
```

기대 동작:

- 작은 배치 단위 처리
- `20/70` 같은 숫자 진행률
- 완료 배치 저장/체크포인트
- 타임아웃 또는 중단 시 첫 미검증 소스부터 재개
- 미확인 상세값을 합계행으로 날조하지 않음

### Gemini Lite 테스트

```text
이 Drive 폴더의 이미지들을 원본 기준으로 읽어서 상세 데이터를 복원해줘.
색인 텍스트와 실제 이미지 픽셀 확인 여부를 구분하고,
원본을 직접 보지 못한 항목은 미복원으로 남겨줘.
```

기대 동작:

- 원본 픽셀 접근 경로 우선 확인
- `DIRECT_PIXEL_VERIFIED / TEXT_INDEX_ONLY / METADATA_ONLY / UNAVAILABLE` 구분
- `PORTFOLIO` 같은 가짜 상세행 생성 금지
- 화면 표시 수치 우선 보존
- 부분 검증을 전체 완료라고 표현하지 않음

---

## 5. 어떤 버전을 설치해야 하나?

| 환경 | 권장 스킬 |
|---|---|
| ChatGPT 웹/앱 | `long-image-ocr-gpt-lite` |
| Codex | `long-image-ocr-gpt-lite` |
| Gemini CLI | `long-image-ocr-gemini-lite` |

두 스킬은 같은 원칙을 공유하지만, 각 모델/호스트에서 반복적으로 나타난 실패 양상에 맞춰 강조점이 다릅니다.

---

## 6. 업데이트

GitHub에서 새 버전이 배포되면 설치 방식에 따라 갱신 방법이 다릅니다.

- **ChatGPT Plugin/Skill**: Plugin Creator 또는 Skills UI에서 기존 설치본을 업데이트/교체합니다.
- **Codex**: 기존 스킬을 업데이트하거나 재설치한 뒤 필요하면 Codex를 재시작합니다.
- **Gemini CLI**: 기존 스킬을 제거 후 재설치하거나 지원되는 업데이트 흐름을 사용한 뒤 `/skills reload`를 실행합니다.

업데이트 전에는 기존 사용자 수정본이 있다면 별도로 백업하십시오.

---

## 7. 제거

### Gemini CLI

```bash
gemini skills uninstall long-image-ocr-gemini-lite
```

### Codex

Codex의 설치된 skill 디렉터리 또는 해당 skill installer의 제거 절차를 사용합니다.

### ChatGPT

Plugins 또는 Skills 화면에서 해당 플러그인/스킬을 제거합니다.

---

## 주의사항

이 저장소는 OCR 엔진 자체가 아닙니다.

이 스킬들은 모델이 이미지 기반 복원 작업을 수행할 때 다음을 강제하는 **작업 프로토콜**입니다.

- 원본 근거 우선
- 색인 텍스트와 이미지 픽셀 구분
- 미확인 데이터 추정 금지
- 긴 작업의 배치 처리
- 진행률 표시
- 체크포인트/재개
- 독립 검산
- 부분 완료의 과장 금지

실제 이미지 접근 가능 여부와 사용할 수 있는 OCR/vision 도구는 설치되는 호스트 환경에 따라 달라집니다.
