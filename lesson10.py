class AnimalCreationError(Exception):
    def __init__(self, animal_type):
        self.animal_type = animal_type

    def __str__(self):
        return f"AnimalCreationError: Ошибка создания животного '{self.animal_type}'"


class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        return "Гав!"


class Cat(Animal):
    def speak(self):
        return "Мяу!"


class AnimalFactory:
    @staticmethod
    def create_animal(animal_type, name):
        if animal_type == "Dog":
            return Dog(name)
        elif animal_type == "Cat":
            return Cat(name)
        else:
            raise AnimalCreationError(animal_type)


try:
    animal_type = input("Введите тип животного (Dog или Cat): ")
    name = input("Введите имя животного: ")

    animal = AnimalFactory.create_animal(animal_type, name)
    print(f"Создано животное с именем {animal.name}")
    print(f"Звук, издаваемый животным: {animal.speak()}")

except AnimalCreationError as e:
    print(str(e))
except Exception as e:
    print(f"Произошла ошибка: {str(e)}")