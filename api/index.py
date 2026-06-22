import os
from flask import Flask, render_template, abort
from datetime import datetime, timedelta

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

app = Flask(
    __name__,
    template_folder=os.path.join(BASE_DIR, "templates"),
    static_folder=os.path.join(BASE_DIR, "static"),
    static_url_path="/static",
)

CAFE_NAME = "전국 맛집 탐방단"
CAFE_INTRO = "맛있는 정보를 나누는 사람들 🍜"
MEMBER_COUNT = 128934
TODAY_VISIT = 4271
TOTAL_VISIT = 9824011

BOARDS = [
    {"id": "notice", "name": "📌 공지사항", "desc": "카페 운영 공지"},
    {"id": "free", "name": "💬 자유게시판", "desc": "자유롭게 이야기해요"},
    {"id": "review", "name": "🍽️ 맛집 후기", "desc": "다녀온 맛집 후기 공유"},
    {"id": "qna", "name": "❓ 맛집 질문", "desc": "맛집 추천 받아요"},
    {"id": "market", "name": "🛍️ 장터", "desc": "식기/식자재 나눔 장터"},
]

GRADES = [
    {"name": "씨앗", "icon": "🌱", "min": 0},
    {"name": "새싹", "icon": "🌿", "min": 10},
    {"name": "나무", "icon": "🌳", "min": 50},
    {"name": "열매", "icon": "🍎", "min": 150},
    {"name": "카페마스터", "icon": "👑", "min": 500},
]

def grade_for(score):
    g = GRADES[0]
    for gr in GRADES:
        if score >= gr["min"]:
            g = gr
    return g

POSTS = [
    {
        "id": 1, "board": "notice", "title": "[필독] 카페 가입 인사 & 등업 안내",
        "author": "카페매니저", "score": 999, "date": datetime.now() - timedelta(days=2),
        "views": 15234, "likes": 482, "comments": 37, "is_notice": True,
        "content": "안녕하세요! 전국 맛집 탐방단에 가입해주셔서 감사합니다.\n가입 인사 게시판에 인사를 남겨주시면 등업이 진행됩니다.\n매주 맛집 정모도 진행하니 많은 참여 부탁드려요!",
    },
    {
        "id": 2, "board": "notice", "title": "[이벤트] 9월 맛집 사진 공모전 - 상품 50만원",
        "author": "카페매니저", "score": 999, "date": datetime.now() - timedelta(days=5),
        "views": 8341, "likes": 301, "comments": 52, "is_notice": True,
        "content": "9월 한달간 맛집 사진 공모전을 진행합니다! 베스트 사진에게는 50만원 상당의 상품권을 드려요.",
    },
    {
        "id": 3, "board": "review", "title": "강남역 노포 곱창집 후기 (사진 30장)",
        "author": "곱창러버", "score": 320, "date": datetime.now() - timedelta(hours=3),
        "views": 5123, "likes": 211, "comments": 44,
        "content": "강남역 뒷골목에 숨어있는 곱창집을 다녀왔습니다. 가격도 착하고 양도 푸짐해서 강추합니다!\n분위기도 옛날 느낌 그대로라 정겨웠어요.",
    },
    {
        "id": 4, "board": "review", "title": "을지로 노가리골목 직접 가본 후기",
        "author": "맥주왕김부장", "score": 88, "date": datetime.now() - timedelta(hours=7),
        "views": 3210, "likes": 134, "comments": 28,
        "content": "을지로 노가리골목은 분위기 하나로 가는 곳! 노가리에 시원한 맥주 한잔, 직장인들의 힐링 코스입니다.",
    },
    {
        "id": 5, "board": "qna", "title": "성수동 데이트 맛집 추천해주세요 ㅠㅠ",
        "author": "곧소개팅", "score": 12, "date": datetime.now() - timedelta(hours=1),
        "views": 982, "likes": 9, "comments": 21,
        "content": "다음주에 성수동에서 소개팅이 있는데 분위기 좋은 맛집 추천 부탁드려요! 예산은 인당 5만원 정도입니다.",
    },
    {
        "id": 6, "board": "qna", "title": "부산 여행 중인데 회 맛집 어디가 좋을까요?",
        "author": "부산초보", "score": 5, "date": datetime.now() - timedelta(minutes=40),
        "views": 421, "likes": 4, "comments": 13,
        "content": "이번 주말 부산 여행 가는데 자갈치시장 근처 회 맛집 추천 부탁드립니다!",
    },
    {
        "id": 7, "board": "free", "title": "오늘 점심 뭐드셨나요? 저는 김치찌개",
        "author": "점심이고민", "score": 45, "date": datetime.now() - timedelta(hours=2),
        "views": 1532, "likes": 22, "comments": 31,
        "content": "다들 점심 뭐 드셨나요~ 저는 회사 앞 분식집에서 김치찌개 먹었어요. 다들 점메추 부탁드려요!",
    },
    {
        "id": 8, "board": "free", "title": "맛집 탐방 다닐 때 카메라 추천 좀",
        "author": "사진초보", "score": 30, "date": datetime.now() - timedelta(hours=10),
        "views": 980, "likes": 15, "comments": 19,
        "content": "맛집 사진 예쁘게 찍으려고 하는데 가벼운 미러리스 카메라 추천해주실 분 있을까요?",
    },
    {
        "id": 9, "board": "market", "title": "안쓰는 에어프라이어 무료 나눔합니다",
        "author": "정리의신", "score": 60, "date": datetime.now() - timedelta(days=1),
        "views": 2210, "likes": 88, "comments": 40,
        "content": "이사 가면서 거의 새 제품인 에어프라이어 무료로 나눔합니다. 댓글로 신청해주세요!",
    },
    {
        "id": 10, "board": "market", "title": "수제 전통 고추장 판매합니다 (직접 담음)",
        "author": "시골할머니손맛", "score": 200, "date": datetime.now() - timedelta(hours=15),
        "views": 1890, "likes": 67, "comments": 22,
        "content": "친정에서 직접 담은 전통 고추장 소량 판매합니다. 깊은 맛이 일품이에요!",
    },
]

def time_ago(dt):
    diff = datetime.now() - dt
    if diff.days >= 1:
        return f"{diff.days}일 전"
    hours = diff.seconds // 3600
    if hours >= 1:
        return f"{hours}시간 전"
    minutes = (diff.seconds % 3600) // 60
    return f"{minutes}분 전"

def board_name(bid):
    for b in BOARDS:
        if b["id"] == bid:
            return b["name"]
    return bid

def decorate(post):
    p = dict(post)
    p["time_ago"] = time_ago(post["date"])
    p["grade"] = grade_for(post["score"])
    p["board_name"] = board_name(post["board"])
    return p

@app.route("/")
def index():
    notices = [decorate(p) for p in POSTS if p.get("is_notice")]
    recent = sorted(
        [decorate(p) for p in POSTS if not p.get("is_notice")],
        key=lambda x: x["date"], reverse=True
    )
    best = sorted(POSTS, key=lambda x: x["likes"], reverse=True)[:5]
    best = [decorate(p) for p in best]
    return render_template(
        "index.html",
        cafe_name=CAFE_NAME, cafe_intro=CAFE_INTRO,
        member_count=MEMBER_COUNT, today_visit=TODAY_VISIT, total_visit=TOTAL_VISIT,
        boards=BOARDS, notices=notices, recent=recent, best=best,
    )

@app.route("/board/<board_id>")
def board(board_id):
    b = next((x for x in BOARDS if x["id"] == board_id), None)
    if not b:
        abort(404)
    posts = sorted(
        [decorate(p) for p in POSTS if p["board"] == board_id],
        key=lambda x: x["date"], reverse=True
    )
    return render_template(
        "board.html", cafe_name=CAFE_NAME, cafe_intro=CAFE_INTRO, boards=BOARDS, board=b, posts=posts,
        member_count=MEMBER_COUNT, today_visit=TODAY_VISIT, total_visit=TOTAL_VISIT,
    )

@app.route("/post/<int:post_id>")
def post(post_id):
    p = next((x for x in POSTS if x["id"] == post_id), None)
    if not p:
        abort(404)
    p = decorate(p)
    others = sorted(
        [decorate(x) for x in POSTS if x["board"] == p["board"] and x["id"] != post_id],
        key=lambda x: x["date"], reverse=True
    )[:5]
    return render_template(
        "post.html", cafe_name=CAFE_NAME, cafe_intro=CAFE_INTRO, boards=BOARDS, post=p, others=others,
        member_count=MEMBER_COUNT, today_visit=TODAY_VISIT, total_visit=TOTAL_VISIT,
    )

@app.errorhandler(404)
def not_found(e):
    return render_template(
        "404.html", cafe_name=CAFE_NAME, cafe_intro=CAFE_INTRO, boards=BOARDS,
        member_count=MEMBER_COUNT, today_visit=TODAY_VISIT, total_visit=TOTAL_VISIT,
    ), 404

if __name__ == "__main__":
    # 로컬 테스트용 (vercel dev 또는 python api/index.py)
    app.run(debug=True, port=5000)
