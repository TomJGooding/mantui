import subprocess


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
