from collections import OrderedDict
import csv

def display_inventory(inventory):
    print("Inventory:")
    for key, value in inventory.items():
        print(value, key)
    print("Total number of items: {}\n".format(sum(inventory.values())))

def add_to_inventory(inventory, added_items):
    new_items = list(set(added_items) - set(inventory)) #keys the inventory did not contain
    for new in new_items:
        inventory[new] = 0
    for item in added_items:
        for key, value in inventory.items():
            if item == key:
                inventory[key] = value + 1
    return inventory

def print_table(order = None):
    global inv
    max_value = max([len(str(v)) for v in inv.values()]) #length of longest value
    max_key = max([len(str(k)) for k in inv.keys()]) #length of longest key
    
    print("Inventory:")
    print("count".rjust(5 + max_value), "item name".rjust(5 + max_key))
    print("-" *(11 + max_value + max_key))

    if order == "count,desc":
        sorted_inventory = OrderedDict(sorted(inv.items(), key=lambda x: x[1], reverse=True))
    elif order == "count,asc":
        sorted_inventory = OrderedDict(sorted(inv.items(), key=lambda x: x[1], reverse=False))
    else:
        sorted_inventory = inv #unsorted
    for key, value in sorted_inventory.items():
        print(str(value).rjust(5 + max_value), str(key).rjust(5 + max_key))
        
    print("-" *(11 + max_value + max_key))
    print("Total number of items: {}\n".format(sum(inv.values())))

def import_inventory(filename):
    global inv
    imp_inv = open(filename, 'r')
    imp_inv.readline() #skip first line
    reader = csv.reader(imp_inv)
    dictionary = {}

    for row in reader:
        key, value = row
        dictionary[key] = int(value) 
    for key, value in dictionary.items():
        if key in inv.keys():
            inv[key] += value
        else:
            inv[key] = 1

def export_inventory(filename):
    global inv
    with open(filename, 'w') as csvfile:  
        w = csv.DictWriter(csvfile, fieldnames = ["item_name", "count"])
        w.writeheader()
        for key, values in inv.items():
            w.writerow({"item_name": key, "count": values})


inv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12} 
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

display_inventory(inv)

inv = add_to_inventory(inv, dragon_loot)

display_inventory(inv)

print_table("count,desc")

import_inventory("import_inventory.csv")

display_inventory(inv)

export_inventory("export_inventory.csv")
