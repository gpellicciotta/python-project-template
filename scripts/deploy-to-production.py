#!/usr/bin/env python3
"""Example production-deployment script, scaffolded for projects derived from this template that
deploy a running service (as opposed to a library published only to a package index).

This template itself has no deployment target, so `deploy` only validates preconditions (clean
git tree, passing build) and then reports what it *would* do. Replace the marked section in
`deploy()` with the project's actual deployment mechanism (container push, SSH rsync + restart,
cloud CLI invocation, ...) - keep the precondition checks and dry-run support as-is.

Cross-platform (Windows/Linux/macOS) - only calls the venv's own python executable and git.

Usage:
  python scripts/deploy-to-production.py deploy [--dry-run]
  python scripts/deploy-to-production.py --version
"""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

from _cli_common import build_action_parser, print_help, print_version

PROG = "deploy-to-production"
DESCRIPTION = "Validates preconditions and deploys the built project to its production target."
EXIT_CODES = [(0, "Success"), (1, "Preconditions not met or deployment failed")]
REPO_ROOT = Path(__file__).resolve().parent.parent


def get_project_version() -> str:
    """Resolves the current project version from pyproject.toml."""
    pyproject = REPO_ROOT / "pyproject.toml"
    if pyproject.exists():
        content = pyproject.read_text(encoding="utf-8")
        match = re.search(r'^version\s*=\s*"([^"]+)"', content, re.MULTILINE)
        if match:
            return match.group(1).strip()
    return "0.0.0+unknown"


def check_clean_git_tree() -> bool:
    """Returns whether the working tree has no uncommitted changes."""
    result = subprocess.run(["git", "status", "--porcelain"], cwd=str(REPO_ROOT), check=False, capture_output=True, text=True)
    if result.stdout.strip():
        print("[!] Working tree has uncommitted changes - commit or stash before deploying.")
        return False
    return True


def check_not_pre_release(version: str) -> bool:
    """Returns whether the current version is a finalized release, not an in-development '-pre'."""
    if version.endswith("-pre"):
        print(f"[!] Version '{version}' is still in development ('-pre') - finalize the release first.")
        return False
    return True


def deploy(version: str, dry_run: bool) -> int:
    if not check_clean_git_tree():
        return 1
    if not check_not_pre_release(version):
        return 1

    print(f"\n[*] Deploying version {version} to production", flush=True)
    if dry_run:
        print("[dry-run] Skipping actual deployment step.")
        return 0

    # Project-specific deployment goes here, e.g. build+push a container image, rsync artifacts
    # to the target host and restart the service, or invoke a cloud provider's deploy CLI.
    print("[!] No production deployment target is configured for this template - nothing done.")
    print("    Replace this section in deploy() with the project's actual deployment mechanism.")
    return 1


def main() -> int:
    version = get_project_version()
    parser = build_action_parser(PROG, DESCRIPTION, ["deploy", "version", "help"], "deploy")
    parser.add_argument("--dry-run", action="store_true", help="Validate preconditions without deploying")
    args = parser.parse_args()

    if args.version or args.action == "version":
        print_version(PROG, version)
        return 0
    if args.help or args.action == "help":
        print_help(PROG, version, DESCRIPTION, parser, EXIT_CODES)
        return 0

    return deploy(version, args.dry_run)


if __name__ == "__main__":
    sys.exit(main())
