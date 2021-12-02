import re
import config

from typing import List


def apply_regex(text: List[str], regex_1: str, regex_2: str) -> List[List[str]]:
    return [regex(element) for element in text]


def find_regex(text: str, regex: str = config.HAS_SQL) -> bool:
    return bool(re.search(regex, text))


def regex(text: str):
    return re.sub(config.REGEX_FARMS_ID, '/farm_id/', text)
