# Discord Typing Test Bot

A simple Discord bot that provides typing tests for users. The bot measures how quickly users can type a given sentence and calculates their typing speed in words per minute (WPM).

## Features

- Provides random sentences for typing tests.
- Measures the time taken to type the sentence.
- Calculates and displays the typing speed in words per minute (WPM).

## Prerequisites

- Python 3.12 or higher

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/discord-typing-test-bot.git
   cd discord-typing-test-bot
   ```

2. **Install the required libraries:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your bot on the Discord Developer Portal:**
   - Go to the [Discord Developer Portal](https://discord.com/developers/applications).
   - Create a new application.
   - Create a bot user for your application.
   - Copy the bot token.
   - Invite the bot to your server using the OAuth2 URL generator.

4. **Configure your bot:**
   - Create a file named `.env` in the project directory.
   - Add your bot token to the `.env` file:

    ```bash
    DISCORD_TOKEN=YOUR_BOT_TOKEN
    ```
