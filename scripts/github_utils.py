#!/usr/bin/env python3
"""Shared GitHub helpers for skill install scripts."""

from __future__ import annotations

import os
import subprocess
import urllib.request
from urllib.error import URLError


def _headers(user_agent: str) -> dict[str, str]:
    headers = {"User-Agent": user_agent}
    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    if token:
        headers["Authorization"] = f"token {token}"
    return headers


def _curl_request(url: str, headers: dict[str, str]) -> bytes:
    cmd = ["curl", "-fsSL"]
    for name, value in headers.items():
        cmd.extend(["-H", f"{name}: {value}"])
    cmd.append(url)
    result = subprocess.run(cmd, check=True, capture_output=True)
    return result.stdout


def github_request(url: str, user_agent: str) -> bytes:
    headers = _headers(user_agent)
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req) as resp:
            return resp.read()
    except URLError:
        # Python SSL trust stores are brittle on some local macOS setups.
        return _curl_request(url, headers)


def github_api_contents_url(repo: str, path: str, ref: str) -> str:
    return f"https://api.github.com/repos/{repo}/contents/{path}?ref={ref}"
