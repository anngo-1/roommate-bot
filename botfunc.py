
#TABLE NAME IS reminders
#FORMAT IS (userid, date, time, text)

import sqlite3 
connection = sqlite3.connect('bruhbruh.db')
cur = connection.cursor()
 

for i in cur.execute("SELECT userid, date, time, text FROM reminders"):
     print(i)



# cur.execute("""INSERT INTO reminders VALUES ('241242', '5/21', '9:32pm', 'This is another test.') """)
# cur.execute("DELETE FROM reminders where time='9:32pm'")






class Schedules:
    def __init__(self):
        self.name = "Schedules"
        self.desc = "This is a tool to upload & view class schedules of roommates."
        funclist = [method_name for method_name in dir(Schedules) if callable(getattr(Schedules, method_name)) if method_name[0]!="_"]
        self.functions = ""
        for i in funclist:
            self.functions = "!" + i + "\n" + self.functions
    def __str__(self):  
        return "class working"

    def registerschedule(self):
        print("registerschedule working")

    def schedule(self, name):
        print("scheduleworking")


class Reminders:
    def __init__(self):
        self.name = "Reminders"
        self.desc = "Reminders allows Roommate bot to send notifications ahead of time to your roommates to remind them of events, private time, etc."
        funclist = [method_name for method_name in dir(Reminders) if callable(getattr(Reminders, method_name)) if method_name[0]!="_"]
        self.functions = ""
        for i in funclist:
            self.functions = "!" + i + "\n" + self.functions
    


    def __str__(self):  
        return "class working"

    def registerreminder(self, id, date, time, text):
        
        if date == None or time == None or text == None:
            return  "Error: function received the incorrect arguments \n``Example: !registerreminder 10/25 10:23pm I need to beat it``"

        else:
            cur.execute("""INSERT INTO reminders (userid, date, time, text) VALUES (?,?,?,?)""", (id, date, time, text))
            connection.commit()
            return ("Reminder added succesfully.")

    def reminders(self, id, y, z, w):
        empty = ""
        for i in cur.execute("SELECT userid, date, time, text FROM reminders"):
            formatlist = ["","Date: ", "Time: ", "Text: "]
            if i[0] == id:
                for x in range(0,len(i)):
                    if x == 0:
                        empty = empty + "Reminds you in X minutes/hours/seconds" +"\n"
                    else:
                        empty = empty + formatlist[x] + i[x] + "\n"
                   
                empty +="\n\n"
        
        return ("```" + "YOUR REMINDERS" + "\n\n" + empty + "```")


async def messagefunc(client, chan, text):
    await chan.send(text) 










scheduleobj = Schedules()
remindersobj = Reminders()

commandlist = [scheduleobj, remindersobj]