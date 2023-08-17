import calendar

year = 2023
month = 8  # August
week_width = 2  # Number of characters per day
line_width = 20  # Total width of each line (adjust as needed)

cal = calendar.TextCalendar()
month_calendar = cal.formatmonth(year, month, w=week_width, l=line_width)

print(month_calendar)
