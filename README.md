# Basic Random Cat Gifs Discord Bot

A simple Discord bot that responds to mentions with commands such as sending random cat GIFs or greeting users. This bot uses [The Cat API](https://thecatapi.com/) to fetch adorable cat GIFs and integrates with Discord using the `discord.py` library.

---

## Features

- Responds with a friendly greeting when the bot is mentioned with `Hello`.
- Fetches and sends a random cat GIF when the bot is mentioned with the `catgifs` command.
- Handles unrecognized commands gracefully.

---

## Prerequisites

1. **Python**: Ensure you have Python 3.8+ installed.
2. **Discord Bot Token**: Create a bot on the [Discord Developer Portal](https://discord.com/developers/applications) and get your token.
3. **The Cat API Key**: Sign up at [The Cat API](https://thecatapi.com/) and get your API key.

---

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/NotSwanand/Basic-Random-Cat-Gifs-Discord-Bot.git
   cd Basic-Random-Cat-Gifs-Discord-Bot
   
2. Install the required dependencies:

```
pip install discord.py requests
```

3. Add your API keys:

Replace 'your_key' in the client.run() method with your Discord bot token.
Replace 'your_cat_api' in the headers with your Cat API key.
