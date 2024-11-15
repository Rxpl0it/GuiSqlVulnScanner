import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
import re

# Define common MySQL error patterns
MYSQL_ERROR_PATTERNS = [
    "You have an error in your SQL syntax;",
    "Warning: mysql_",
    "Unclosed quotation mark after the character string",
    "quoted string not properly terminated"
]

def start_scan(urls, counter, graph, error_logger):
    with ThreadPoolExecutor(max_workers=10) as executor:
        future_to_url = {executor.submit(test_sql_injection, url, counter, graph, error_logger): url for url in urls}
        for future in as_completed(future_to_url):
            url = future_to_url[future]
            try:
                future.result()
            except Exception as e:
                error_logger.log(f"Error scanning {url}: {str(e)}")

def test_sql_injection(url, counter, graph, error_logger):
    payload = "'123"
    try:
        response = requests.get(url, params={"id": payload}, timeout=5)
        if detect_mysql_errors(response.text):
            counter.increment()
            graph.update(counter.get_count())
            error_logger.log(f"Vulnerability found at {url} with payload {payload}")
    except requests.RequestException as e:
        error_logger.log(f"Request failed for {url}: {str(e)}")

def detect_mysql_errors(response_text):
    for pattern in MYSQL_ERROR_PATTERNS:
        if re.search(pattern, response_text, re.IGNORECASE):
            return True
    return False
