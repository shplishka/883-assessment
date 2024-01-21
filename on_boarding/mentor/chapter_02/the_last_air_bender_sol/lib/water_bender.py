#!/usr/bin/env python3

from bender import Bender

class WaterBender(Bender):
    
    def __init__(self, name, power):
        super().__init__(name, power)
        self.skill = "Waterbending"
        self.health = 100

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
        return f"{self.name} is bending water with a power level of {self.power}!"

    def enhance_power(self, boost):
        self.power += boost
        return f"{self.name} enhanced their waterbending power by {boost} units!"

    def special_ability(self):
        return f"{self.name} uses healing abilities to restore health!"

    def use_waterbending(self):
        message = f"{self.name} is using her waterbending skill!"
        print(message)

    def boost_power(self, boost):
        self.power += boost

    def freeze_enemy(self, enemy):
        return f"{enemy} (Frozen)"

    def heal_self(self, amount):
        self.health += amount
