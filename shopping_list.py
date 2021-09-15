shopping_list = []

def add_to_list(item):
    shopping_list.append(item)
    num_of_items = len(shopping_list)
    if num_of_items == 1:
        print("The item: '{}' has been added! There is currently {} item in the list."
            .format(item, num_of_items))
    else:
        print("The item: '{}' has been added! There are currently {} items in the list."
        .format(item, num_of_items))

def show_help():
    print("What should we pick up at the store?")
    print("""
Enter "DONE" to stop adding items.
Enter "HELP" to show help.
""")

show_help()
while True:
    new_item = str(input("==> "))
    if new_item.upper() == "DONE":
        break
    elif new_item.upper() == "HELP":
        show_help()
        continue
    else:
        add_to_list(new_item)

#final_list = shopping_list.copy()
#final_shopping_list = ", ".join(final_list)
#final_shopping_list = final_shopping_list.title()
#print(final_shopping_list)