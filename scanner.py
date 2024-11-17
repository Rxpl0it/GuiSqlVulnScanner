import aiohttp
import asyncio
import re

# Define common MySQL error patterns
MYSQL_ERROR_PATTERNS = [
    "You have an error in your SQL syntax;",
    "Warning: mysql_",
    "Unclosed quotation mark after the character string",
    "quoted string not properly terminated"
]

async def start_scan(urls, counter, graph, error_logger):
    async with aiohttp.ClientSession() as session:
        tasks = [test_sql_injection(session, url, counter, graph, error_logger) for url in urls]
        await asyncio.gather(*tasks)

async def test_sql_injection(session, url, counter, graph, error_logger):
    payload = "'123"
    try:
        async with session.get(url, params={"id": payload}, timeout=5) as response:
            text = await response.text()
            if detect_mysql_errors(text):
                counter.increment()
                graph.update(counter.get_count())
                error_logger.log(f"Vulnerability found at {url} with payload {payload}")
    except aiohttp.ClientError as e:
        error_logger.log(f"Request failed for {url}: {str(e)}")

def detect_mysql_errors(response_text):
    for pattern in MYSQL_ERROR_PATTERNS:
        if re.search(pattern, response_text, re.IGNORECASE):
            return True
    return False
