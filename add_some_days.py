import datetime
y, m, d = map(int, input().split())
plus_days = int(input())
current_date = datetime.date(y,m,d)

delta = datetime.timedelta(days=plus_days)
final_date = current_date + delta

print(final_date.year, final_date.month, final_date.day)