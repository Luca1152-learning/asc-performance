from typing import List, Tuple


def get_average_improvement(data: List[Tuple[str, float]]) -> float:
    improvements_per_year = []
    for index, performance_data in enumerate(data[:-1]):
        # Current year's data
        current_year_month_str, current_rmax = performance_data
        current_year, current_month = (int(number) for number in current_year_month_str.split("/"))

        # Previous year's data
        previous_year_month_str, previous_rmax = data[index + 1]
        previous_year, previous_month = (int(number) for number in previous_year_month_str.split("/"))

        # Calculate what percent is the current_rmax out of previous_rmax
        percentage_difference = current_rmax / previous_rmax * 100 - 100

        # Find the average percentage of performance improvement per year
        elapsed_months = (current_year - previous_year) * 12 + current_month - previous_month
        improvement_per_year = (percentage_difference / elapsed_months) * 12
        improvements_per_year.append(improvement_per_year)

    average_percentage_per_year = sum(improvements_per_year) / len(improvements_per_year)
    return average_percentage_per_year
