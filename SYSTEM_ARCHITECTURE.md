# Carmel Multi-Bot & Daily Devotional Architecture (SGT / UTC+8)

## 1. Repositories & Entrypoints
- **Central Hub:** `carmelsinaitabor/bot-hub` (reusable workflows: `reusable_chief.yml`, `reusable_coder.yml`, `reusable_tester.yml`, `reusable_telegram.yml`, `reusable_whatsapp.yml`, `reusable_health_5am.yml`, `reusable_weekly_stage.yml`). `telegram_poller.yml` is disabled.
- **Primary Pipeline:** `carmelsinaitabor/bible_dailydevotional`
  - **Canonical Production Script:** `devotional_pipeline_v2.py` (enforces `Asia/Singapore` via `PIPELINE_TIMEZONE` / `ZoneInfo("Asia/Singapore")`).
  - **Primary Workflow:** `.github/workflows/daily_devo2.yml` (publishes Notion toggles/archives + Google Drive MP3s for CMN, YUE, EN, ES).
  - **Caller Workflows:** `bot_chief.yml`, `bot_coder.yml` (both use `secrets: inherit`).

## 2. Cloud & Webhook Infrastructure
- **GCP Project:** `dailydevotion-515202` (region `asia-southeast1`)
- **Cloud Run Service:** `telegram-devo-webhook` (`~/telegram-webhook/main.py` in Cloud Shell)
  - `/chief <task>`: Creates a GitHub Issue and dispatches `bot_chief.yml`.
  - `/run_devo` or `/run`: Dispatches `daily_devo2.yml`.
  - `/status` or `/s`: Checks latest `daily_devo2.yml` run.
  - `/links` or `/wa`: Fetches latest WhatsApp links from Issue #2.

## 3. Bot Rules & Active Model
- **AI Model:** `gemini-3.8-flash` across `bot-hub` workflows.
- **Chief (`Bot 1`):** Triages issues/failures and sets `Dispatch Coder: true` only for actionable code/workflow edits (skips status-only inquiries).
- **Guardrail 1:** `devotional_pipeline_v2.py` is the canonical production entrypoint; do not diverge functionality into legacy `devotional_pipeline.py`.
