## 2026-05-20

- Added a resilient GitHub request fallback that retries with `curl` when Python's local SSL trust chain fails on macOS.
- Shareability: improves out-of-the-box behavior on real developer machines without requiring manual certificate fixes.
- Security/privacy: keeps GitHub auth optional through existing `GITHUB_TOKEN` or `GH_TOKEN` env vars and does not embed any personal credentials.
