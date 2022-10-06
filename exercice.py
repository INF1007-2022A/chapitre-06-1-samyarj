#!/usr/bin/env python
# -*- coding: utf-8 -*-


def order(values: list = None) -> list:
    if values is None:
        # TODO: demander les valeurs ici
        values = [input('enter value:') for i in range(10)]

    return sorted(values)


def anagrams(word1, word2) -> bool:
    list1 = [letter for letter in word1].sort()
    list2 = [letter for letter in word2].sort()
    if list1 == list2:
        return True
    else:
        return False


def contains_doubles(items: list) -> bool:
    set1 = {item for item in items}
    list1 = [item for item in items]
    if len(set1) == len(list1):
        return False  # same items in set1, list1
    return True


def best_grades(student_grades: dict) -> dict:
    # TODO: Retourner un dictionnaire contenant le nom de l'étudiant ayant la meilleure moyenne ainsi que sa moyenne
    '''avg = [[sum(student_grades[student])/len(student_grades[student])] for student in student_grades]
    best = avg.index(max(avg))
    list1 = [[student] for student in student_grades]
    return list1[best]'''
    pass


def frequence(sentence: str) -> dict:
    # TODO: Afficher les lettres les plus fréquentes
    #       Retourner le tableau de lettres
    list_of_letters = [letter for letter in sentence if ord(letter.lower()) in range(97, 123)]
    dict = {}
    for letter in list_of_letters:
        p = 0  # value
        for other_letter in list_of_letters:
            if letter == other_letter:
                p += 1
        dict[letter] = p
    new_dict = {}
    for key in dict:
        if dict[key] > 5:
            new_dict[key] = dict[key]
    return new_dict


def get_recipes() -> dict:
    # TODO: Demander le nom d'une recette, puis ses ingredients et enregistrer dans une structure de données
    recipe_dict = dict()  # return variable
    name_key = input('Enter name of recipe: ')
    ingredients_values = input('Enter ingredients: ')
    recipe_dict[name_key] = ingredients_values.split(', ')

    return recipe_dict


def print_recipe(ingredients) -> None:
    # TODO: Demander le nom d'une recette, puis l'afficher si elle existe

    pass


def main() -> None:
    print(f"On essaie d'ordonner les valeurs...")
    #print(order())

    print(f"On vérifie les anagrammes...")
    print(anagrams('ALEVIN', 'NIVELA'))

    my_list = [3, 3, 5, 6, 1, 1]
    print(f"Ma liste contient-elle des doublons? {contains_doubles(my_list)}")

    grades = {"Bob": [90, 65, 20], "Alice": [85, 75, 83]}
    best_student = best_grades(grades)
    #print(f"{list(best_student.keys())[0]} a la meilleure moyenne: {list(best_student.values())[0]}")

    sentence = "bonjour, je suis une phrase. je suis compose de beaucoup de lettre. oui oui"
    print(frequence(sentence))

    print("On enregistre les recettes...")
    recipes = get_recipes()

    print("On affiche une recette au choix...")
    print_recipe(recipes)


if __name__ == '__main__':
    main()
