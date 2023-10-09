class CarbonFootprintCalculator:
    def __init__(self, transportation_emissions, home_emissions, diet_emissions):
        self.transportation_emissions = transportation_emissions
        self.home_emissions = home_emissions
        self.diet_emissions = diet_emissions

    def calculate_total_emissions(self):
        return self.transportation_emissions + self.home_emissions + self.diet_emissions

    def get_suggestions(self):
        suggestions = []
        if self.transportation_emissions > 1000:  # arbitrary threshold
            suggestions.append("Consider using public transportation to reduce your transportation emissions.")
        if self.home_emissions > 1000:  # arbitrary threshold
            suggestions.append("Consider using energy-efficient appliances to reduce your home emissions.")
        if self.diet_emissions > 1000:  # arbitrary threshold
            suggestions.append("Consider adopting a plant-based diet to reduce your diet emissions.")
        return suggestions

# Example usage:
transportation_emissions = float(input("Enter your monthly transportation emissions (in kg CO2): "))
home_emissions = float(input("Enter your monthly home emissions (in kg CO2): "))
diet_emissions = float(input("Enter your monthly diet emissions (in kg CO2): "))

calculator = CarbonFootprintCalculator(transportation_emissions, home_emissions, diet_emissions)

total_emissions = calculator.calculate_total_emissions()
suggestions = calculator.get_suggestions()

print(f"\nYour total monthly emissions are {total_emissions} kg CO2.")
print("Here are some suggestions to reduce your carbon footprint:")
for suggestion in suggestions:
    print(f"- {suggestion}")
