appetizers = ["Wings", "Cookies", "Spring Rolls"]
entrees = ["Salmon", "Steak", "Meat Tornado", "A Literal Garden"]
desserts = ["Ice Cream", "Cake", "Pie"]
drinks = ["Coffee", "Tea", "Unicorn Tears"]
stars = "**"
order = {}


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
    response = input("** What would you like to order? **\n")
    #promptborder()

    while response != "quit":
        if response in order.keys():
            order.update({response: int(order[response]+1)})
        else:
            order.update({response: 1})
        print(f"** An order of {response} has been added to your meal **")
        response = input("What would you like to order? ** \n")
    else:
        if len(order) > 0:
            print(f"Your order includes {order.items()}")


intro()
menu()
customerprompt()