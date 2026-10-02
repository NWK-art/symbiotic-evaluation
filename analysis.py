# analysis.py
# Symbiotic Evaluation Project: ИИ-агенты и анализ связей в экосистеме

import matplotlib.pyplot as plt
import numpy as np

class Agent:
    """
    Класс ИИ-агента (мех-вида).
    Каждый агент имеет базовую популяцию и коэффициент чувствительности к партнёру.
    """
    def __init__(self, name, base_population, sensitivity):
        self.name = name
        self.base_population = base_population
        self.sensitivity = sensitivity  # насколько сильно агент реагирует на партнёра

    def calculate_population(self, partner_population):
        """
        Логика ИИ-агента: популяция зависит от партнёра.
        Формула: base + (sensitivity * partner_population)
        Это имитирует симбиоз: если партнёр растёт, растёт и наш агент.
        """
        return self.base_population + (self.sensitivity * partner_population)

def load_data():
    """
    Инициализируем двух ИИ-агентов (мех-видов).
    """
    # Агент A: базовая популяция 1, реагирует слабо (sensitivity=0.5)
    agent_a = Agent(name="Mech-Species-A", base_population=1, sensitivity=0.5)
    # Агент B: базовая популяция 2, реагирует сильно (sensitivity=1.0)
    agent_b = Agent(name="Mech-Species-B", base_population=2, sensitivity=1.0)
    
    # Создадим шкалу времени (шаги симуляции)
    time_steps = np.array([1, 2, 3, 4, 5])
    
    return agent_a, agent_b, time_steps

def analyze_relationships(agent_a, agent_b, time_steps):
    """
    Запускаем симуляцию взаимодействия агентов на каждом шаге времени.
    """
    pop_a = []
    pop_b = []
    
    # На каждом шаге считаем популяцию обоих агентов, учитывая влияние друг друга
    for t in time_steps:
        # Популяция A зависит от текущей популяции B
        current_pop_a = agent_a.calculate_population(agent_b.base_population + t)
        # Популяция B зависит от текущей популяции A
        current_pop_b = agent_b.calculate_population(agent_a.base_population + t)
        
        pop_a.append(current_pop_a)
        pop_b.append(current_pop_b)
    
    return np.array(pop_a), np.array(pop_b)

def visualize_results(species_a, species_b):
    """
    Строим график зависимости популяций ИИ-агентов.
    """
    plt.figure(figsize=(10, 6))
    plt.plot(species_a, species_b, marker='o', linestyle='-', color='green', linewidth=2, label='Symbiotic Trend')
    
    plt.title('Simulation: Mech-Species AI Agents Interaction')
    plt.xlabel('Population of Mech-Species-A')
    plt.ylabel('Population of Mech-Species-B')
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend()
    
    # Добавим аннотацию, чтобы было видно, где начинается симуляция
    plt.annotate('Start', xy=(species_a, species_b), xytext=(species_a+0.5, species_b+0.5),
                 arrowprops=dict(facecolor='black', shrink=0.05))
    
    plt.show()

if __name__ == "__main__":
    print("Запуск симуляции экосистемы ИИ-агентов...")
    
    # 1. Загружаем данные (создаём агентов)
    agent_a, agent_b, time_steps = load_data()
    print(f"Созданы агенты: {agent_a.name} и {agent_b.name}")
    
    # 2. Анализируем связи (запускаем симуляцию)
    pop_a, pop_b = analyze_relationships(agent_a, agent_b, time_steps)
    print(f"Симуляция завершена. Популяция A: {pop_a}, Популяция B: {pop_b}")
    
    # 3. Визуализируем результат
    visualize_results(pop_a, pop_b)
