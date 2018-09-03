checklist = list()

def fun_function(str):
    print(str)

# create
def create(string):
    checklist.append(string)

# read
def read(index):
    return checklist[int(index)]

#update
def update(index, string):
    checklist[index] = string

#delete
def delete(index):
    checklist.pop(index)

def list_all_items():
    index = 0
    for list_item in checklist:
        print("{} {}".format(index, list_item))
        index +=1

def mark_completed(index):
    update(index, "{}{}".format(":)",checklist[index]))

def select(function_code):
    # Create item
    if function_code == "C":
        input_item = user_input("Input item:")
        create(input_item)

    # Read item
    elif function_code == "R":
        item_index = user_input("Index Number?")

        # Remember that item_index must actually exist or our program will crash.
        read(item_index)

    # Print all items
    elif function_code == "P":
        list_all_items()

    elif function_code == "Q":
        return False

    # Catch all
    else:
        print("Unknown Option")
    return True

def user_input(prompt):
    # the input function will display a message in the terminal
    # and wait for user input.
    user_input = input(prompt)
    return user_input


running = True
while running:
    selection = user_input("Press C to add to list, R to Read from list and P to display list")
    running = select(selection)
