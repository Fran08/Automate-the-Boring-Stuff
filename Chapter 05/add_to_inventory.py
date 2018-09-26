# This code adds on to the other project in Chapter 5
# We are adding a list of loot to our inventory

def display_inventory(inventory):
    print('Inventory:')
    item_total = 0
    for x, y in inventory.items():
        item_total += inventory[x]
        print(f"{inventory[x]} {x}")
    print(f"Total number of items: {item_total}\n")
    

def add_to_inventory(inventory, added_items):
    for item in added_items:
        inventory.setdefault(item, 0)
        inventory[item] += 1
    return inventory


inv = {'gold coin': 42, 'rope': 1}
display_inventory(inv)
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = add_to_inventory(inv, dragon_loot)
display_inventory(inv)
