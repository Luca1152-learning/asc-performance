from src.asc_performance.scripts.get_data import get_data
from src.asc_performance.scripts.get_improvement import get_average_improvement
from src.asc_performance.scripts.get_urls import get_urls
from src.asc_performance.scripts.graph import show_graph

urls = get_urls()
data = get_data(urls)
show_graph(data)
average = get_average_improvement(data)
