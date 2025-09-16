def display_cart(cart):
    print("\nDisplaying Values")
    print("Key      Value")
    for key, value in cart.items():
        print(f"{key:<10}{value}")
    print()


def search_cart(cart):
    search = input("Enter item to search: ")

    if search.isdigit():
        key = int(search)
        value = cart.get(key)
        if value:
            print(f"Found {value} item")
        else:
            print("Im sorry, not in the cart")
    else:
        found = False
        for key, value in cart.items():
            if value.lower() == search.lower():
                print(f"Found {value} item")
                found = True
                break
        if not found:
            print("Im sorry, not in the cart")
    print()


def remove_item(cart):
    search = input("Enter key to search: ")

    if search.isdigit():
        key = int(search)
        value = cart.get(key)
        if value:
            del cart[key]
            print(f"The key {key} with value {value} has been deleted")
        else:
            print("Key not found")
    else:
        print("Key not found")
    print()


def change_item(cart):
    search = input("Enter key to search: ")

    if search.isdigit():
        key = int(search)
        value = cart.get(key)
        if value:
            print(f"Found {value} item")
            new_value = input("Enter value: ")
            cart[key] = new_value
        else:
            print("Im sorry, not in the cart")
    else:
        print("Im sorry, not in the cart")
    print()


def main():
    
    cart = {
        0: "underwear",
        1: "tank top",
        2: "jacket"
    }

    print("You have 3 items in the cart")

    while True:
        choice = input(
            "What would you like to do [C]hange items [R]emove [D]isplay  S[earch] ?  "
        ).strip().upper()

        if choice == "D":
            display_cart(cart)
        elif choice == "S":
            search_cart(cart)
        elif choice == "R":
            remove_item(cart)
        elif choice == "C":
            change_item(cart)
        elif choice == "*":
            print("Bye")
            break
        else:
            print("Invalid choice, try again.\n")

if __name__ == "__main__":
    main()