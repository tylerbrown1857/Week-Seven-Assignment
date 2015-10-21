# Framework for Conway's game of life
# Tyler Brown
# CIS 125 FA2104

# Functions
# populate()
# display()
# generation()
# main()

#Function populate
#preconditions
#   random is imported
#   world is created as list
#   height is defined (as integer)
#   width is defined (as integer)
#postcondition
#   world is populated with ?? (string)


def populate(petri_dish, h=80, w=22):
    import random
    for x in range(h):
            row = []
            for y in range(w):
                    row.append(0)
            petri_dish.append(row)
            
def rPopulate(petri_dish, h=80, w=22):
    import random
    for x in range(h):
            row = []
            for y in range(w):
                    row.append(random.randint(0, 1))
            petri_dish.append(row)

# Function display(world,h,w)
# Preconditions
#   world is populated
# Postcondition
#   world is not changed


def display(world, h = 22, w = 80):
    worldstring = ""
    for x in range(h):
        for y in range(w):
            if world[x][y] == 1:
                worldstring += "*"
            else:
                worldstring += "-"
        worldstring += '\n'
    print(worldstring)


# Function generation(world,h,w)
# Preconditions
#   world is populated
# Postconditions
#   Returns new world


def generation(petri_dish, h=22, w=80):
    new_world = []
    populate(new_world, h, w)
    
    n = 0    
    for x in range(1,h-1):
        for y in range(1,w-1):
            n = 0
            n = petri_dish[x-1][y-1] +  \
                petri_dish[x-1][y] +  \
                petri_dish[x-1][y+1] +  \
                petri_dish[x][y-1] +  \
                petri_dish[x][y+1] +  \
                petri_dish[x+1][y-1] +  \
                petri_dish[x+1][y] +  \
                petri_dish[x+1][y+1]

            
            if petri_dish[x][y] == 0:
                if n == 3:
                    new_world[x][y] = 1
                else:
                    new_world[x][y] = 0
            else: #(cell is alive)
                if n < 2 or n > 3:
                    new_world[x][y] = 0
                else:
                    new_world[x][y] = 1
    # print(petri_dish)
    # print("\n")
    # print(new_world)
    # print("\n")
    petri_dish[:] = new_world
    # print(petri_dish)


def main():
    world = []
    height = 22
    width = 80
    rPopulate(world, height, width)
    display(world, height, width)
    key = raw_input("Press q to quit, any other key to continue: ")
    while (key != 'q'):
        generation(world, height, width)
        display(world, height, width)
        key = raw_input("Press q to quit, any other key to continue: ")

    print("Goodbye")


if __name__ == "__main__":
    main()
