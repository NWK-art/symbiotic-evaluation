
class Agent:
    def __init__(self, name, base_population, sensitivity):
        self.name = name
        self.base_population = base_population
        self.sensitivity = sensitivity

    def calculate_population(self, partner_population):
        return self.base_population + (self.sensitivity * partner_population)
