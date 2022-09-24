#TABLE NAME IS reminders
#FORMAT IS (userid, date, time, text)

import sqlite3 
connection = sqlite3.connect('bruhbruh.db')
cur = connection.cursor()
 

for i in cur.execute("SELECT userid, date, time, text FROM reminders"):
     print(i)

# cur.execute("""INSERT INTO reminders VALUES ('241242', '5/21', '9:32pm', 'This is another test.') """)
# cur.execute("DELETE FROM reminders where time='9:32pm'")
