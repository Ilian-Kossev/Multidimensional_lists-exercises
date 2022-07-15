def stock_availability(flavors_list, action, *args):
    if action == 'delivery':
        for item in args:
            flavors_list.append(item)
    elif action == 'sell':
        if not args:
            flavors_list.pop(0)
            return flavors_list
        if type(args[0]) == int:
            number = args[0]
            for num in range(number):
                flavors_list.pop(0)
        elif type(args[0]) == str:
            for item in args:
                while item in flavors_list:
                    flavors_list.remove(item)
    return flavors_list


print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie","banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))


