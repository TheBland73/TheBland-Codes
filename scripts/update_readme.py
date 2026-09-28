#!/usr/bin/env python3
"""
从 LeetCode 中文站抓取统计数据并自动更新 README.md。

环境变量：
    LEETCODE_USERNAME   LeetCode 用户名（默认：thebland）
"""

import os
import re
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

import requests

# ================= 配置 =================
USERNAME = os.environ.get("LEETCODE_USERNAME", "thebland").strip()
README = Path("README.md")
GRAPHQL_URL = "https://leetcode.cn/graphql/"
HEADERS = {
    "Content-Type": "application/json",
    "Referer": f"https://leetcode.cn/u/{USERNAME}/",
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/122.0.0.0 Safari/537.36"
    ),
}

# ================= GraphQL =================
def gql(query, variables=None):
    r = requests.post(
        GRAPHQL_URL,
        json={"query": query, "variables": variables or {}},
        headers=HEADERS,
        timeout=30,
    )
    r.raise_for_status()
    payload = r.json()
    if "errors" in payload:
        raise RuntimeError(f"GraphQL error: {payload['errors']}")
    return payload["data"]


QUERY_PROGRESS = """
query userProfileUserQuestionProgressV2($userSlug: String!) {
  userProfileUserQuestionProgressV2(userSlug: $userSlug) {
    numAcceptedQuestions {
      count
      difficulty
    }
  }
}
"""

QUERY_TOTALS = """
query problemsetQuestionList($categorySlug: String, $limit: Int, $skip: Int, $filters: QuestionListFilterInput) {
  problemsetQuestionList: questionList(
    categorySlug: $categorySlug
    limit: $limit
    skip: $skip
    filters: $filters
  ) {
    total: totalNum
  }
}
"""

QUERY_LANGS = """
query languageStats($userSlug: String!) {
  userLanguageProblemCount(userSlug: $userSlug) {
    languageName
    problemsSolved
  }
}
"""

QUERY_CONTEST = """
query userContestRankingInfo($userSlug: String!) {
  userContestRanking(userSlug: $userSlug) {
    attendedContestsCount
    rating
    globalRanking
    totalParticipants
    topPercentage
  }
}
"""

# ================= 抓取 =================
def fetch_progress():
    data = gql(QUERY_PROGRESS, {"userSlug": USERNAME})
    result = {"easy": 0, "medium": 0, "hard": 0}
    for item in data["userProfileUserQuestionProgressV2"]["numAcceptedQuestions"]:
        key = item["difficulty"].lower()
        if key in result:
            result[key] = item["count"]
    return result


def fetch_totals():
    # 失败时的兜底值
    totals = {"easy": 1088, "medium": 2319, "hard": 1049}
    try:
        for diff in ["EASY", "MEDIUM", "HARD"]:
            data = gql(QUERY_TOTALS, {
                "categorySlug": "",
                "skip": 0,
                "limit": 1,
                "filters": {"difficulty": diff},
            })
            total = (data.get("problemsetQuestionList") or {}).get("total")
            if total:
                totals[diff.lower()] = total
    except Exception as e:
        print(f"警告：无法获取总题数，使用兜底值（{e}）", file=sys.stderr)
    return totals


def fetch_languages():
    try:
        data = gql(QUERY_LANGS, {"userSlug": USERNAME})
        return data.get("userLanguageProblemCount") or []
    except Exception as e:
        print(f"警告：无法获取语言数据（{e}）", file=sys.stderr)
        return []


def fetch_contest():
    try:
        data = gql(QUERY_CONTEST, {"userSlug": USERNAME})
        return data.get("userContestRanking") or {}
    except Exception as e:
        print(f"警告：无法获取竞赛数据（{e}）", file=sys.stderr)
        return {}

# ================= 渲染 =================
def bar(ratio, length=10):
    ratio = max(0.0, min(1.0, ratio))
    filled = round(ratio * length)
    return "█" * filled + "░" * (length - filled)


def pct(a, b):
    return f"{a / b * 100:.1f}%" if b else "0.0%"


def render_progress(solved, totals):
    e, m, h = solved["easy"], solved["medium"], solved["hard"]
    te, tm, th = totals["easy"], totals["medium"], totals["hard"]
    total = e + m + h
    t_total = te + tm + th

    return (
        "| 难度 | 已解决 | 总题数 | 进度 |\n"
        "| :---: | :---: | :---: | :--- |\n"
        f"| 🟢 简单 | {e} | {te} | `{bar(e / te if te else 0)}` {pct(e, te)} |\n"
        f"| 🟡 中等 | {m} | {tm} | `{bar(m / tm if tm else 0)}` {pct(m, tm)} |\n"
        f"| 🔴 困难 | {h} | {th} | `{bar(h / th if th else 0)}` {pct(h, th)} |\n"
        f"| **总计** | **{total}** | **{t_total}** | `{bar(total / t_total if t_total else 0)}` {pct(total, t_total)} |"
    )


LANG_DESC = {
    "python3": "主力语言，快速表达思路",
    "python": "主力语言，快速表达思路",
    "cpp": "对比 STL 与性能写法",
    "c": "手写底层结构，理解内存",
    "java": "面向对象视角对比",
    "golang": "并发与简洁语法",
    "javascript": "前端视角",
    "typescript": "类型化实现",
    "rust": "内存安全与零成本抽象",
    "go": "并发与简洁语法",
}


def render_language(langs):
    if not langs:
        return "_暂无数据_"
    lines = ["| 语言 | 解题数 | 用途 |", "| :---: | :---: | :--- |"]
    for item in sorted(langs, key=lambda x: -x["problemsSolved"]):
        name = item["languageName"]
        key = name.lower().replace(" ", "")
        desc = LANG_DESC.get(key, "—")
        lines.append(f"| {name} | {item['problemsSolved']} | {desc} |")
    return "\n".join(lines)


def render_contest(c):
    if not c:
        return "_暂无竞赛数据_"

    rating = c.get("rating")
    rating_str = f"{round(rating)}" if rating else "—"
    count = c.get("attendedContestsCount") or 0
    gr = c.get("globalRanking")
    tp = c.get("totalParticipants")
    if gr and tp:
        rank_str = f"{gr} / {tp}"
    elif gr:
        rank_str = f"{gr}"
    else:
        rank_str = "—"
    top = c.get("topPercentage")
    top_str = f"前 {top:.2f}%" if top else "—"

    return (
        "| 指标 | 数据 |\n"
        "| :--- | :--- |\n"
        f"| 竞赛分数 | {rating_str} |\n"
        f"| 参赛总数 | {count} 场 |\n"
        f"| 全球排名 | {rank_str} |\n"
        f"| 百分位 | {top_str} |"
    )


def render_updated():
    bj = timezone(timedelta(hours=8))
    now = datetime.now(bj).strftime("%Y-%m-%d %H:%M (UTC+8)")
    return f"🕒 最后更新：{now}"

# ================= 更新 README =================
def replace_section(content, start, end, new):
    pattern = re.compile(re.escape(start) + r".*?" + re.escape(end), re.DOTALL)
    if not pattern.search(content):
        print(f"警告：未找到标记 {start}", file=sys.stderr)
        return content
    return pattern.sub(f"{start}\n{new}\n{end}", content)


def main():
    print(f"正在获取 {USERNAME} 的 LeetCode 数据 ...")

    solved = fetch_progress()
    totals = fetch_totals()
    langs = fetch_languages()
    contest = fetch_contest()

    content = README.read_text(encoding="utf-8")

    # 更新顶部徽章中的“已解决-XXX 题”
    total = solved["easy"] + solved["medium"] + solved["hard"]
    content = re.sub(r"已解决-\d+%20题", f"已解决-{total}%20题", content)

    content = replace_section(
        content,
        "<!-- AUTO:PROGRESS:START -->",
        "<!-- AUTO:PROGRESS:END -->",
        render_progress(solved, totals),
    )
    content = replace_section(
        content,
        "<!-- AUTO:LANGUAGE:START -->",
        "<!-- AUTO:LANGUAGE:END -->",
        render_language(langs),
    )
    content = replace_section(
        content,
        "<!-- AUTO:CONTEST:START -->",
        "<!-- AUTO:CONTEST:END -->",
        render_contest(contest),
    )
    content = replace_section(
        content,
        "<!-- AUTO:UPDATED:START -->",
        "<!-- AUTO:UPDATED:END -->",
        render_updated(),
    )

    README.write_text(content, encoding="utf-8")
    print(f"✓ README 更新完成，共 {total} 题")


if __name__ == "__main__":
    main()
