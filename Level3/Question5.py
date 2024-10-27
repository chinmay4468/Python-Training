class Time:
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes

    def addTime(self, other):
        total_minutes = self.minutes + other.minutes
        extra_hours = total_minutes // 60
        total_hours = self.hours + other.hours + extra_hours
        total_minutes = total_minutes % 60

        return Time(total_hours, total_minutes)

    def displayTime(self):
        print(f"{self.hours} hr and {self.minutes} min")

    def displayMinute(self):
        total_minutes = self.hours * 60 + self.minutes
        print(f"Total minutes: {total_minutes}")

time1 = Time(2, 50)
time2 = Time(1, 20)

total_time = time1.addTime(time2)

total_time.displayTime()  

total_time.displayMinute()  
