#!/usr/bin/env python3
# def __init__(self, name="Rex", breed="Pug"):
#     if isinstance(name, str) and 1 <= len(name) <= 25 and name != '':
#         self.name = name
#     else:
#         print("Name must be string between 1 and 25 characters.")
#
#     if breed not in Dog.APPROVED_BREEDS:
#         print("Breed must be in list of approved breeds.")
#     else:
#         self.breed = breed
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

    def __init__(self, name="glass", breed="Pug"):
        if isinstance(name, str) and 1 <= len(name) <= 25 and name != '':
            self._name = name
        else:
            print("Name must be string between 1 and 25 characters.")

        if breed not in Dog.APPROVED_BREEDS:
            print("Breed must be in list of approved breeds.")
        else:
            self._breed = breed

    def get_name(self):
        return self._name

    def set_name(self, new_name):
        if isinstance(new_name, str) and 1 <= len(new_name) <= 25 and new_name != '':
            print(f'{self._name} is now changed to {new_name}')
            self._name = new_name
        else:
            print("Name must be string between 1 and 25 characters.")

    def get_breed(self):
        return self._breed

    def set_breed(self, new_breed_name):
        if isinstance(new_breed_name, str) and 1 <= len(new_breed_name) <= 25 and new_breed_name != '':
            print(f'{self._name} is now changed to {new_breed_name}')
            self._name = new_breed_name
        else:
            print("Name must be string between 1 and 25 characters.")

    name = property(get_name, set_name)
    breed = property(get_breed, set_breed)





    #
    # def set_breed(self, breed):
    #     if breed not in Dog.APPROVED_BREEDS:
    #         print("Breed must be in list of approved breeds.")
    #     else:
    #         self.breed = breed
    #
    # def get_breed(self, breed):
    #     return self.breed


    # breed = property(get_breed, set_breed)

# newDog = Dog("ruloo")
# newDog.name = 12
# newDog.name




