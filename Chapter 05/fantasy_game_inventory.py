# This code displays game inventory

stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def display_inventory(inventory):
    print('Inventory:')
    item_total = 0
    for x, y in inventory.items():
        item_total += inventory[x]
        print(f"{inventory[x]} {x}") 
    print(f"Total number of items: {item_total}")

display_inventory(stuff)
