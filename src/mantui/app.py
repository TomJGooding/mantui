import argparse

from textual.app import App, ComposeResult
from textual.widgets import MarkdownViewer

from mantui.man_to_md import (
    convert_man_to_markdown,
    get_man_page_filepath,
    is_pandoc_installed,
)


class Mantui(App):
    def __init__(self, man_markdown: str) -> None:
        super().__init__()
        self.man_markdown = man_markdown

    def compose(self) -> ComposeResult:
        yield MarkdownViewer(self.man_markdown, show_table_of_contents=True)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="mantui",
        description="A friendly terminal user interface for Linux man pages",
    )
    parser.add_argument("command", help="The command man page to view")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    command = args.command

    man_page_filepath = get_man_page_filepath(command)
    if not man_page_filepath:
        print("ERROR: No manual entry found for", command)
        return

    if is_pandoc_installed() is False:
        print(
            "ERROR: pandoc not installed.",
            "See https://pandoc.org/installing.html",
        )
        return

    man_markdown = convert_man_to_markdown(man_page_filepath)
    if not man_markdown:
        print("ERROR: Failed to convert man page for", command)
        return

    app = Mantui(man_markdown)
    app.run()


if __name__ == "__main__":
    main()
