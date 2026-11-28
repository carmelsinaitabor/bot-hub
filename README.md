## Quick Context Recovery (New Gemini Chat)
**Run `ctx` in Cloud Shell (or paste this command) to dump the full system architecture:**

**`gh api repos/carmelsinaitabor/bot-hub/contents/SYSTEM_ARCHITECTURE.md --jq '.content' | base64 -d`**

### How It Works
- **Cloud Shell Alias (`ctx`):** Stored in `~/.bashrc` on Google Cloud Shell (`dailydevotion-515202`); expands to the `gh api` command above to fetch and decode `SYSTEM_ARCHITECTURE.md` in one word.
- **Portable GitHub Script (`scripts/ctx`):** Committed directly in this repository with executable permissions (`chmod +x`, mode `100755`). Whenever `bot-hub` is cloned in Cloud Shell, a GitHub Actions runner, or another machine, run `./scripts/ctx` to print the latest handover document without relying on local shell aliases.
- **Source of Truth (`SYSTEM_ARCHITECTURE.md`):** Holds the live topology, entrypoints (`devotional_pipeline_v2.py` in SGT / UTC+8), Telegram webhook commands, and `gemini-3.8-flash` bot rules.

---

# bot-hub

<!-- BOT_CLI_HELPERS_START -->
## Multi-Repo Bot CLI Helpers

All helpers accept a short repository name (such as `tcm_basics`), a full `owner/repo` path, or no repository argument to default to `carmelsinaitabor/bible_dailydevotional`:

- **Check runs and open issues (`checkpipeline`):**
  - `checkpipeline tcm_basics` — lists recent workflow runs and open issues on `carmelsinaitabor/tcm_basics`
  - `checkpipeline carmelsinaitabor/temp_dump` — accepts full `owner/repo` syntax
  - `checkpipeline` — defaults to `carmelsinaitabor/bible_dailydevotional`
- **Assign a task or trigger Chief (`askchief`):**
  - `askchief tcm_basics "Audit index layout and check broken links"` — opens a `[Chief]` issue on `carmelsinaitabor/tcm_basics`
  - `askchief "Audit daily pipeline logs"` — opens a `[Chief]` issue on `carmelsinaitabor/bible_dailydevotional`
  - `askchief tcm_basics` — triggers `chief.yml` (or falls back to `bot_chief.yml`) directly without opening a new issue
- **Full daily status report (`dailyreport`):**
  - `dailyreport tcm_basics` — displays the latest 10 workflow runs, open issues, and open PRs on `carmelsinaitabor/tcm_basics`
  - `dailyreport` — defaults to `carmelsinaitabor/bible_dailydevotional`
- **Close specific issues (`closeissue`):**
  - `closeissue tcm_basics 1` — closes issue `#1` on `carmelsinaitabor/tcm_basics` (supports multiple issue numbers, e.g. `closeissue tcm_basics 1 2`)
  - `closeissue 12` — closes issue `#12` on `carmelsinaitabor/bible_dailydevotional`
- **Batch-close `bot-triage` issues (`closeissues`):**
  - `closeissues tcm_basics` — closes all open issues labeled `bot-triage` on `carmelsinaitabor/tcm_basics`
  - `closeissues` — batch-closes open `bot-triage` issues on `carmelsinaitabor/bible_dailydevotional`
- **Check scheduled workflows and next-day queue (`tomorrowcheck`):**
  - `tomorrowcheck tcm_basics` — lists active workflows and recent `schedule` runs on `carmelsinaitabor/tcm_basics`
  - `tomorrowcheck` — checks scheduled runs and displays the tail of `source_devotionals.txt` on `carmelsinaitabor/bible_dailydevotional`
  - `checkdevo` — Check the latest scheduled Daily Devotional run and step status
  - `addmusic` — Custom Cloud Shell CLI helper
  - `adhoc` — Custom Cloud Shell CLI helper
  - `checkchief` — Custom Cloud Shell CLI helper
  - `checkrun` — Custom Cloud Shell CLI helper
  - `checkwhatsapp` — Custom Cloud Shell CLI helper
  - `checkworkflow` — Custom Cloud Shell CLI helper
  - `csclean` — Custom Cloud Shell CLI helper
  - `cslist` — Custom Cloud Shell CLI helper
  - `csnuke` — Custom Cloud Shell CLI helper
  - `csstop` — Custom Cloud Shell CLI helper
  - `devo2` — Custom Cloud Shell CLI helper
  - `devopull` — Custom Cloud Shell CLI helper
  - `mixmusic` — Custom Cloud Shell CLI helper
  - `mp3list` — Custom Cloud Shell CLI helper
  - `readme` — Custom Cloud Shell CLI helper
  - `synctelegram` — Sync telegram_alert.yml and Telegram secrets across all repositories
  - `checktelegram` — Check recent runs and latest log of telegram_poller.yml in bot-hub
  - `wkissue` — Custom Cloud Shell CLI helper
  - `wkprev` — Custom Cloud Shell CLI helper
  - `wkstage` — Custom Cloud Shell CLI helper
  - `wkstatus` — Custom Cloud Shell CLI helper
  - `ls` — Cloud Shell helper command `ls`
  - `grep` — Cloud Shell helper command `grep`
  - `fgrep` — Cloud Shell helper command `fgrep`
  - `egrep` — Cloud Shell helper command `egrep`
  - `ll` — Cloud Shell helper command `ll`
  - `la` — Cloud Shell helper command `la`
  - `l` — Cloud Shell helper command `l`
  - `alert` — Cloud Shell helper command `alert`
  - `_devo_gh_token` — Cloud Shell helper command `_devo_gh_token`
  - `_resolve_carmel_repo` — Cloud Shell helper command `_resolve_carmel_repo`
<!-- BOT_CLI_HELPERS_END -->

## Carmel Bot Alerts (`/chief` via Telegram)

- **Assign a task to Chief:** Send `/chief <repo> <task>` in **Carmel Bot Alerts** (for example, `/chief bible_dailydevotional Check cover rotation warning`). Multi-line messages work too—line 1 becomes the issue title and subsequent lines become the issue body.
- **List commands & repos:** Send `/chief help`.
- **Timing & security:** GitHub Actions (`bot-hub/telegram_poller.yml`) polls Telegram automatically (typically every 5–15 minutes depending on GitHub's queue), ignores messages from any chat other than `TELEGRAM_CHAT_ID`, and replies with the created GitHub Issue link.

## Bot Operations Reference

### Telegram Commands (Carmel Bot Alerts)
- `/chief` — Run Chief triage on recent failures
- `/chief <issue_num>` — Triage a specific issue number
- `/chief <task>` — Create a new issue for Chief triage & Coder PR dispatch
- `/run` or `/run_devo` — Trigger `daily_devo2.yml` manually
- `/status` or `/s` — Check latest `daily_devo2.yml` status
- `/links` or `/wa` — Fetch WhatsApp dispatch links from Issue #2
- `/issues` or `/open` — List open bot issues
- `/stuck` — Check untriaged or stalled bot issues
- `/closed` — List recently closed issues
- `/help` — Show command menu

### Cloud Shell Helpers (`~/.bashrc`)
- `gh-open` — List open issues
- `gh-closed` — List recently closed issues
- `gh-resolved` — View recent PRs and closed issues
- `gh-stuck` — Identify untriaged issues or triaged issues without open bot PRs
- `gh-clean-tests` — Close test issues and delete `bot/fix-*` test PR branches
