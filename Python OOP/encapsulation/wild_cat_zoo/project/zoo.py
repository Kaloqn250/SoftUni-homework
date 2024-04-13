from project.animal import Animal


class Zoo:

    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal: Animal, price):
        if self.__budget >= price and self.__animal_capacity > len(self.animals):
            self.animals.append(animal)
            self.__budget -= price
            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

        elif self.__budget < price and self.__animal_capacity >= len(self.animals):
            return "Not enough budget"

        return "Not enough space for animal"

    def hire_worker(self, worker):
        if self.__workers_capacity > len(self.workers):
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"

        return "Not enough space for worker"

    def fire_worker(self, worker_name):
        try:
            worker = next(filter(lambda w: w.name == worker_name, self.workers))
        except StopIteration:
            return f"There is no {worker_name} in the zoo"

        self.workers.remove(worker)
        return f"{worker_name} fired successfully"

    def pay_workers(self):
        workers_salary = sum([w.salary for w in self.workers])

        if self.__budget >= workers_salary:
            self.__budget -= workers_salary
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"

        return f"You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        animals_budget = sum([a.money_for_care for a in self.animals])

        if self.__budget >= animals_budget:
            self.__budget -= animals_budget
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

        return f"You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        result = f"You have {len(self.animals)} animals\n"
        lions = []
        tigers = []
        cheetahs = []

        for animal in self.animals:
            if animal.__class__.__name__ == 'Lion':
                lions.append(animal)

            elif animal.__class__.__name__ == 'Tiger':
                tigers.append(animal)

            elif animal.__class__.__name__ == 'Cheetah':
                cheetahs.append(animal)

        result += f'----- {len(lions)} Lions:\n'
        result += ''.join([f'{l}\n' for l in lions])

        result += f'----- {len(tigers)} Tigers:\n'
        result += ''.join([f'{t}\n' for t in tigers])

        result += f'----- {len(cheetahs)} Cheetahs:\n'
        result += ''.join([f'{c}\n' for c in cheetahs])

        return result.strip()

    def workers_status(self):
        result = f"You have {len(self.workers)} workers\n"
        keeper = []
        caretaker = []
        vet = []

        for worker in self.workers:
            if worker.__class__.__name__ == 'Keeper':
                keeper.append(worker)

            elif worker.__class__.__name__ == 'Caretaker':
                caretaker.append(worker)

            elif worker.__class__.__name__ == 'Vet':
                vet.append(worker)

        result += f'----- {len(keeper)} Keepers:\n'
        result += ''.join([f'{k}\n' for k in keeper])

        result += f'----- {len(caretaker)} Caretakers:\n'
        result += ''.join([f'{c}\n' for c in caretaker])

        result += f'----- {len(vet)} Vets:\n'
        result += ''.join([f'{v}\n' for v in vet])

        return result.strip()
