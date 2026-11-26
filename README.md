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
<!-- BOT_CLI_HELPERS_END -->
