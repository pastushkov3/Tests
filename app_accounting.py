documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
      ]
directories = {
      '1': ['2207 876234', '11-2', '5455 028765'],
      '2': ['10006'],
      '3': []
    }


# p – people – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит;
def number_passport_name():
  number = input("Введите номер документа: ")
  for value in documents:
    if value["number"] == number:
      print(f'\nВладелец документа - {value["name"]} \n')
      break
  else:
    print("Такого документа нет! Посмотри список, введя команду l")


# s – shelf – команда, которая спросит номер документа и выведет номер полки, на которой он находится;
def number_shelf():
  pool_active = True
  while pool_active:
    number_doc = input("\nВведите номер документа / q - для выхода: ")
    if number_doc == "q":
      pool_active = False
      break
    for shelf, value in directories.items():
      if number_doc in value:
        print(f'\nДокумент на полке {shelf}')
        repeat = input("\nХотите поискать другой? (y/n): ")
        if repeat == "n":
          pool_active = False
          break
        elif repeat == "y":
          break
    else:
      print("\nТакого документа нет!")


# l– list – команда, которая выведет список всех документов в формате passport "2207 876234" "Василий Гупкин";
def list_doc():
  for doc in documents:
    print(*doc.values())
  return


# a – add – команда, которая добавит новый документ в каталог и в перечень полок, спросив его номер, тип, имя владельца и номер полки, на котором он будет храниться.
def add_doc():
  pooling_active = True
  while pooling_active:
    type_doc = input("Тип документа: ")
    number_doc = input("Номер документа: ")
    name_doc = input("Имя владельца: ")
    shelf = input("Введите номер полки: ")
    if shelf in directories:
      directories[shelf].append(number_doc)
    else:
      print(f'\nМы построили полку {shelf}, т.к. у нас ее не было.')
      directories[shelf] = number_doc
    new_doc = dict(type = type_doc, number = number_doc, name = name_doc)
    documents.append(new_doc)
    repeat = input("\nДокумент добавлен!\nХотите добавить еще? (y/n): ")
    if repeat == "n":
      pooling_active = False


def main():
  while True:
    print('\nСписок команд: \n1 - поиск по номеру документа')
    command = input("Введите команду: ")
    if command == "p":
      number_passport_name()
    elif command == "s":
      number_shelf()
    elif command == "l":
      list_doc()
    elif command == "a":
      add_doc()
main()