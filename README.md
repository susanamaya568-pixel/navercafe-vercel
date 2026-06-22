# 전국 맛집 탐방단 — 네이버 카페 스타일 (Vercel 배포용)

Flask로 만든 네이버 카페 느낌의 커뮤니티 데모입니다. Vercel 서버리스 Python 런타임(`@vercel/python`)으로 배포할 수 있도록 구성되어 있습니다.

## 폴더 구조

```
navercafe-vercel/
├── api/
│   └── index.py        # Flask 앱 (Vercel 서버리스 함수 엔트리포인트)
├── templates/           # Jinja2 템플릿 (base, index, board, post, 404)
├── static/
│   └── css/style.css    # 화려한 네이버 그린 톤 스타일시트
├── vercel.json           # Vercel 빌드 / 라우팅 설정
├── requirements.txt      # Python 의존성
└── .vercelignore
```

## 로컬에서 먼저 확인하기

```bash
pip install -r requirements.txt
python api/index.py
# http://localhost:5000 접속
```

## Vercel로 배포하기

### 방법 1: Vercel CLI

```bash
npm install -g vercel   # CLI가 없다면 설치
cd navercafe-vercel
vercel login
vercel            # 처음엔 질문에 답하며 프로젝트 생성 (Preview 배포)
vercel --prod     # 프로덕션 배포
```

### 방법 2: GitHub 연동

1. 이 폴더를 GitHub 저장소로 푸시합니다.
2. https://vercel.com/new 에서 해당 저장소를 Import 합니다.
3. Framework Preset은 "Other"로 두고, Root Directory를 이 폴더(`navercafe-vercel`)로 지정합니다.
4. Build/Output 설정은 그대로 두면 `vercel.json`을 읽어 자동으로 처리됩니다.
5. Deploy 클릭 → 끝.

배포가 끝나면 `https://<프로젝트명>.vercel.app` 주소로 바로 접속할 수 있습니다.

## 동작 구조 참고

- Vercel은 `api/` 폴더 안의 파이썬 파일을 서버리스 함수로 인식합니다. `api/index.py`에서 `app` 변수로 export된 Flask(WSGI) 앱을 그대로 핸들러로 사용합니다.
- `vercel.json`의 `routes`로 모든 요청(`/(.*)`)을 `api/index.py`로 보내고, `/static/(.*)`는 정적 파일로 직접 서빙합니다.
- 템플릿/정적 파일 경로는 `api/index.py` 안에서 프로젝트 루트 기준 절대경로로 지정되어 있어 서버리스 환경에서도 정상 동작합니다.

## 커스터마이징

`api/index.py` 상단의 `CAFE_NAME`, `BOARDS`, `POSTS` 데이터를 수정하면 카페 이름, 게시판 구성, 게시글 내용을 바로 바꿀 수 있습니다. 현재는 메모리 내 더미 데이터라 서버리스 함수가 재시작되면(=거의 매 요청마다 콜드 스타트 가능) 초기 데이터로 리셋됩니다. 실제 글쓰기/댓글 기능이 필요하면 Vercel Postgres, Supabase, PlanetScale 같은 외부 DB 연동이 필요합니다.
