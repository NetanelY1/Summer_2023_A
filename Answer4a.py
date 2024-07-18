class Time:
    def __init__(self, hour, minutes):
        self.hour = hour
        self.minutes = minutes

    def difference(self, other):
        # חישוב הזמן הכולל בדקות עבור כל זמן
        total_minutes_self = self.hour * 60 + self.minutes
        total_minutes_other = other.hour * 60 + other.minutes

        # החזרת ההפרש בדקות
        return total_minutes_other - total_minutes_self
