# Print “Calculate the area of a wall.”
# Prompt user
# “Enter the width in meters: ”
# Store the input value into Feed variable.
# Convert the Feed variable into an integer and store it in Width variable
# Prompt user
# “Enter the height in meters: ”
# store the input value into Feed variable.
# Convert the Feed variable into an integer and store it in Height variable
# Print “Width is {Width} m and height is {Height} m.”

# Multiply Width and Height, then store the result in Area variable
# Display results to the user: “The wall will be {Area} square meters.”

print("Calculate the area of a wall.") 
while True:
    try:
        feed = input("Enter the width in meters: ")
        Width = float(feed)
        # Width = int(feed)
        break
    except:
        print(f"Please enter a valid number. {feed} is not a number.")
while True:
    try:
        feed = input("Enter the height in meters: ")
        Height = float(feed)
        # Height = int(feed)
        break
    except:
        print(f"Please enter a valid number. {feed} is not a number.") 

print(f"Width is {Width} m and height is {Height} m.")

Area = Width * Height
print(f"The wall will be {Area} square meters.")


