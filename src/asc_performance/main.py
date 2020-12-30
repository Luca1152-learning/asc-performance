from src.asc_performance.scripts.get_data import get_data
from src.asc_performance.scripts.get_improvement import get_average_improvement
from src.asc_performance.scripts.get_urls import get_urls

urls = get_urls()
data = get_data(urls)
average = get_average_improvement(data)
