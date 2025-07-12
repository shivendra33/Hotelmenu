menu = {
    'pizza':40,
    'pasta':50,
    'burger':60,
    'salad':30,
    'coffee':80,
}
print(menu)
'''#greet'''
print("welcome to btech wala restaurant")
print("pizza: Rs40\n pasta:Rs 50\n burger: Rs60\n salad:Rs30\n coffee: Rs80")

order_total = 0

'''#order from customer'''
item_1 = input("Enter the name of item you want to order =")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item {item_1} has beemn added to your order")

else:
    print(f"ordered item {item_1} is not available yet!")

another_order =  input("Do you want another item? (Yes/No) ")
if another_order == "Yes":
    item_2 = input("Enter the name of second item = ")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Item {item_2} has been added to order")
    else:
        print(f"order item {item_2} is not available!")

print(f"The total amount of items to pay is {order_total}") 