#!/usr/bin/env python3

from bender import Bender

class EarthBender(Bender):
    
    def __init__(self, name, power):
        super().__init__(name, power)
        self.skill = "Earthbending"

    @property
    def power(self):
        return self._power
    
    @power.setter
    def power(self, power):
        if isinstance(power, int):
            self._power = power
        else:
            print("Power level must be an integer")

    def bend(self):
        return f"{self.name} is bending earth with a power level of {self.power}!"

    def enhance_power(self, boost):
        self.power += boost
        return f"{self.name} enhanced their earthbending power by {boost} units!"

    def special_ability(self):
        return f"{self.name} uses seismic sense to detect hidden objects!"

    def use_earthbending(self):
        message = f"{self.name} is using her earthbending skill!"
        print(message)
