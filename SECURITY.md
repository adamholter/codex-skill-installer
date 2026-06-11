# Security Notes

`codex-skill-installer` is intended to stay easy to audit.

Current guardrails:

- no embedded API keys, OAuth tokens, cookies, or local session files
- optional GitHub auth only through existing `GH_TOKEN` or `GITHUB_TOKEN` environment variables
- destination installs are blocked when the target skill directory already exists
- selected repo paths must stay inside the source repository

Before publishing updates, scan for:

- local home-directory paths
- copied private skill content
- checked-in temporary install output
- real token values in examples or shell transcripts
