#!/usr/bin/env python

import datetime, time, sys

#now = time.time()
today = datetime.datetime.today()
(year, month, day) = map(int, sys.argv[1].split('/'))
date = datetime.datetime(year, month, day)
diff = today - date
birthdays = diff.days / 365
not_birthday_days = diff.days - birthdays

print 'date is: %s' % date
print 'today is: %s' % today
print 'diff: %s' % diff
print 'birthdays: %s' % birthdays
print 'not bday days: %d' % not_birthday_days
