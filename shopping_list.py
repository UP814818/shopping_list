shopping_list = []

def show_help():
    print("What should we pick up at the store?")
    print("""
To add an item. Enter what you need after the '==>' sign.
Enter "HELP" to show help.
Enter "SHOW" to see your current list
Enter "DONE" to stop adding items.
""")


def add_to_list(item):
    shopping_list.append(item)
    num_of_items = len(shopping_list)
    if num_of_items == 1:
        print("The item: '{}' has been added! There is currently {} item in the list."
            .format(item, num_of_items))
    else:
        print("The item: '{}' has been added! There are currently {} items in the list."
        .format(item, num_of_items))


def show_list():
    current_list = shopping_list.copy()
    current_shopping_list = ", ".join(current_list)
    current_shopping_list = current_shopping_list.title()
    print("Here's your list: {}".format(current_shopping_list))


show_help()
while True:
    new_item = str(input("==> "))
    if new_item.upper() == "DONE":
        break
    elif new_item.upper() == "HELP":
        show_help()
        continue
    elif new_item.upper() == "SHOW":
        show_list()
        continue
    else:
        add_to_list(new_item)

final_list = shopping_list.copy()
final_shopping_list = ", ".join(final_list)
final_shopping_list = final_shopping_list.title()
print("Here's your completed list:",final_shopping_list)