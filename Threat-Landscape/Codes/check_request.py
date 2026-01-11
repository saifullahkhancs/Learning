import requests
import scrapy
from bs4 import BeautifulSoup  # Import BeautifulSoup for HTML parsing
# import scrapy.httpHtmlResponse
import re
import os
from urllib.parse import urljoin
from dateutil import parser
# url = "https://helpx.adobe.com/security/products/dreamweaver/apsb25-35.html"

# response= requests.get(url)

# if response.status_code == 200:
#     print("The request was successful.")
#     print("Response content:")
#     # print(response.text)
# else:
#     print(f"Failed to retrieve the page. Status code: {response.status_code}")
#     print("Response content:")
    # print(response.text)

# res = scrapy.httpHtmlResponse(url=url, body=response.text.encode('utf-8'))
# cves = response.xpath('//tbody/tr/td/p/a[contains(. ,"CVE")]/text()').getall()

# print(cves)

# import requests
# from scrapy.http import HtmlResponse # Correct import for HtmlResponse

# url = "https://helpx.adobe.com/security/products/dreamweaver/apsb25-35.html"

# # Make the request using the requests library
# response_requests = requests.get(url)

# if response_requests.status_code == 200:
#     print("The request was successful.")
#     print("Response content (first 500 chars):")
#     print(response_requests.text[:500]) # Print first 500 chars to avoid flooding console
# else:
#     print(f"Failed to retrieve the page. Status code: {response_requests.status_code}")
#     print("Response content (first 500 chars):")
#     print(response_requests.text[:1000]) # Print first 500 chars
#     # If the request failed, there's no point in trying to parse it
#     exit() # Exit the script if the request was not successful

# # Create a Scrapy HtmlResponse object from the requests library's response
# # Note: You must encode the body content to bytes for HtmlResponse
# scrapy_response = HtmlResponse(url=url, body=response_requests.text, encoding='utf-8')

# # Now, use the scrapy_response object for XPath queries
# # You had 'response.xpath' which refers to the requests object, not the scrapy one.
# cves = scrapy_response.xpath('//tbody/tr/td/p/a[contains(. ,"CVE")]/text()').getall()

# print("\nExtracted CVEs:")
# print(cves)

import requests
from scrapy.http import HtmlResponse # Correct import for HtmlResponse
import logging # Import logging for basic output
# from time import time # You had time() for timing, uncomment if needed
# from datetime import datetime # You had datetime, uncomment if needed

# Configure basic logging for visibility (optional, but good practice)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# url = "https://support.sap.com/en/my-support/knowledge-base/security-notes-news/january-2025.html"
# url = "https://www.manageengine.com/products/service-desk/cve-2024-27314.html"
url = "https://www.manageengine.com/products/service-desk/security-advisory.html"
# url = "https://support.sap.com/en/my-support/knowledge-base/security-notes-news.html"
# --- Equivalent of your spider's start_requests logic ---

# start_time = time() # Uncomment if you want to time the request
res_requests = requests.get(url) # Renamed to avoid confusion

logger.debug('Requested URL: %s', url)
# logger.info(f"Time taken to fetch the page: {round(time() - start_time, 3)}") # Uncomment if timing

if res_requests.status_code != 200:
    logger.error(f"Failed to fetch the page: {url}. Status code: {res_requests.status_code}")
    logger.error("Response content (first 500 chars):\n%s", res_requests)
    exit() # Stop execution if the page couldn't be fetched

logger.info("The request was successful. Status code: %s", res_requests.status_code)
 # Print first 500 chars to avoid flooding console

# Convert requests response to Scrapy HtmlResponse
# Use res_requests.content for bytes, and specify encoding
response = HtmlResponse(url=url, body=res_requests.content, encoding='utf-8')
# logger.info("Response content (first 500 chars):\n%s", scrapy_response.text[3000:10000])
# --- Equivalent of your spider's parse logic ---

# Accessing the response directly, no need for dummy.meta.get("response") here
# because scrapy_response is already the object we want to work with.
