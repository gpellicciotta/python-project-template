from __future__ import annotations

import argparse
import sys

from . import __version__
from .core import greet
from .scaffold import ScaffoldError, create_project

TOOL_NAME = "myproject"
COPYRIGHT = "Copyright (c) 2026 Giovanni Pellicciotta"
DESCRIPTION = "Sample CLI for python-template-project providing greeting and project scaffolding."

SHORT_USAGE = "myproject [help|version|greet|create] [args] [options]"

LONG_USAGE = """myproject [help|version|greet|create] [args] [options]

Actions:
    help                             show this help message and exit
    version                          show version information and exit
    greet [NAME]                     print a greeting (sample business logic)
    create PROJECT_NAME [-o DIR]     create a new project as a renamed copy of this template

Options:
    -h, --help                       show this help message and exit
    --version                        show version information and exit
    --verbose                        show detailed usage and execution info
    -o, --output-dir DIR             destination directory for create (default: .)"""

SHORT_EXIT_CODES = """Exit codes:
    0  success
    1  application or command execution error
    2  invalid command-line arguments"""


def version_text() -> str:
    """Return single-line formatted version string per development guidelines."""
    return f"{TOOL_NAME} v{__version__} - {COPYRIGHT}"


def print_help(verbose: bool = False) -> None:
    """Print formatted multi-line help message per development guidelines."""
    print(version_text())
    print()
    print(DESCRIPTION)
    print()
    if verbose:
        print(LONG_USAGE)
        print()
        print(SHORT_EXIT_CODES)
    else:
        print(f"Usage: {SHORT_USAGE}\n\n{SHORT_EXIT_CODES}\n\nRun with --verbose for full option details.")


def build_parser() -> argparse.ArgumentParser:
    """Build the argument parser for CLI actions and options."""
    parser = argparse.ArgumentParser(
        prog=TOOL_NAME,
        description=DESCRIPTION,
        add_help=False,
    )
    parser.add_argument("-h", "--help", action="store_true", help="Show this help message and exit")
    parser.add_argument("--version", action="store_true", help="Show version information and exit")
    parser.add_argument("--verbose", action="store_true", help="Show detailed usage or execution info")

    subparsers = parser.add_subparsers(dest="command")

    help_parser = subparsers.add_parser("help", add_help=False, help="Show usage info")
    help_parser.add_argument("-h", "--help", action="store_true", help=argparse.SUPPRESS)
    help_parser.add_argument("--verbose", action="store_true", help=argparse.SUPPRESS)

    version_parser = subparsers.add_parser("version", add_help=False, help="Show version information")
    version_parser.add_argument("-h", "--help", action="store_true", help=argparse.SUPPRESS)

    greet_parser = subparsers.add_parser("greet", add_help=False, help="Print a greeting (sample business logic)")
    greet_parser.add_argument("name", nargs="?", default="wereld", help="Name to greet")
    greet_parser.add_argument("-h", "--help", action="store_true", help=argparse.SUPPRESS)
    greet_parser.add_argument("--verbose", action="store_true", help="Show verbose greeting")

    create_parser = subparsers.add_parser("create", add_help=False, help="Create a new project as a renamed copy of this template")
    create_parser.add_argument("project_name", nargs="?", default=None, help="Name for the new project")
    create_parser.add_argument(
        "-o", "--output-dir", default=".", help="Directory to create the new project under (default: current directory)"
    )
    create_parser.add_argument("-h", "--help", action="store_true", help=argparse.SUPPRESS)
    create_parser.add_argument("--verbose", action="store_true", help="Show verbose output during creation")

    return parser


def main(argv: list[str] | None = None) -> int:
    """Entry point for the CLI."""
    parser = build_parser()
    try:
        args = parser.parse_args(argv)
    except SystemExit as exc:
        return int(exc.code) if isinstance(exc.code, int) else 2

    # Check top-level flags or subcommands requesting version first
    if getattr(args, "version", False) or args.command == "version":
        print(version_text())
        return 0

    # Check top-level flags or subcommands requesting help
    if getattr(args, "help", False) or args.command in (None, "help"):
        print_help(verbose=getattr(args, "verbose", False))
        return 0

    if args.command == "greet":
        if getattr(args, "verbose", False):
            print(f"Greeting target: {args.name}")
        print(greet(args.name))
        return 0

    if args.command == "create":
        if not args.project_name:
            print("error: project_name is required for create action", file=sys.stderr)
            return 2
        if getattr(args, "verbose", False):
            print(f"Scaffolding project '{args.project_name}' into '{args.output_dir}'...")
        try:
            destination = create_project(args.project_name, args.output_dir)
        except ScaffoldError as exc:
            print(f"error: {exc}", file=sys.stderr)
            return 1
        print(f"Created new project at {destination}")
        return 0

    print_help()
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
