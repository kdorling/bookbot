def get_sorted_list_of_dicts(dictionary):
    dictionaries = []
    for character in dictionary:
        dictionaries.append({"char": character, "num": dictionary[character]})

    def sort_on(item):
        return item["num"]

    dictionaries.sort(reverse=True, key=sort_on)
    return dictionaries


def get_character_counts(text):
    character_counts = {}
    for char in text.lower():
        if char in character_counts:
            character_counts[char] += 1
        else:
            character_counts[char] = 1
    return character_counts


def get_num_words(text):
    words = text.split()
    return len(words)
