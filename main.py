def main():
    import argparse

    argument_parser = argparse.ArgumentParser(description="DSA Calculator")
    argument_parser.add_argument(
        "--cli",
        action="store_true",
        help="launch the command-line calculator",
    )
    arguments = argument_parser.parse_args()

    if arguments.cli:
        from ui.cli import main as run_cli

        run_cli()
    else:
        from ui.gui import run as run_gui

        run_gui()


if __name__ == '__main__':
    main()