#!/usr/bin/env python3

class Dog:
    APPROVED_BREEDS = [
        "Mastiff",
        "Chihuahua",
        "Corgi",
        "Shar Pei",
        "Beagle",
        "French Bulldog",
        "Pug",
        "Pointer"
    ]

    def __init__(self, name="Rex", breed="pug"):
        if isinstance(name, str) and 1 <= len(name) <= 25 and name != '':
            self.name = name
        else:
            print("Name must be string between 1 and 25 characters.")

        if breed in Dog.APPROVED_BREEDS:
            self.breed = breed
        else:
            print("Breed must be in list of approved breeds.")


newDog = Dog("1", "Pug")
newDog.name



