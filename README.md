## Telegram Broadcast Bot

### Overview

This project involves a Telegram bot designed to broadcast messages to a large number of users. The bot interacts with a PostgreSQL database to retrieve user information and uses the `python-telegram-bot` library to send messages. The bot also features rate limiting to comply with Telegram's API limits.

<p float="center">
<img src="https://github.com/piersonphua/Telegram-Broadcast-Bot/blob/main/images/broadcast_bot.png?raw=true" width=100% height=100%>
<center>
  <img src="https://github.com/piersonphua/Telegram-Broadcast-Bot/blob/main/images/IMG_9F6DBC0D0385-1.jpeg?raw=true" width=30% height=30%>
</center>
</p>


### Features

- **Database Integration**: Connects to a PostgreSQL database to fetch user details.
- **Targetted Broadcasts**: Allows uploading a custom Excel file containing intended recipients, which is then merged with database records.
- **Personalised Messages**: Allows personalised messages for each user by using placeholders for headers of the excel file
- **Feedback**: Link to external form for feedback
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
