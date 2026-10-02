# Symbiotic Evaluation Project

This repository contains the materials for the Symbiotic Evaluation project.

## Overview
This project simulates the interaction of two mechanical species (Mech‑Species) modeled as simple AI agents. Each agent adjusts its population based on the presence of its symbiotic partner, demonstrating a basic ecosystem model driven by agent logic. The simulation uses Python with NumPy for calculations and Matplotlib for data visualization, illustrating how agent-based logic can
reflect symbiotic relationship dynamics.
## Technologies Used

*   Python
*   NumPy
*   Matplotlib

## Core Logic Snippet

This snippet shows the actual agent class used in `analysis.py`. It demonstrates how each Mech-Species calculates its population based on its partner's state:

```python
class Agent:
    def __init__(self, name, base_population, sensitivity):
        self.name = name
        self.base_population = base_population
        self.sensitivity = sensitivity

    def calculate_population(self, partner_population):
        # The population grows proportionally to the partner's presence
        return self.base_population + (self.sensitivity * partner_population)

# Example interaction between two Mech-Species
species_a = Agent("Mech-Species A", base_population=10, sensitivity=0.5)
species_b = Agent("Mech-Species B", base_population=10, sensitivity=0.5)

# Simulating one step of interaction
pop_a_next = species_a.calculate_population(species_b.base_population)
pop_b_next = species_b.calculate_population(species_a.base_population)
