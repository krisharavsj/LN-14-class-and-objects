
class Dog:
    species = "Canis familiaris"

    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def display_details(self):
        print(f"Name   : {self.name}")
        print(f"Breed  : {self.breed}")
        print(f"Species: {Dog.species}")
        print("----x---------x------")
dog1 = Dog("Max", "Golden Retriever")
dog2 = Dog("Bella", "German Shepherd")
dog1.display_details()
dog2.display_details()