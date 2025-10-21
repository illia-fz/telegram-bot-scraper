#!/usr/bin/env python3
"""
telegram-bot-scraper
This script fetches new Telegram bot listings from a public aggregator site and prints them.
"""

import requests
from bs4 import BeautifulSoup


def fetch_new_bots(url="https://botostore.com/new/"):
    """Fetches new Telegram bot names and links from the specified URL.

    Args:
        url (str): URL of the bot listing page.

    Returns:
        list of tuple: List of (bot_name, bot_url) pairs.
    """
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")

    bots = []
    # Example: parse all links with class "bot-card"
    for link in soup.find_all("a", class_="bot-card"):
        name = link.get_text(strip=True)
        href = link.get("href", "")
        # If href is relative, prefix with base domain
        if href.startswith("/"):
            base = "https://botostore.com"
            href = base + href
        bots.append((name, href))
    return bots


def main():
    bots = fetch_new_bots()
    print("Latest Telegram bots:")
    for name, url in bots:
        print(f"{name} - {url}")


if __name__ == "__main__":
    main()
