import datetime
year = raw_input('Enter year in format YYYY... ')
mon = raw_input('Enter month in format MM ')
date = raw_input('Enter date in format ')
a = datetime.date(int(year), int(mon), int(date)).weekday()  # 3=Thursday
d = { 0 : "Monday",
      1 : "Tuesday",
      2 : "Wednesday",
      3 : "Thursday",
      4 : "Friday",
	  5 : "Saturday",
	  6 : "Sunday"
    }
print "It's {}".format(d[a])