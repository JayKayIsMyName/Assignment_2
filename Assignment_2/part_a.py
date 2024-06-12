# Part a

from abc import ABC, abstractmethod
from datetime import datetime, timedelta

class AbstractDateCalculator(ABC):
    @abstractmethod
    def calculate_future_date(self, days):
        pass

class DateCalculator(AbstractDateCalculator):
    def __init__(self, current_date):
        self.current_date = current_date

    def calculate_future_date(self, days):
        return self.current_date + timedelta(days=days)

calculator = DateCalculator(datetime.now())

future_date = calculator.calculate_future_date(10)

print(f"The date 10 days from now is: {future_date}")
