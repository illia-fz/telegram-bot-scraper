# telegram-bot-scraper

Tool to automatically parse new Telegram bot listings and track their releases.

## Features

- Fetches the latest Telegram bot listings from an aggregator website (e.g. Botostore).
- Extracts bot names and links and prints them to stdout.
- Easily extensible to parse additional pages or output formats.

## Requirements

- Python 3.8+
- See `requirements.txt` for Python package dependencies (`requests`, `beautifulsoup4`).

## Setup

It’s recommended to create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Usage

Run the scraper script from your terminal:

```bash
python scraper.py
```

It will fetch the latest bots and print each bot name along with a link to the bot details page.

## Configuration

By default the script scrapes `https://botostore.com/new/`. You can pass a different URL as an argument to the `fetch_new_bots` function in `scraper.py`.

## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request with improvements, bug fixes or new features.

1. Fork this repository.
2. Create a feature branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -am 'feat: add new feature'`).
4. Push to your branch (`git push origin feature/your-feature`).
5. Open a new Pull Request and describe your changes.
