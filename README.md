# Install Codex Skills Straight From GitHub

`codex-skill-installer` is a small utility for listing Codex-installable skills and copying them into `$CODEX_HOME/skills` without manual repo cloning.

It supports:

- listing curated skills from GitHub
- installing a skill from an `owner/repo` plus path
- installing from a full GitHub URL
- public repos via direct download
- private repos or auth-required repos via sparse checkout fallback

![Preview](assets/preview.svg)

## Why This Exists

Most shareable Codex skills live inside bigger repos. Copying them by hand is tedious, and private repos are worse. This tool gives you a predictable install path with a couple of commands.

It is also packaged as a Codex skill, so you can drop this repo into your own skill collection or adapt the scripts directly.

## Quick Start

List curated skills:

```bash
python3 scripts/list-skills.py
```

Install from a repo path:

```bash
python3 scripts/install-skill-from-github.py \
  --repo openai/skills \
  --path skills/.curated/aspnet-core
```

Install from a full GitHub URL:

```bash
python3 scripts/install-skill-from-github.py \
  --url https://github.com/openai/skills/tree/main/skills/.curated/aspnet-core
```

Install into a custom directory:

```bash
python3 scripts/install-skill-from-github.py \
  --repo openai/skills \
  --path skills/.curated/aspnet-core \
  --dest ./sandbox-skills
```

## Requirements

- Python 3
- `git`
- `curl`

`curl` is used as a practical fallback when local Python SSL certificate chains are broken, which happens on some macOS setups.

## Behavior

- installs into `$CODEX_HOME/skills` by default
- uses `~/.codex` when `CODEX_HOME` is not set
- fails fast if the destination skill already exists
- validates that skill paths stay inside the source repo
- accepts `GITHUB_TOKEN` or `GH_TOKEN` for private repo access
- falls back from archive download to sparse checkout when needed

## Smoke-Tested Examples

The scripts were verified on `2026-05-20` with:

```bash
python3 scripts/list-skills.py
python3 scripts/install-skill-from-github.py \
  --repo openai/skills \
  --path skills/.curated/aspnet-core \
  --dest "$(mktemp -d)"
python3 scripts/install-skill-from-github.py \
  --url https://github.com/openai/skills/tree/main/skills/.curated/aspnet-core \
  --dest "$(mktemp -d)"
```

## Repo Layout

- `scripts/list-skills.py`: list installable skills from a GitHub repo path
- `scripts/install-skill-from-github.py`: install one or more skills into a Codex skills directory
- `scripts/github_utils.py`: shared GitHub request helpers
- `SKILL.md`: Codex skill wrapper for using the installer inside Codex

## Notes

This repo is a cleaned public extraction of a working local Codex skill. Personal machine paths, account-specific state, tokens, and private notes are not included.
