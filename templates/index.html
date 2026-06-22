{% extends "base.html" %}
{% block content %}

<div class="notice-board">
  <h2 class="board-section-title">📌 공지사항</h2>
  <ul class="post-list notice-list">
    {% for p in notices %}
    <li class="post-row">
      <a href="{{ url_for('post', post_id=p.id) }}" class="post-link">
        <span class="badge badge-notice">공지</span>
        <span class="post-title">{{ p.title }}</span>
        <span class="comment-count">[{{ p.comments }}]</span>
      </a>
      <span class="post-meta">{{ p.author }} · {{ p.time_ago }} · 조회 {{ "{:,}".format(p.views) }}</span>
    </li>
    {% endfor %}
  </ul>
</div>

<div class="main-grid">
  <div class="main-col">
    <h2 class="board-section-title">🆕 새 글</h2>
    <ul class="post-list">
      {% for p in recent %}
      <li class="post-row">
        <a href="{{ url_for('post', post_id=p.id) }}" class="post-link">
          <span class="badge badge-board">{{ p.board_name }}</span>
          <span class="post-title">{{ p.title }}</span>
          <span class="comment-count">[{{ p.comments }}]</span>
          {% if p.time_ago.endswith("분 전") %}<span class="badge badge-new">NEW</span>{% endif %}
        </a>
        <span class="post-meta">
          <span class="g-icon">{{ p.grade.icon }}</span>{{ p.author }} · {{ p.time_ago }} · 조회 {{ "{:,}".format(p.views) }} · 추천 {{ p.likes }}
        </span>
      </li>
      {% endfor %}
    </ul>
  </div>

  <div class="side-col">
    <div class="best-box">
      <h3 class="side-title">🔥 실시간 인기글</h3>
      <ol class="best-list">
        {% for p in best %}
        <li>
          <a href="{{ url_for('post', post_id=p.id) }}">
            <span class="rank-num rank-{{ loop.index }}">{{ loop.index }}</span>
            <span class="best-title">{{ p.title }}</span>
          </a>
        </li>
        {% endfor %}
      </ol>
    </div>
  </div>
</div>

{% endblock %}
