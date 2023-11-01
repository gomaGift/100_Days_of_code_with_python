import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_API = ' IF2L4DSO5YWGXBTS'

stock_params = {
    'function': 'TIME_SERIES_DAILY_ADJUSTED',
    'symbol': STOCK_NAME,
    'apikey': STOCK_API
}

stock_endpoint = 'https://www.alphavantage.co/query'
stock_response = requests.get(url=stock_endpoint, params=stock_params)
# access daily stock data
data = stock_response.json()['Time Series (Daily)']
daily_stock_data = [value for (key, value) in data.items()]

# access yesterday and the day before yesterday stock prices
yesterday_stock_price = daily_stock_data[0]['4. close']
day_before_yesterday_stock_price = daily_stock_data[1]['4. close']

price_difference = float(yesterday_stock_price) - float(day_before_yesterday_stock_price)

change = None
if price_difference < 0:
    change = '🔻'
else:
    change = '🔺'

percent_diff = round(abs(price_difference / float(yesterday_stock_price) * 100), 2)

NEWS_API = 'c1114698fd734b398c1f5766bfcf1b74'
NEWS_ENDPOINT = 'https://newsapi.org/v2/everything'

news_params = {
    'qInTitle': COMPANY_NAME,
    'apiKey': NEWS_API,
}


news_response = requests.get(url=NEWS_ENDPOINT, params=news_params)
news = news_response.json()
# get the three first articles from the news api
news_articles = news['articles']
top_3_articles = [article for article in news_articles[:3]]

TWILIO_ACC_SID = 'AC00bb47cb2ac49df6b4142bbfb94bd11e'
AUTH_TOKEN = '6a0d56836734c22f14f313efaa5f2130'
client = Client(TWILIO_ACC_SID, AUTH_TOKEN)

# send three separate text messages to owner number of the formatted articles
if percent_diff > 1:
    for article in top_3_articles:
        message = client.messages.create(
            body=f'TSLA: {change}{percent_diff}%\n'
                 f'Headline: {article["title"]}\n'
                 f'Brief: {article["description"]}',
            from_="+16516612493",
            to="+260976693699"
        )
