from system_interaction import what_to_do
if __name__ == "__main__":
    number=-1
    while True:
        while number!=1 and number!=2 and number!=3:
            number = int(input( "type 1 if you want to create a lesson\n type 2 if you want to join to a lesson\n type 3 if you want to go back to the menu\n: "))
        if number==3:
            continue
        what_to_do(number)