import logging
import argparse

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


if __name__ == "__main__":

    logger = logging.getLogger("animal_factory")
    logger.setLevel(logging.ERROR)

    file_handler = logging.FileHandler("animal_factory.log")
    file_handler.setLevel(logging.ERROR)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.ERROR)

    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    try:
        parser = argparse.ArgumentParser(description="Animal Factory")
        parser.add_argument("animal_type", choices=["Dog", "Cat"], help="Type of animal")
        parser.add_argument("name", type=str, help="Name of the animal")
        args = parser.parse_args()

        animal = AnimalFactory.create_animal(args.animal_type, args.name)
        logger.info(f"Создано животное с именем {animal.name}")
        logger.info(f"Звук, издаваемый животным: {animal.speak()}")

    except AnimalCreationError as e:
        logger.error(str(e))

    except Exception as e:
        logger.error(f"Произошла ошибка: {str(e)}")