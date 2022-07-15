def shopping_list(budget, **kwargs):
    result = ''
    if budget < 100:
        return "You do not have enough budget."
    product_type_counter = 0
    for product_name, data in kwargs.items():
        if product_type_counter == 5:
            break
        product_price, product_quantity = data
        total_price_per_product = product_price * product_quantity
        if total_price_per_product > budget:
            continue
        budget -= total_price_per_product
        product_type_counter += 1
        result += f'You bought {product_name} for {total_price_per_product:.2f} leva.' + '\n'
    return result.rstrip()




print(shopping_list(100,
                    microwave=(70, 2),
                    skirts=(15, 4),
                    coffee=(1.50, 10),
                    ))

print(shopping_list(104,
                    cola=(1.20, 2),
                    candies=(0.25, 15),
                    bread=(1.80, 1),
                    pie=(10.50, 5),
                    tomatoes=(4.20, 1),
                    milk=(2.50, 2),
                    juice=(2, 3),
                    eggs=(3, 1),
                    ))

print(shopping_list(20,
                    jeans=(19.99, 1),
                    ))