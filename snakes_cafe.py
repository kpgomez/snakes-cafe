appetizers = ["Wings", "Cookies", "Spring Rolls"]
entrees = ["Salmon", "Steak", "Meat Tornado", "A Literal Garden"]
desserts = ["Ice Cream", "Cake", "Pie"]
drinks = ["Coffee", "Tea", "Unicorn Tears"]
stars = "**"


def introborder():
    print("*"*38)

def promptborder():
    print("*"*35)

def blank():
    print()


def listappetizer():
    print("Appetizers")
    print("----------")
    for x in appetizers:
        print(x)
    blank()


def listentrees():
    print("Entrees")
    print("-------")
    for x in entrees:
        print(x)
    blank()


def listdesserts():
    print("Desserts")
    print("--------")
    for x in desserts:
        print(x)
    blank()


def listdrinks():
    print("Drinks")
    print("------")
    for x in drinks:
        print(x)
    blank()


def menu():
    listappetizer()
    listentrees()
    listdesserts()
    listdrinks()


def intro():
    introborder()
    spacing = "   "
    print(stars + spacing + "Welcome to the Snakes Cafe! " + spacing + stars)
    print(stars + spacing + "Please see our menu below.  " + spacing + stars)
    print(stars)
    print(stars + ' To quit at any time, type "quit" ' + stars)
    introborder()
    blank()


def customerprompt():
    promptborder()
    print(stars + " What would you like to order? " + stars)
    promptborder()

intro()
menu()
customerprompt()