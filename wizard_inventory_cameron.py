#usr/bin/env python3

#Wizard Invetory



#Menu
def displayMenu():
    print ("The Wizard Inventory program")
    print ("\nCOMMAND MENU")
    print ("show - Show all items")
    print ("grab - Grab an item")
    print ("edit - Edit an item")
    print ("drop - Drop an item")
    print ("exit - exit program")
    print()

#Items/ used to show,grab,edit,drop
inventory = ["wooden staff", "wizard hat", "cloth shoes"]

#Showing what's in *invetory*
def show(inventory):
    y = 0
    for x in inventory:
        y = y +1
        print (str(y) + "." , x)

#Retreiving invetory
def grab(inventory):
    if len(inventory) < 4:
        grab = str(input("Name: "))
        inventory.append(grab)
        print(grab, "was added")
    else:
         print ("You can't carry any more items. Drop something first.")
    

#Changing items in invetory
def edit(inventory):
    editor = int(input("Number: "))
    if editor <= len(inventory) and editor >= 1:
        update = str(input("Updated name: "))
        inventory[editor -1 ] = update
        print ("item number", editor, "was updated")
    else:
        print("Not a valid item")


#deleting/dropping invetory
def drop(inventory):
    garbage = int(input("Number: "))
    if garbage < 1 or garbage > len(inventory):
        garbage = garbage -1
        print(inventory[garbage], "was dropped")
        inventory.remove(inventory,garbage)
    else:
        print("Not a valid item")


#Main/Makes the magic happen
#Display~
def main():
    print ("The Wizard Inventory program")
    print ("\nCOMMAND MENU")
    print ("show - Show all items")
    print ("grab - Grab an item")
    print ("edit - Edit an item")
    print ("drop - Drop an item")
    print ("exit - exit program")
    print()
    
#While a command = whatever is typed it carries out the command
    command = ""
    while command != "exit":
        if command.lower() == "show":
            show(inventory)
        elif command.lower() == "grab":
            grab(inventory)
        elif command.lower() == "edit":
            edit(inventory)
        elif command.lower() == "drop":
            drop(inventory)
        command = str(input ("\nCommand: "))
    print ("Bye!")




if __name__ == "__main__":
    main()
