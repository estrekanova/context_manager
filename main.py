from context_manager import TimeStamp

def file_read(file_name):
    cook_book = {}
    with open(file_name, 'rt', encoding='ansi') as recipes:
        keys_list = ['ingredient_name', 'quantity', 'measure']
        for line in recipes:
            cook_book[line.strip().title()] = []
            ingredients_count = int(recipes.readline().strip())
            while ingredients_count > 0:
                ingredient = recipes.readline().strip().split("|")
                ingredient_dict = dict(zip(keys_list, ingredient))
                cook_book[line.strip().title()].append(ingredient_dict)
                ingredients_count -= 1
            recipes.readline()
    return cook_book


def file_write(file_name, dish_name, ingredients_count, ingredients_list):
    with open(file_name, 'at', encoding='ansi') as recipes:
        recipes.write(dish_name + '\n' + str(ingredients_count) + '\n')
        for ingredient in ingredients_list:
            recipes.write(ingredient + '\n')
        recipes.write('\n')


def get_shop_list_by_dishes(dishes, person_count):
    cook_book = file_read('recipes.txt')
    result = {}
    for dish in dishes:
        if dish.strip().title() not in cook_book.keys():
            print(f'В книге рецептов нет блюда "{dish.strip().title()}"')
        else:
            for ingredient in cook_book[dish.strip().title()]:
                result_key = ingredient['ingredient_name']
                if result_key not in result.keys():
                    result[result_key] = {'measure': ingredient['measure'], 'quantity': 0}
                quantity = float(result[result_key]['quantity']) + float(ingredient['quantity']) * person_count
                result[result_key]['quantity'] = quantity
    return result


def add_recipe():
    cook_book = file_read('recipes.txt')
    dish_name = str(input("Введите название блюда:")).strip().title()
    if dish_name in cook_book.keys():
        print(f'Блюдо "{dish_name}" уже есть в книге рецептов.')
        return
    ingredients_count = int(input("Введите количество ингредиентов:"))
    ingredients_list = add_ingredient(ingredients_count)
    file_write('recipes.txt', dish_name, ingredients_count, ingredients_list)
    return


def add_ingredient(ingredients_count):
    delimiter = " | "
    ingredients_list = []
    i = 1
    while i <= ingredients_count:
        ingredient_name = str(input(f"    Введите название {i}-го ингредиента:")).strip().title()
        ingredient_count = input(f"    Введите количество {i}-го ингредиента:")
        ingredient_measure = input(f"    Введите единицу измерения {i}-го ингредиента:")
        ingredients_list.append(ingredient_name + delimiter + ingredient_count + delimiter + ingredient_measure)
        i += 1
    return ingredients_list


with TimeStamp() as ts:
    while True:
        print('Доступны следующие команды:\n r - вывести на экран список рецептов\n '
              'b - сформировать список покупок\n n - добавить новый рецепт\n e - выход из программы')
        command = input("Введите код команды: ")
        if command == 'e':
            print('Выход из программы')
            break
        elif command == 'r':
            print('Рецепты поваренной книги:')
            cook_book = file_read('recipes.txt')
            for item in cook_book:
                print(item)
                for ingredient in cook_book[item]:
                    print(ingredient)
        elif command == 'n':
            print('Добавляем новый рецепт')
            add_recipe()
        elif command == 'b':
            print('Составляем список покупок')
            dishes = input('Введите названия блюд через запятую: ')
            person_count = int(input('Введите количество гостей: '))
            dishes_list = dishes.split(',')
            buying_list = get_shop_list_by_dishes(dishes_list, person_count)
            for item in buying_list.items():
                print(item)
