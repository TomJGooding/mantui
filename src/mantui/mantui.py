import argparse
import subprocess


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "command",
        help="The command man page to view",
        nargs=1,
    )
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


def get_nroff_content(man_page_filepath: str) -> str:
    result: str = ""
    try:
        out_bytes = subprocess.check_output(
            ["zcat", man_page_filepath],
            stderr=subprocess.STDOUT,
        )
    except subprocess.CalledProcessError:
        pass
    else:
        out_text = out_bytes.decode("utf-8")
        result = out_text.strip("\n")

    return result


def main() -> None:
    args = parse_args()
    command = args.command[0]

    man_page_filepath = get_man_page_filepath(command)
    if not man_page_filepath:
        print("ERROR: No manual entry found for", command)
        return

    nroff_content = get_nroff_content(man_page_filepath)
    print(nroff_content)


if __name__ == "__main__":
    main()
