from typing import Literal

import requests
from bs4 import BeautifulSoup


def google_translate(
    text: str,
    source: Literal["auto", "en", "ko"],
    target: Literal["en", "ko"],
):
    text = text.strip()
    if not text:
        return ""

    endpoint_url = "https://translate.google.com/m"

    params = {
        "hl": source,
        "sl": source,
        "tl": target,
        "q": text,
        "ie": "UTF-8",
        "prev": "_m",
    }

    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 "
            "(KHTML, like Gecko) Chrome/86.0.4240.183 Mobile Safari/537.36"
        ),
    }

    res = requests.get(
        endpoint_url,
        params=params,
        headers=headers,
        timeout=5,
    )
    res.raise_for_status()

    soup = BeautifulSoup(res.text, "html.parser")
    translated_text = soup.select_one(".result-container").text.strip()

    return translated_text
