# Allison Obourn and Janalee O'Bagy
# CSc 110 Spring 2017
# Lecture 23

# gets city information from a file and earthquake location and radius
# from a user and then draws this information graphically showing
# which cities are affected by the quake. 

from drawingpanel import *

def main():
    cities = get_cities()

    # gets information from the user
    epi_x = int(input("Epicenter x? "))
    epi_y = int(input("Epicenter y? "))
    radius = int(input("Radius? "))

    draw(cities, epi_x, epi_y, radius)

# returns a list of tuples. Each tuple contains a city name, x and y
# from one line of cities.txt
def get_cities():
    file = open("cities.txt")
    lines = file.readlines()

    cities = []
    for line in lines: # each line has this format: Tucson 45 98
        parts = line.split()
        city = (parts[0], parts[1], parts[2])
        cities.append(city)
    return cities

# draws all of the cities as dots on a DrawingPanel. If they are
# in the affected radius colors them red, otherwise black.
# Draws a circle around the affected region
def draw(cities, epi_x, epi_y, radius):
    p = DrawingPanel(200, 200)
    p.canvas.create_oval(epi_x - radius, epi_y - radius, epi_x + radius,
                         epi_y + radius)
    for city in cities: 
        x = int(city[1])
        y = int(city[2])
        color = "black"
        if(x >= epi_x - radius and x <= epi_x + radius and
           y >= epi_y - radius and y <= epi_y + radius):
            color = "red"
        p.canvas.create_oval(x, y, x + 4, y + 4, outline=color)

main()