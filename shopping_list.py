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