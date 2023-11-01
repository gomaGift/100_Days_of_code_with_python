# def solution(arr):
#     t = arr
#     millipede = t[0]
#     t.remove(t[0])
#
#     test = True
#
#     while test:
#         added = False
#         for i in range(len(t)):
#             if millipede[len(millipede) - 1] == t[i][0]:
#                 millipede += t[i]
#                 t.remove(t[i])
#                 added = True
#                 break
#         if not added:
#             for i in range(len(t)):
#                 if t[i][len(t[i]) - 1] == millipede[0]:
#                     millipede = t[i] + millipede
#                     t.remove(t[i])
#                     added = True
#                     break
#         if not added or len(t) == 0:
#             test = False
#
#     if len(t) == 0:
#         return True
#     return False
#
#
# d = ['tablet', 'east', 'endorse', 'traffic']
# print(solution(d))
# thislist = ["apple", "banana", "cherry", "banana"]
# thislist.remove("banana")
# print(thislist)

import requests
import datetime as dt

todaysdate = dt.datetime.now()
month = todaysdate.month
day = todaysdate.day

print(day)
print(month)
# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=IBM&apikey=IF2L4DSO5YWGXBTS'
r = requests.get(url)
data = r.json()
yesterday_closing_price = float(data['Time Series (Daily)']['2023-01-04']['4. close'])
day_before_yesterday_closing_price = float(data['Time Series (Daily)']['2023-01-03']['4. close'])

price_difference = abs(yesterday_closing_price - day_before_yesterday_closing_price)

percent_diff = price_difference/ (yesterday_closing_price + day_before_yesterday_closing_price) / 2 * 100

print(data)
print(yesterday_closing_price)
print(day_before_yesterday_closing_price)
print(percent_diff)
