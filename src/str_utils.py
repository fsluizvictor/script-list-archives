import re
import config

from typing import List


def find_regex(text: str, regex: str) -> bool:
    return bool(re.search(regex, text))


def apply_regex(text: str) -> str:
    return re.sub(config.REGEX_FARMS_ID, '/farm_id/', text)
