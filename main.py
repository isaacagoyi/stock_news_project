import requests
from twilio import client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = "HY5NJ7LVIX3OSCOG"
NEWS_API_KEY = "40c57ebaa57549c68a3a41883a737100"

# STEP 1: Use https://www.alphavantage.co/documentation/#daily

# Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries.

stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,
}

response = requests.get(url=STOCK_ENDPOINT, params=stock_parameters)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]  # Here, we convert dictionary to a list
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]
print(yesterday_closing_price)

# Get the day before yesterday's closing stock price

day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]
print(day_before_yesterday_closing_price)

# Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20.
difference = abs(float(yesterday_closing_price) - float(day_before_yesterday_closing_price))

# Work out the percentage difference in price between closing price yesterday
# and closing price the day before yesterday.
percentage_difference = (difference / float(yesterday_closing_price)) * 100
print(percentage_difference)

## STEP 2: https://newsapi.org/
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

# Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
news_parameters = {
    "apikey": NEWS_API_KEY,
    "qInTitle": COMPANY_NAME,
}
if percentage_difference < 5:
    news_response = requests.get(url=NEWS_ENDPOINT, params=news_parameters)
    news_response = news_response.json()
    news_article = news_response["articles"]
    # Use Python slice operator to create a list that contains the first 3 articles.
    article_list = news_article[:3]
    print(article_list)

    # Use twilio.com/docs/sms/quickstart/python
    # to send a separate message with each article's title and description to your phone number.
    # Create a new list of article message for the 3 headline and description using list comprehension.
    article_message = [f"Headline: {article['title']}, \n Article Description: {article['description']}"
                       for article in article_list]
    for message in article_message:
        with open("article_message.txt", mode="w") as article_file:
            article_file.write()
