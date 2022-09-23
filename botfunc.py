

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

    def registerreminder(self, date, time, text):
        
        if date == None or time == None or text == None:
            return  "Error: function received the incorrect arguments \n``Example: !registerreminder 10/25 10:23pm I need to beat it``"

        else:
            return (date + " "  +time+ " " + text)

    def reminders(self):
        print("None")


async def messagefunc(client, chan, text):
    await chan.send(text) 










scheduleobj = Schedules()
remindersobj = Reminders()

commandlist = [scheduleobj, remindersobj]