# -R03--1FA09--ARADO-
This script calculates the straight-line distance between two points on a 2D coordinate plane using the Pythagorean theorem.

The program prompts the user to enter the X and Y values for two separate points. Once these coordinates are provided, it calculates the horizontal distance and vertical distance between them. It then applies the Euclidean distance formula to find the direct length between the two points.

To run this script, you only need to have Python 3.x installed on your computer. No external libraries are required.

When you run the script, the following actions occur:The terminal displays a message asking for the first set of coordinates.The program pauses to accept decimal or integer inputs for x1 and y1.The terminal displays a message asking for the second set of coordinates.The program pauses to accept decimal or integer inputs for x2 and y2.The system performs the calculation instantly and prints the final distance value to the screen.


The script imports the Python math module to access the math.hypot function. This function uses the Pythagorean theorem formula:distance = square root of ((x2 - x1)^2 + (y2 - y1)^2)It subtracts the first X coordinate from the second X coordinate to find the horizontal change, and subtracts the first Y coordinate from the second Y coordinate to find the vertical change. The function squares both differences, adds them together, and calculates the square root of the total to output the final result.
