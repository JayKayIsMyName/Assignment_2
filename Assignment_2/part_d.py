# Part d

class Celsius:
    def __init__(self, temperature=0):
        self._temperature = temperature

    @property
    def temperature(self):
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        if value < -273.15: # if temperature is below absolute zero
            raise ValueError("Temperature below absolute zero is not possible.")
        self._temperature = value

c = Celsius()
c.temperature = 100
print(c.temperature)