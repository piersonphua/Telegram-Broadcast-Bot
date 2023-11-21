## Telegram Broadcast Bot

### Overview

This project involves a Telegram bot designed to broadcast messages to a large number of users. The bot interacts with a PostgreSQL database to retrieve user information and uses the `python-telegram-bot` library to send messages. The bot also features rate limiting to comply with Telegram's API limits.

### Features

- **Database Integration**: Connects to a PostgreSQL database to fetch user details.
- **Excel Upload**: Allows uploading an Excel file containing user data, which is then merged with database records.
- **Custom Rate Limiting**: Implements token bucket algorithm for rate limiting to adhere to Telegram's API usage policies.
- **Batch Processing**: Sends messages in batches to efficiently manage large volumes of outgoing messages.
- **Error Handling**: Catches and logs specific Telegram API errors and general exceptions.

### Requirements

- Google Colab
- Python 3.7
- `python-telegram-bot`
- `Flask`
- `pandas`
- `SQLAlchemy`
- `psycopg2-binary`
- `openpyxl`
- PostgreSQL Database
- Telegram Bot Token

### Configuration

- **Database Configuration**: Set your database URI in the Flask app settings or through an environment variable.
- **Rate Limiting**: Adjust the rate-limiting settings in the `MyRateLimiter` class as per your requirements.
