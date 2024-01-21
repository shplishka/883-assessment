#!/usr/bin/env python3

from bender import Bender

class FireBender(Bender):
    
    def __init__(self, name, power):
        super().__init__(name, power)
        self.skill = "Firebending"

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
        return f"{self.name} is bending fire with a power level of {self.power}!"

    def enhance_power(self, boost):
        self.power += boost
        return f"{self.name} enhanced their firebending power by {boost} units!"

    def special_ability(self):
        return f"{self.name} is using their special firebending ability!"

    def use_firebending(self):
        message = f"{self.name} is using his firebending skill!"
        print(message)

    def inferno_attack(self, enemy):
        damage = self.power * 2
        print(f"{self.name} uses Inferno Attack on {enemy} and deals {damage} damage!")
        return damage

    def power_up(self, boost):
        self._power += boost

    def roaring_flames(self, enemy):
        print(f"{self.name} uses Roaring Flames on {enemy} and defeats them!")
        return True
