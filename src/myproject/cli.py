import argparse
import sys

from . import __version__
from .core import greet
from .scaffold import ScaffoldError, create_project


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="myproject", description="Sample CLI for python-template-project.")
    parser.add_argument("--version", action="version", version=f"%(prog)s {__version__}")

    subparsers = parser.add_subparsers(dest="command")

    subparsers.add_parser("help", help="Show usage info")
    subparsers.add_parser("version", help="Show the current version")

    greet_parser = subparsers.add_parser("greet", help="Print a greeting (sample business logic)")
    greet_parser.add_argument("name", nargs="?", default="wereld", help="Name to greet")

    create_parser = subparsers.add_parser("create", help="Create a new project as a renamed copy of this template")
    create_parser.add_argument("project_name", help="Name for the new project (used for its directory and package name)")
    create_parser.add_argument(
        "-o", "--output-dir", default=".", help="Directory to create the new project under (default: current directory)"
    )

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.command in (None, "help"):
        parser.print_help()
        return 0

    if args.command == "version":
        print(__version__)
        return 0

    if args.command == "greet":
        print(greet(args.name))
        return 0

    if args.command == "create":
        try:
            destination = create_project(args.project_name, args.output_dir)
        except ScaffoldError as exc:
            print(f"error: {exc}", file=sys.stderr)
            return 1
        print(f"Created new project at {destination}")
        return 0

    parser.print_help()
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
