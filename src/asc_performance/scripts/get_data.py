from typing import List, Tuple

import requests
from bs4 import BeautifulSoup


def _get_year_performance_data(url: str) -> float:
    # Get the page's BeautifulSoup instance
    page_content = requests.get(url).content
    soup = BeautifulSoup(page_content, "html.parser")

    rmax_list = []
    rmax_unit_of_measurement = ""

    # Iterate through the first 4 rows of the table with performance data
    data_table = soup.find('table', {'class': 'table table-condensed table-striped'})

    # The "November 1995" page shows the message "Page not found!"
    if not data_table:
        raise ValueError(f"Couldn't parse the {url} url.")

    for index, table_row in enumerate(data_table.find_all("tr")[:4]):
        # Get the unit of measurement for Rmax
        if index == 0:
            rmax_unit_of_measurement = table_row.find_all("th")[3].text
        # Get the Rmax value
        else:
            rmax_list.append(float(table_row.find_all("td")[3].text.replace(",", "")))

    top_3_rmax_average = sum(rmax_list) / len(rmax_list)

    # Convert the top 3 Rmax average from GFlop/s to TFlop/s
    if "GFlop/s" in rmax_unit_of_measurement:
        top_3_rmax_average /= 1000

    return top_3_rmax_average


def get_data(urls: List[str]) -> List[Tuple[str, float]]:
    performance_data = []
    for url in urls:
        try:
            year_average = _get_year_performance_data(url)
            performance_data.append((url[-7:], year_average))
        except ValueError:
            pass
    return performance_data
