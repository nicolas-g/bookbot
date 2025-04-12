def get_num_words(strings):
    words = strings.split()
    return len(words)


def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


def get_sorted_dict(unsorted_dict):
    char_list = []
    for char, count in unsorted_dict.items():
        if char.isalpha():
            char_dict = {"char": char, "count": count}
            char_list.append(char_dict)
    return char_list
