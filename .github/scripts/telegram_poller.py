import json
import os
import urllib.error
import urllib.parse
import urllib.request

BOT_TOKEN = os.environ["TELEGRAM_BOT_TOKEN"].strip()
ALLOWED_CHAT_ID = str(os.environ["TELEGRAM_CHAT_ID"]).strip()
GH_TOKEN = os.environ["GH_TOKEN"].strip()
OWNER = "carmelsinaitabor"

TG_API = f"https://api.telegram.org/bot{BOT_TOKEN}"
GH_API = "https://api.github.com"


def tg_call(method: str, params: dict | None = None) -> dict:
    url = f"{TG_API}/{method}"
    data = urllib.parse.urlencode(params).encode("utf-8") if params else None
    req = urllib.request.Request(url, data=data)
    with urllib.request.urlopen(req, timeout=20) as resp:
        return json.loads(resp.read().decode("utf-8"))


def gh_call(method: str, path: str, payload: dict | None = None) -> dict | list:
    url = f"{GH_API}{path}"
    body = json.dumps(payload).encode("utf-8") if payload is not None else None
    headers = {
        "Authorization": f"Bearer {GH_TOKEN}",
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
        "User-Agent": "carmel-telegram-poller",
    }
    if body is not None:
        headers["Content-Type"] = "application/json"
    req = urllib.request.Request(url, data=body, headers=headers, method=method)
    with urllib.request.urlopen(req, timeout=20) as resp:
        raw = resp.read().decode("utf-8")
        return json.loads(raw) if raw else {}


def list_active_repos() -> list[str]:
    repos = gh_call("GET", f"/users/{OWNER}/repos?per_page=100&type=owner")
    return sorted(
        r["name"] for r in repos if not r.get("archived") and not r.get("disabled")
    )


def send_reply(chat_id: str, text: str) -> None:
    tg_call(
        "sendMessage",
        {
            "chat_id": chat_id,
            "text": text,
            "disable_web_page_preview": "true",
        },
    )


def handle_chief_command(chat_id: str, text: str) -> None:
    lines = text.strip().splitlines()
    first_line = lines[0].strip()
    extra_lines = "\n".join(lines[1:]).strip()

    parts = first_line.split(maxsplit=2)
    # parts[0] is /chief or /chief@BotName
    if len(parts) < 2 or parts[1].lower() in {"help", "?"}:
        repos = list_active_repos()
        repo_list = "\n".join(f"• {r}" for r in repos)
        send_reply(
            chat_id,
            "Usage:\n/chief <repo> <task description>\n\n"
            "Example:\n/chief bible_dailydevotional Check cover rotation\n\n"
            f"Available repositories:\n{repo_list}",
        )
        return

    repo = parts[1].strip()
    inline_task = parts[2].strip() if len(parts) > 2 else ""

    if not inline_task and not extra_lines:
        send_reply(
            chat_id,
            f"Missing task description.\nFormat: /chief {repo} <what you want Chief to do>",
        )
        return

    repos = list_active_repos()
    if repo not in repos:
        repo_list = ", ".join(repos)
        send_reply(
            chat_id,
            f"Repository '{repo}' not found under {OWNER}.\nValid repos: {repo_list}",
        )
        return

    title_source = inline_task or extra_lines.splitlines()[0]
    title = title_source[:120]
    full_body = f"{inline_task}\n\n{extra_lines}".strip() if inline_task and extra_lines else (inline_task or extra_lines)
    issue_body = f"{full_body}\n\n---\n_Dispatched via Carmel Bot Alerts (Telegram)_"

    issue = gh_call(
        "POST",
        f"/repos/{OWNER}/{repo}/issues",
        {"title": title, "body": issue_body},
    )
    send_reply(
        chat_id,
        f"Issue #{issue['number']} opened on {repo}:\n{issue['html_url']}",
    )


def main() -> None:
    res = tg_call("getUpdates", {"timeout": 2})
    updates = res.get("result", [])
    if not updates:
        print("No new Telegram updates.")
        return

    max_update_id = max(u["update_id"] for u in updates)

    for upd in updates:
        msg = upd.get("message")
        if not msg:
            continue
        chat_id = str(msg.get("chat", {}).get("id", ""))
        if chat_id != ALLOWED_CHAT_ID:
            continue
        text = (msg.get("text") or "").strip()
        if text.startswith("/chief") or text.startswith("/help"):
            try:
                handle_chief_command(chat_id, text)
            except Exception as exc:
                send_reply(chat_id, f"Failed to create issue: {exc}")

    # Acknowledge all updates up to max_update_id so Telegram clears them from the queue
    tg_call("getUpdates", {"offset": max_update_id + 1, "timeout": 1})
    print(f"Processed {len(updates)} update(s); offset advanced to {max_update_id + 1}.")


if __name__ == "__main__":
    main()
