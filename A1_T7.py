# Create a Python program that is able to calculate car’s fuel consumption (diesel or petrol) and present the consumption in liters per 100km “x l per 100 km”

# Print info message “Calculate fuel consumtion.”
# Ask “Enter travel distance(kilometers): ” and store the value to Feed variable
# Convert the Feed into an integer and assign it to Distance variable
# Ask “Enter fuel usage(liters): ”
# Convert the Feed into an integer and assign it to FuelUsage variable
# Calculate the Consumption for 100 km
# Convert the Consumption back to an integer
# Print “Fuel consumption is {Consumption} l per 100 km”

# eXample program run:
# Calculate fuel consumption.
# Enter travel distance(kilometers): 200
# Enter fuel usage(liters): 20
# Fuel consumption is 10 l per 100 km

print("Calculate fuel consumption.")
Feed = input("Enter travel distance(kilometers): ")
Distance = int(Feed)
Feed = input("Enter fuel usage(liters): ")
FuelUsage = int(Feed)
# Calculate the Consumption for 100 km
Feed = (FuelUsage / Distance) * 100
Consumption = int(Feed)
print(f"Fuel consumption is {Consumption} l per 100 km")
