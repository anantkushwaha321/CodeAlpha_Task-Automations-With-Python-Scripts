"""
Python Automation Script: Scrape the title of a fixed webpage and save it.
Key Concepts Used: requests, re (regular expressions), file handling
"""

from datetime import datetime
import html
import os
import re
import requests


def scrape_webpage_title(url: str, output_file_path: str):
    """
    Fetches the HTML of the specified URL, extracts the <title> tag using regex,
    and saves the extracted title to a text file.
    """
    print("=" * 60)
    print(" Scrape title of a fixed webpage")
    print("=" * 60)
    print(f"Target URL : {url}")
    print(f"Output File: {os.path.abspath(output_file_path)}\n")

    # Step 1: Send HTTP GET request using 'requests'
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/124.0.0.0 Safari/537.36"
        )
    }

    try:
        print("[HTTP] Sending GET request...")
        response = requests.get(url, headers=headers, timeout=10)
        # Raise an exception for HTTP error codes (4xx, 5xx)
        response.raise_for_status()
        print(f"[HTTP] Response received with status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"[ERROR] Failed to fetch webpage: {e}")
        return

    # Step 2: Extract the <title> tag using regular expressions (re)
    html_content = response.text
    title_pattern = r"<title(?:\s+[^>]*)?>(.*?)</title>"
    match = re.search(title_pattern, html_content, re.IGNORECASE | re.DOTALL)

    if not match:
        print("[WARNING] Could not find a <title> tag in the webpage HTML.")
        page_title = "No title found"
    else:
        # Clean title: unescape HTML entities (&amp;, &#39;, etc.) and strip extra whitespace
        raw_title = match.group(1).strip()
        page_title = html.unescape(re.sub(r"\s+", " ", raw_title))
        print(f"[EXTRACTED] Page Title: '{page_title}'")

    # Step 3: Save title to file using file handling
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    file_content = (
        f"Webpage Title Scraping Result\n"
        f"{'=' * 40}\n"
        f"URL Scraped   : {url}\n"
        f"Date & Time   : {timestamp}\n"
        f"HTTP Status   : {response.status_code}\n"
        f"Page Title    : {page_title}\n"
        f"{'=' * 40}\n"
    )

    try:
        output_dir = os.path.dirname(output_file_path)
        if output_dir:
            os.makedirs(output_dir, exist_ok=True)

        with open(output_file_path, "w", encoding="utf-8") as f:
            f.write(file_content)

        print("\n" + "-" * 60)
        print(f"[SUCCESS] Webpage title saved to '{output_file_path}'.")
        print("-" * 60)

    except Exception as e:
        print(f"[ERROR] Failed to write title to file: {e}")


if __name__ == "__main__":
    TARGET_URL = "https://example.com"
    OUTPUT_FILE = "webpage_title.txt"

    scrape_webpage_title(TARGET_URL, OUTPUT_FILE)
