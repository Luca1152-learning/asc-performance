import re
from typing import List

import requests

MAIN_LISTS_PAGE_URL = "https://top500.org/lists/top500/"


def _get_main_lists_page_content():
    main_lists_page = requests.get(MAIN_LISTS_PAGE_URL)
    return main_lists_page.text


def _get_individual_lists_links(page_content: str) -> List[str]:
    # Find "<a href="[year]/[month]">" matches while only capturing "[year]/[month]"
    year_month_pattern = r'(?<=<a href=")[0-9]{4}/[0-9]{2}(?=">)'
    matches = re.findall(year_month_pattern, page_content)

    # Append the MAIN_LISTS_PAGE_URL to all "[year]/[month]" matches to create links
    links = [MAIN_LISTS_PAGE_URL + match for match in matches]

    return links


def get_links() -> List[str]:
    return _get_individual_lists_links(_get_main_lists_page_content())
