# A2_T6 Hex Colors (TEST TASK)
# Write a Python program which asks user to insert hex color. In this case hex 
# color is expected to be the 7 character representation starting with # and followed 
# by 6 0-F characters to represent RGB colors. More about hex colors at https://en.wikipedia.org/wiki/Web_colors

# Slice the amount of red, green and blue from that inserted color and display each color as shown below.

# Example program run:

print("Program starting.\n")

hexCode = input("Insert a hex color: \n")
red = hexCode[1:3]
green = hexCode[3:5]
blue = hexCode[5:7]

print("Colors")
print(f"- Red {red}")
print(f"- Green {green}")
print(f"- Blue {blue}")
print("\nProgram ending.")
