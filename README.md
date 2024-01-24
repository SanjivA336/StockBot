# Stock Bot
A discord bot that displays real-time data on the stock and cryptocurrency market.

## Add The Bot
[Add Stock Bot to your server](https://discord.com/api/oauth2/authorize?client_id=775537511401127996&permissions=116736&scope=bot)

## Controlling The Bot

### Bot Prefix:
    s!

### Available Commands
- Stocks (`stocks`, `stock`, `markets`, `market`, `nyse`): Find stock information based on its ticker.

        s!stocks {ticker} {timeframe} {period}
  * Parameters:
    * `ticker`: The stock's ticker.
    * `timeframe`: How many days of data should be displayed. Defaults to one day (`1`).
    * `period`: The interval between each data point. Defaults to one day (`1d`)

- Cryptocurrencies (`crypto`, `digital`, `cryptos`, `cryptocurrency`, `cryptocurrencies`): Find crypto information based on its ticker.

        s!crypto {ticker} {timeframe} {period}
  * Parameters:
    * `ticker`: The crypto's ticker.
    * `timeframe`: How many days of data should be displayed. Defaults to one day (`1`).
    * `period`: The interval between each data point. Defaults to one day (`1d`)
  
- Reminder (`remind`, `remindme`, `timer`): An alert that will go off after a specified amount of time.
  
        v!remind {time} {message}
  * Parameters:
    * `time`: How long the bot should wait before reminding you. Defaults to 5 minutes (`5m`). *Use s, m, h, and d for seconds, minutes, hours, and days*
    * `message`: What the bot should remind you about. Defaults to "Here's your reminder!" (`Here's your reminder`).
- Ping (`ping`): Checks the bot's ping.
  
        v!ping
