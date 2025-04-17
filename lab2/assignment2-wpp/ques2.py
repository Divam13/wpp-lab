products = {}

while True:
    name = input("Enter product name (or type 'done' to finish): ")
    if name.lower() == 'done':
        break
    price = input(f"Enter price for {name}: ")
    products[name] = price

while True:
    search_name = input("Enter a product name to get the price (or type 'exit' to quit): ")
    if search_name.lower() == 'exit':
        break
    if search_name in products:
        print(f"The price of {search_name} is {products[search_name]}")
    else:
        print(f"{search_name} not found in the dictionary.")
