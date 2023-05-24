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


def main() -> None:
    args = parse_args()
    command = args.command[0]

    manpath = get_man_page_filepath(command)
    if not manpath:
        print("ERROR: No manual entry found for", command)
        return

    print("Man page filepath:", manpath)


if __name__ == "__main__":
    main()
