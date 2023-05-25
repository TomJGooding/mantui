import argparse
import subprocess


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("command", help="The command man page to view")
    return parser.parse_args()


def get_man_page_filepath(command: str) -> str:
    result: str = ""
    try:
        out_bytes = subprocess.check_output(
            ["man", "-w", command],
            stderr=subprocess.STDOUT,
        )
    except subprocess.CalledProcessError:
        pass
    else:
        out_text = out_bytes.decode("utf-8")
        result = out_text.strip("\n")

    return result


def is_pandoc_installed() -> bool:
    result: bool = False
    try:
        subprocess.check_output(["pandoc", "--version"])
    except FileNotFoundError:
        pass
    except subprocess.CalledProcessError:
        pass
    else:
        result = True

    return result


def convert_man_to_markdown(man_page_filepath: str) -> str:
    result: str = ""
    try:
        zcat = subprocess.Popen(
            ["zcat", man_page_filepath],
            stdout=subprocess.PIPE,
        )
        pandoc_out = subprocess.check_output(
            ["pandoc", "--from", "man", "--to", "commonmark"], stdin=zcat.stdout
        )
    except FileNotFoundError:
        pass
    except subprocess.CalledProcessError:
        pass
    else:
        result = pandoc_out.decode("utf-8")

    return result


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

    print(man_markdown)


if __name__ == "__main__":
    main()
