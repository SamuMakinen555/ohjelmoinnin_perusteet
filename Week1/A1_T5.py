#* Print “Calculate the area of a wall.”
print("Calculate the area of a wall.")
#* Prompt user
#  * “Enter the width in meters: ”
#  * Store the input value into Feed variable.
Feed = input("Enter the width in meters: ")
#* Convert the Feed variable into an integer and store it in Width variable
Width = int(Feed)
#* Prompt user
#  * “Enter the height in meters: ”
#  * Store the input value into Feed variable.
Feed = input("Enter the height in meters: ")
#* Convert the Feed variable into an integer and store it in Height variable
Height = int(Feed)
#* Print “Width is {Width} m and height is {Height} m.”
print("Width is", Width, "m and height is", Height, "m.")
#* Multiply Width and Height, then store the result in Area variable
Area = Width * Height
#* Display results to the user: “The wall will be {Area} square meters.”
print("The wall will be", Area, "square meters.")


#* Try the program with different inputs e.g. decimals. Notice any problems in the program? Are you able to solve the issue?
# Use float instead of int.