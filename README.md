# bot-hub

<!-- BOT_CLI_HELPERS_START -->
## How to Use `checkpipeline` and `askchief` Across Any Repository

- **Check runs and open issues on any repo:**
  - `checkpipeline tcm_basics` — checks `carmelsinaitabor/tcm_basics`
  - `checkpipeline carmelsinaitabor/temp_dump` — accepts full `owner/repo` syntax too
  - `checkpipeline` — defaults to `carmelsinaitabor/bible_dailydevotional`
- **Assign a task to Chief on any repo (opens a `[Chief]` issue):**
  - `askchief tcm_basics "Audit index layout and check broken links"`
  - `askchief "Audit daily pipeline logs"` — defaults to `carmelsinaitabor/bible_dailydevotional` when no repo is specified
- **Trigger an immediate Chief triage run without opening a new issue:**
  - `askchief tcm_basics` — tries `chief.yml` first and falls back to `bot_chief.yml` for older repo setups
<!-- BOT_CLI_HELPERS_END -->
