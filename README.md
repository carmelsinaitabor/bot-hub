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
  - `wkissue` — Custom Cloud Shell CLI helper
  - `wkprev` — Custom Cloud Shell CLI helper
  - `wkstage` — Custom Cloud Shell CLI helper
  - `wkstatus` — Custom Cloud Shell CLI helper
<!-- BOT_CLI_HELPERS_END -->

## Carmel Bot Alerts (`/chief` via Telegram)

- **Assign a task to Chief:** Send `/chief <repo> <task>` in **Carmel Bot Alerts** (for example, `/chief bible_dailydevotional Check cover rotation warning`). Multi-line messages work too—line 1 becomes the issue title and subsequent lines become the issue body.
- **List commands & repos:** Send `/chief help`.
- **Timing & security:** GitHub Actions (`bot-hub/telegram_poller.yml`) polls Telegram automatically (typically every 5–15 minutes depending on GitHub's queue), ignores messages from any chat other than `TELEGRAM_CHAT_ID`, and replies with the created GitHub Issue link.
