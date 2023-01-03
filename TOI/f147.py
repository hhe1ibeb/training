combo = ["Medium Wac", "WChicken Nugget", "Geez Burger",
         "ButtMilk Crispy Chicken", "Plastic Toy"]
combo_price = [4, 8, 7, 6, 3]
single = ["German Fries", "Durian Slices", "WcFurry", "Chocolate Sunday"]
single_price = [2, 3, 5, 7]

total = 0
command = int(input())
while command != 0:
    n = int(input())
    if command == 1:
        n -= 1
        print(combo[n], combo_price[n])
        total += combo_price[n]
    else:
        n -= 1
        print(single[n], single_price[n])
        total += single_price[n]
    command = int(input())
print('Total: %d' % total)
