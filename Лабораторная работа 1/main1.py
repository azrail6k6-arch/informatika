list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

middle_index = len(list_players) // 2 # Находим сколько человек должно быть в каждой команде.

first_team = list_players[:middle_index] # При помощи слайсирования определяем игроков первой команды.
second_team = list_players[middle_index:] # При помощи слайсирования определяем игроков второй команды.

print(first_team) #Выводим имена игроков первой команды.
print(second_team) #Выводим имена игроков второй команды.
