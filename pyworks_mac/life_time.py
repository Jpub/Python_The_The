import datetime

today = datetime.date.today()
birthday = datetime.date(1975, 8, 3)
life = today - birthday
print(life.days)