from main import MENU, resources

stock = resources

p = 0.01
d = 0.10
n = 0.05
q = 0.25

quit = "yes"
flag = 0
price = 0


def quantity(drink):
    for i in MENU[str(drink)]["ingredients"]:
        if MENU[str(drink)]["ingredients"][str(i)] > resources[i]:
            flag = 1
            return flag
           # return f"you dont have enough resources for {drink}. sorry"
        else:
            #resources[i] = int(resources[i]) - int(MENU[str(drink)]["ingredients"][i])
            flag = 2
            return flag

def upgrade_resources(drink):
    for i in MENU[str(drink)]["ingredients"]:
        resources[i] = int(resources[i]) - int(MENU[str(drink)]["ingredients"][i])


def money(drink):
    global price
    global quit
    flag = quantity(drink)
    if flag == 2:
        print("Please insert coins:")
        penny = int(input("how many p: "))
        dime = int(input("how many d: "))
        nickel = int(input("how many n: "))
        quarter = int(input("how many q: "))

        total = penny * p + dime * d + nickel * n + quarter * q
        rate = float(MENU[str(drink)]["cost"])
        if total == rate:
            price += rate
            upgrade_resources(drink)
            return f"here is your {drink}"
        elif total > rate:
            price += rate
            upgrade_resources(drink)
            return f"here is your {drink} & your change: ${total-rate}"
        else:
            quit = "no"
            return f"you dont have enough money to buy {drink}"
    elif flag == 1:
        quit = "no"
        print(f"Machine out of resources for {drink}")


while quit != "no":
    ask = input("What yould you like? E, L, C: ")

    if ask == "report":
        for i in stock:
            print(i, stock[i])
        print(price)
    else:
        print(f"This {ask} will cost you {MENU[str(ask)]['cost']}")
        print(money(ask))

