# Создать произвольный список из 8 элементов, проверить что длина списка равна 8 элементам
def test_list_length(function_hm_fixture, module_hm_fixture, session_hm_fixture):
    any_list = [x for x in range(8)]

    assert len(any_list) == 8


# Сложить две строки, проверить что полученный результат соответствует ожидаемому
def test_two_strings_plus(function_hm_fixture, module_hm_fixture):
    first_string = "App"
    second_string = "le"
    result_string = first_string + second_string
    assert result_string == "Apple", "Error is raised in test"

# Создать словарь, проверить, что под ключом имя передана строка
def test_dict_value(function_hm_fixture):
    dict = {"name": "Olga", "year": 1987}
    assert type(dict["name"]) == str, "Type of 'name' is not string"

# Проверить, что input не равен NULL
def test_input(function_hm_fixture):
    print("Введите любое значение")
    your_word = input()
    assert your_word != "", "The word wasn't inserted"


# Создать input, проверить, что слово читается одинаково в перевернутом виде
def test_reverse_word(function_hm_fixture):
    print("Введите любое слово")
    input_word = input()
    assert input_word[::-1] == input_word, "The word can't be read vise or verse"