import pprint, pickle, os, datetime

#Open the saved pickle file

if os.path.isfile('data.pkl') == True:
    pkl_file = open('data.pkl', 'rb')
    reminders= pickle.load(pkl_file)
    remdates= pickle.load(pkl_file)
else:
    reminders = ['']
    remdates = ['']
    diffdate = ['']

for x in range(0, len(reminders)):
    print reminders[x], remdates[x]
#datetime.datetime.strptime(string_date, "%Y-%m-%d %H:%M:%S.%f")

rem1 = raw_input('Enter the Reminder ')
rem1date = raw_input('Enter date of this reminder in format DDMMYYYY ')
if rem1 != '' and rem1date != '':
    reminders.append(rem1)
    remdates.append(rem1date)
else:
    print 'Unexpected or no input, not adding anything'


def show_msg(x, leftdays):
    if leftdays > 0:
	    return 'The number of days left for ' + reminders[x] + ' is ' + str(leftdays)
    elif leftdays < 0:
        return 'Already behind ' + str(leftdays * (-1)) + ' days for ' + reminders[x]
    else:
        return 'Today is last day for ' + reminders[x]


#calculate the date difference
for x in range(1, len(remdates)):
    global msg1
    #print len(remdates)
    day1 = remdates[x][0:2]
    mon1 = remdates[x][2:4]
    year1 = remdates[x][4:8]
    #print day1, mon1, year1
    today = datetime.date.today()
    someday = datetime.date(int(year1), int(mon1), int(day1))
    diff = someday - today
    #print diff.days
    leftdays = diff.days
    mymsg = show_msg(x, leftdays)
    print '=============================================================='
    print mymsg
    print '=============================================================='
	
	
    #print today

#for x in range(0, len(reminders)):
    #print reminders[x], remdates[x]

#Write to pickle file
output = open('data.pkl', 'wb')
pickle.dump(reminders, output)
pickle.dump(remdates, output)

output.close()

