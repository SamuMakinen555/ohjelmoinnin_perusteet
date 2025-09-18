#Create a Python program that is able to calculate car’s fuel consumption (diesel or petrol) and present the consumption in liters per 100km “x l per 100 km”
#
#    Print info message “Calculate fuel consumtion.”
print("Calculate fuel consumption.")
#    Ask “Enter travel distance(kilometers): ” and store the value to Feed variable
Feed = input("Enter travel distance(kilometers): ")
#    Convert the Feed into an integer and assign it to Distance variable
Distance = int(Feed)
#    Ask “Enter fuel usage(liters): ”
Feed = input("Enter fuel usage(liters): ")
#    Convert the Feed into an integer and assign it to FuelUsage variable
FuelUsage = int(Feed)
#    Calculate the Consumption for 100 km
Feed = 100 * FuelUsage / Distance
#    Convert the Consumption back to an integer
Consumption = int(Feed)
#    Print “Fuel consumption is {Consumption} l per 100 km”
print("Fuel consumption is", Consumption, "l per 100 km.")

#could maybe use floats and then round the number
#tai riville 16 Consumption = round(Feed), pyöristää lähimpään kokonaislukuun
