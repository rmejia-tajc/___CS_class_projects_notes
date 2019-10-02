class TodoList:
    def __init__(self, name):
        self.name = name
        self.items = []

    def __str__(self):
        return f"{self.name}: {self.items}"

    def __repr__(self):
        return f"TodoList({repr(self.name)})"

quit = False

all_list = []

current_list = None

while not quit:

    command = input(f"\n(C)reate new list\n(s)elect a list ({current_list})\n(A)dd item\n(Q)uit\n\nCommand: ")

    command = command.lower().strip()  # normalizing input. inputs can be upper and lowercase. strips all empty spacing. (e.g. Quit, quits, etc)

    if command == "":
        continue

    command = command[0] # only accepts first letter (e.i. q in Quit)

    if command == "q": # quit
        quit = True
    elif command =="c": # create
        name = input("Enter list name: ").strip()

        new_list = TodoList(name)
        all_list.append(new_list)

        print(all_list)

    elif command == "s": # select list
        name = input("Enter list name: ").strip()

        named_list = None

        for l in all_list:
            if l.name == name:
                named_list = l
                break # get out of for loop

        if named_list is None:
            print(f"No such list named {name}")

        else:
            current_list = named_list

            # current_room = room[current_room].n_to # something like this in the adv game

    elif command == "a": # add
        if current_list is None:
            print("\n** No list selected!")

        else:
            item_name = input("Enter item: ").strip()

            current_list.items.append(item_name)

            print(f">>> {named_list}")

# tl = TodoList("List 1")

# tl.items.append("get milk")
# tl.items.append("go mountain biking")
# print(tl)