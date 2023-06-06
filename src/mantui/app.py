import argparse

from textual.app import App, ComposeResult
from textual.widgets import Footer, Header, MarkdownViewer

from mantui.man_to_md import (
    convert_man_to_markdown,
    get_man_page_filepath,
    is_pandoc_installed,
)


class ManPageMarkdownViewer(MarkdownViewer):
    BINDINGS = [
        ("k", "scroll_up", "Up"),
        ("j", "scroll_down", "Down"),
        ("g", "scroll_home", "Top"),
        ("ctrl+g", "scroll_end", "End"),
    ]


class Mantui(App):
    BINDINGS = [("q", "quit", "Quit")]

    def __init__(self, command: str, man_markdown: str) -> None:
        super().__init__()
        self.man_markdown = man_markdown
        self.title = f"{command} - mantui"

    def compose(self) -> ComposeResult:
        yield Header()
        yield ManPageMarkdownViewer(self.man_markdown)
        yield Footer()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="mantui",
        description="A friendly terminal user interface for Linux man pages",
    )
    parser.add_argument(
        "command", help="The command name for the man page you want to view"
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    command = args.command

    man_page_filepath = get_man_page_filepath(command)
    if not man_page_filepath:
        print("ERROR: No manual entry found for", command)
        return

    if is_pandoc_installed() is False:
        print("ERROR: pandoc not installed.")
        print("mantui uses pandoc to convert the man page files.")
        print(
            "Install pandoc using your platform's package manager.",
            "See https://pandoc.org/installing for more information.",
        )
        return

    man_markdown = convert_man_to_markdown(man_page_filepath)
    if not man_markdown:
        print("ERROR: Failed to convert man page for", command)
        return

    app = Mantui(command, man_markdown)
    app.run()
