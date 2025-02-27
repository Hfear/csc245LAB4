#Use the itertools.cycle function to cycle through a list of colors ["red", "blue","green"]
# indefinitely and print the first 6 values.
import itertools

colors = ["red", "blue", "green"]

colorcycle = itertools.cycle(colors)

for color in colorcycle:
    print(color)

