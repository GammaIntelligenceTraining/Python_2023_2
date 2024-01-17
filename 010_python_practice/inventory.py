# Inventory management app
# inventory => Product - name(key), {quantity, price}(value)
# FUNCTIONS:
# add item DONE
# remove item DONE
# update price DONE
# sell item DONE
# display inventory
# calculate total value

inventory = {'Apple': {'quantity': 7, 'price': 0.5}, 'Orange': {'quantity': 10, 'price': 0.7}}
def add_product(name, quantity, price):
    if name in inventory:
        print(f'{quantity} {name}s were added')
        inventory[name]['quantity'] += quantity
    else:
        inventory[name] = {'quantity': quantity, 'price': price}
        print(f'{name}s were added to inventory')


def remove_product(name):
    if name in inventory:
        del inventory[name]
        print(f'{name} was deleted')
    else:
        print(f'{name} is not in inventory')


def update_price(name, price):
    if name in inventory:
        inventory[name]['price'] = price
        print(f'Price for {name} updated to ${price:.2f}')
    else:
        print(f'{name} is not in inventory')


def sell_product(name, quantity):
    if name in inventory:
        if inventory[name]['quantity'] >= quantity:
            inventory[name]['quantity'] -= quantity
            total_price = inventory[name]['price'] * quantity
            print(f'{quantity} {name}s sold. Total: ${total_price:.2f}')
        else:
            print(f'Not enough {name}s in stock. There are only {inventory[name]["quantity"]} {name}s left!.')
    else:
        print(f'{name} is not in inventory')


def display_inventory():
    # for product in inventory:
    #     print(f'{product} - qty: {inventory[product]["quantity"]}, price: ${inventory[product]["price"]:.2f}')
    for product, data in inventory.items():
        print(f'{product} - qty: {data["quantity"]}, price: ${data["price"]:.2f}')


def calculate_total_value():
    total_value = 0
    for data in inventory.values():
        total_value += data["quantity"] * data["price"]
    print(f'Total cost of inventory is ${total_value:.2f}')

# calculate_total_value()

# sell_product('Pear', 5)
# display_inventory()
# print(inventory)

# 'Apple - qty: 7, price: $0.50'