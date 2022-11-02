import discord
from discord.ext import commands
import yfinance as yf
import pandas as pd
import datetime
import plotly.graph_objects as go
from asyncio import sleep as s


bot = commands.Bot(command_prefix = 's!')
bot.remove_command('help')


#Alerts you when the bot is ready to take in commands
@bot.event
async def on_ready():
    print('Opening the Market!')
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Yahoo Finance"))

#Checks the ping of the bot
@bot.command()
async def ping(ctx):
    await ctx.send(f'Pong! My ping is {round(bot.latency*1000)}ms')

#Find stock information based on ticker
@bot.command(aliases=['stocks', 'market', 'markets', 'nyse'])
async def stock(ctx, ticker, timeframe=1, period="1d"):
    today = datetime.date.today()
    data = yf.Ticker(ticker)
    days = datetime.timedelta(timeframe)
    start = today - days
    df = data.history(period=period, start=start, end=today)

    fig = go.Figure(data=[go.Candlestick(x=df.index, open=df['Open'], high=df['High'], low=df['Low'], close=df['Close'])])
    fig.write_image("output.png")


    if(timeframe == 1):
        embed = discord.Embed(title=f"Stock information for {ticker.upper()}",description=f"Timeframe: {timeframe} day",color=discord.Color.blue())

        embed.add_field(name="Open: ",value=f"${round(df['Open'].mean(), 2)}",inline=True)
        embed.add_field(name="High: ",value=f"${round(df['High'].mean(), 2)}",inline=True)
        embed.add_field(name="Low: ",value=f"${round(df['Low'].mean(), 2)}",inline=True)
        embed.add_field(name="Close: ",value=f"${round(df['Close'].mean(), 2)}",inline=True)
    else:
        embed = discord.Embed(title=f"Stock information for {ticker.upper()}",description=f"Timeframe: {timeframe} days",color=discord.Color.blue())

        open = df.describe()["Open"]
        high = df.describe()["High"]
        low = df.describe()["Low"]
        close = df.describe()["Close"]

        embed.add_field(name="Open: ",value=f"Mean: ${round(open[1], 2)}\nHigh: ${round(open[7], 2)}\nLow: ${round(open[3], 2)}",inline=False)
        embed.add_field(name="High: ",value=f"Mean: ${round(high[1], 2)}\nHigh: ${round(high[7], 2)}\nLow: ${round(high[3], 2)}",inline=False)
        embed.add_field(name="Low: ",value=f"Mean: ${round(low[1], 2)}\nHigh: ${round(low[7], 2)}\nLow: ${round(low[3], 2)}",inline=False)
        embed.add_field(name="Close: ",value=f"Mean: ${round(close[1], 2)}\nHigh: ${round(close[7], 2)}\nLow: ${round(close[3], 2)}",inline=False)

    await ctx.send(embed=embed)
    await ctx.send("Here's a candlestick chart to go along with that data:")
    await ctx.send(file=discord.File('output.png'))

#Find stock information based on ticker
@bot.command(aliases=['digital', 'cryptos', 'cryptocurrency', 'cryptocurrencies'])
async def crypto(ctx, ticker, timeframe=1, period="1d"):
    ticker = ticker + "-USD"
    today = datetime.date.today()
    data = yf.Ticker(ticker)
    days = datetime.timedelta(timeframe)
    start = today - days
    df = data.history(period=period, start=start, end=today)

    fig = go.Figure(data=[go.Candlestick(x=df.index, open=df['Open'], high=df['High'], low=df['Low'], close=df['Close'])])
    fig.write_image("output.png")


    if(timeframe == 1):
        embed = discord.Embed(title=f"Stock information for {ticker.upper()}",description=f"Timeframe: {timeframe} day",color=discord.Color.blue())

        embed.add_field(name="Open: ",value=f"${round(df['Open'].mean(), 2)}",inline=True)
        embed.add_field(name="High: ",value=f"${round(df['High'].mean(), 2)}",inline=True)
        embed.add_field(name="Low: ",value=f"${round(df['Low'].mean(), 2)}",inline=True)
        embed.add_field(name="Close: ",value=f"${round(df['Close'].mean(), 2)}",inline=True)
    else:
        embed = discord.Embed(title=f"Stock information for {ticker.upper()}",description=f"Timeframe: {timeframe} days",color=discord.Color.blue())

        open = df.describe()["Open"]
        high = df.describe()["High"]
        low = df.describe()["Low"]
        close = df.describe()["Close"]

        embed.add_field(name="Open: ",value=f"Mean: ${round(open[1], 2)}\nHigh: ${round(open[7], 2)}\nLow: ${round(open[3], 2)}",inline=False)
        embed.add_field(name="High: ",value=f"Mean: ${round(high[1], 2)}\nHigh: ${round(high[7], 2)}\nLow: ${round(high[3], 2)}",inline=False)
        embed.add_field(name="Low: ",value=f"Mean: ${round(low[1], 2)}\nHigh: ${round(low[7], 2)}\nLow: ${round(low[3], 2)}",inline=False)
        embed.add_field(name="Close: ",value=f"Mean: ${round(close[1], 2)}\nHigh: ${round(close[7], 2)}\nLow: ${round(close[3], 2)}",inline=False)

    await ctx.send(embed=embed)
    await ctx.send("Here's a candlestick chart to go along with that data:")
    await ctx.send(file=discord.File('output.png'))

@bot.command(aliases=['timer', 'remindme'])
async def remind(ctx, time="5m", *, message="Here is your reminder!"):
    seconds = 0
    user = ctx.message.author
    embed = discord.Embed(title=f"Reminder for {user} has been set for {time} from now",description=f"Message: {message}",color=discord.Color.blue())
    if time.lower().endswith("d"):
        seconds = int(time.replace("d","")) * 60 * 60 * 24
    if time.lower().endswith("h"):
        seconds = int(time.replace("h","")) * 60 * 60
    if time.lower().endswith("m"):
        seconds = int(time.replace("m","")) * 60
    if time.lower().endswith("s"):
        seconds = int(time.replace("s",""))

    await ctx.send(embed=embed)
    await s(seconds)
    await ctx.send(f'Hey {user.mention}! {message}')


bot.run("Nzc1NTM3NTExNDAxMTI3OTk2.X6nxlw.Q5QvcoQXU-XuUt0EImNlRFv77B4")
