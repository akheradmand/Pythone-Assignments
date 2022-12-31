class Time:

    def __init__(self,hh,mm,ss):
        #properties
        self.hour=hh
        self.minute=mm
        self.second=ss
        self.fix()

    #methods
    def show(self):
        print(self.hour,":",self.minute,":",self.second)
    
    def sum(self,other):
        s_new = self.second + other.second
        m_new = self.minute + other.minute
        h_new = self.hour + other.hour
        result = Time(h_new,m_new,s_new)
        return result

    def sub(self,other):
        s_new = self.second - other.second
        m_new = self.minute - other.minute
        h_new = self.hour - other.hour
        result = Time(h_new,m_new,s_new)
        return result

    def seconds_to_time(self):
        hour=self//3600
        minute=(self % 3600) // 60
        seconds=self % 60
        result= Time(hour,minute,seconds)
        return result

    def time_to_seconds(self):
        global seconds
        seconds=self.hour*3600+self.minute*60+self.second
        return seconds

    def gmt_to_tehran(self):
        difference_time=Time(3,30,00)
        tehran_time=self.sum(difference_time)
        return tehran_time


    def fix(self):
        if self.second >= 60:
            self.second -= 60
            self.minute += 1

        if self.minute >= 60:
            self.minute -= 60
            self.hour += 1

        if self.second < 0:
            self.second += 60
            self.minute -= 1

        if self.minute < 0:
            self.minute += 60
            self.hour -= 1


t1=Time(5,75,17)
print("\033[38;5;4m","t1: ","\033[0m",end='')
t1.show()

t2=Time(4,50,2)
print("\033[38;5;4m","t2: ","\033[0m",end='')
t2.show()

# t1+t2
t3=t1.sum(t2)
print("\033[38;5;4m","t1+t2: ","\033[0m",end='')
t3.show()

# t1-t2
t4=t1.sub(t2)
print("\033[38;5;4m","t1-t2: ","\033[0m",end='')
t4.show()

# convert seconds to time
t=Time.seconds_to_time(3682)
print("\033[38;5;4m","3682 s: ","\033[0m",end='')
t.show()

# convert time to seconds
t1.time_to_seconds()
print("\033[38;5;4m",end='')
t1.show()
print("= ","\033[0m",end='')
print(seconds,"sec")

# convert GMT time to tehran
tehran_time=t1.gmt_to_tehran()
print("\033[38;5;4m","t1 in tehran time: ","\033[0m",end='')
tehran_time.show()
