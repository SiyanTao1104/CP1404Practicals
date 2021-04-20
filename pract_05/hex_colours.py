"""
CP1404 Practical
Hexadecimal colour lookup
"""

COLOUR_CODES = {"aliceblue": "#f0f8ff", "antiquewhite": "#faebd7",
                "antiquewhite1": "#ffefdb", "antiquewhite2": "#eedfcc",
                "lightcoral": "#f08080", "antiquewhite4": "#8b8378",
                "aquamarine1": "#7fffd4", "aquamarine2": "#76eec6",
                "aquamarine4": "#458b74", "azure1": "#f0ffff",
                "greenyellow": "#adff2f", "hotpink": "#ff69b4", "azure4": "#838b8b",
                "beige": "#f5f5dc", "lightseagreen": "#20b2aa"}

colour_name = input("Enter a colour name: ")
colour_name = colour_name.lower()
while colour_name != "":
    if colour_name in COLOUR_CODES:
        print(colour_name, "is", COLOUR_CODES[colour_name])
    else:
        print("Invalid colour code!")
    colour_name = input("Enter a colour name: ")
