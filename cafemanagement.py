menu = {"idly" : 30,
        "dosa" :40,
        "parota":50,
        "egg-dosa":45}
# printing menu
print("  items          price(in rupees)")
print("-"*32)
index = 1
for i,j in menu.items():
    print(f"{index}.{i:<20}{j}")
    index = index+1
#dict of order and quantity
order={}
while True:
    get_order = input("Enter the item : ").lower()
    if get_order not in menu:
        print("Not in the menu")
    else:    
        get_quantity = int(input("Enter the quantity: "))
        order[get_order] = get_quantity
        continue_order = input("Do you want to order anything else(y/n): ").lower()
        if continue_order == 'y':
            continue
        else:
            break

print("Your order")
print("items          quantity   cost(in rupee)")
print("-"*35)
total = 0
for i,j in order.items():
    print(f"{i:<20}{j:<10}{menu[i]*j}")
    total = total + menu[i]*j
print(" "*25,"Total =",total)