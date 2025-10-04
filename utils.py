import logging
import re

logging.basicConfig(
    filename="errors.log",
    level=logging.ERROR,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)


def safe_run(func, *args, **kwargs):
    try:
        return func(*args, **kwargs)
    except FileNotFoundError as e:
        logging.error(f"File not found: {e}")
        print(f"[FileNotFoundError] {e}")
    except ValueError as e:
        logging.error(f"Value error: {e}")
        print(f"[ValueError] {e}")
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        print(f"[Unexpected error] {e}")
    return None


def clean_job_offer_text(raw_text: str) -> str:
    raw_text = re.sub(r"\n\s*\n+", "\n\n", raw_text)

    unwanted = [
        "Polityka prywatności",
        "Regulamin",
        "©",
        "Cookies",
        "Zgłoś ofertę",
        "Aplikuj teraz"
    ]
    for phrase in unwanted:
        raw_text = raw_text.replace(phrase, "")

    lines = [line.strip()
             for line in raw_text.splitlines() if len(line.strip()) > 2]

    return "\n".join(lines)
