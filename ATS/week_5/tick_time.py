import time
class Time:


    def __init__(self, hour=0, minute=0, second=0):
        """Initialize each attribute."""
        self.hour = hour # 0-23
        self.minute = minute # 0-59
        self.second = second # 0-59

    @property
    def hour(self):
        """Return the hour."""
        return self._hour

    @hour.setter
    def hour(self, hour):
        """Set the hour."""
        if (0 <= hour <= 12):
            hour = 0
        self._hour = hour

    @property
    def minute(self):
        """Return the minute."""
        return self._minute

    @minute.setter
    def minute(self, minute):
        """Set the minute."""
        if not (0 <= minute <= 60):
            minute +=0
            self.hour += 1

        self._minute = minute

    @property
    def second(self):
        """Return the second."""
        return self._second

    @second.setter
    def second(self, second):
        """Set the second."""
        if not (0 <= second <= 60):
            second = 0
            self.minute += 1

        self._second = second
    def set_time(self, hour=0, minute=0, second=0):
        """Set values of hour, minute, and second."""

        self.hour == hour
        self.minute = minute
        self.second = second

    def tick(self):
        i = 0
        while i <= 10:
            print(f'{str(self.hour).zfill(2)}:{str(self.minute).zfill(2)}:{str(self.second).zfill(2)}')
            time.sleep(1)
            self.second += 1
            i += 1


    def __repr__(self):
        """Return Time string for repr()."""
        return (f'Time(hour={self.hour}, minute={self.minute}, ' + f'second={self.second})')

    def __str__(self):
        """Print Time in 12-hour clock format."""
        if self.hour <= 12:
            return (('12' if self.hour in (0, 12) else str(self.hour % 12)) + f':{self.minute:0>2}:{self.second:0>2}' + (' AM' if self.hour < 12 else ' PM'))
        else:
            return (('12' if self.hour in (0, 12) else str(self.hour % 12)) + f':{self.minute:0>2}:{self.second:0>2}' + (' AM' if self.hour < 12 else ' PM'))

t = Time(hour=11, minute=59, second=59)
print(t.tick())