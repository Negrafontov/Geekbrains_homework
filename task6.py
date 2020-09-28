goods = []
goods_count = input('Укажите количество товаров, используйте только числа')
while goods_count.isdigit() is False:
    goods_count = input('Пожалуйста, введите целое натуральное число')
count = 1
while count <= int(goods_count):
    name = input('Введите наименование товара')
    price = input('Введите значение цены товара')
    amount = input('Введите значение количества товара в единицах')
    goods_dict = {'Наименование': name, 'Цена': int(price), 'Количество': int(amount)}
    goods.append((count, goods_dict))
    count += 1
print(goods)
count = 1
name_list = []
price_list = []
amount_list = []
while count <= int(goods_count):
    name_getting1 = goods[count - 1]
    name_getting2 = name_getting1[1]
    name_getting3 = name_getting2.get('Наименование')
    name_list.append(name_getting3)
    price_getting1 = goods[count - 1]
    price_getting2 = price_getting1[1]
    price_getting3 = price_getting2.get('Цена')
    price_list.append(price_getting3)
    amount_getting1 = goods[count - 1]
    amount_getting2 = amount_getting1[1]
    amount_getting3 = amount_getting2.get('Количество')
    amount_list.append(amount_getting3)
    count += 1
goods_analytics = {'Наименование': name_list, 'Цена': price_list, 'Количество': amount_list}
print(goods_analytics)