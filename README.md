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

```python
class Agent:
    def __init__(self, name, base_population, sensitivity):
        self.name = name
        self.base_population = base_population
        self.sensitivity = sensitivity

    def calculate_population(self, partner_population):
        return self.base_population + (self.sensitivity * partner_population)
