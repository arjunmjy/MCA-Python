import datetime
today = datetime.date.today()
print("Today:", today)
yesterday = today - datetime.timedelta(days=1)
print("Yesterday:", yesterday)
tomorrow = today + datetime.timedelta(days=1)
print("Tomorrow:", tomorrow)
