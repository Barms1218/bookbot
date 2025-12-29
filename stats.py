def get_word_count(text):
    words = text.split()
    return len(words)

def get_letter_count(text):
    char_dict = {}
    for char in text:
        lowered = char.lower()
        if lowered in char_dict:
            char_dict[lowered] += 1
        else:
            char_dict[lowered] = 1
    return char_dict

def sort_letters(text):
    char_dict = get_letter_count(text)
    return sorted(char_dict.items())
    

def get_nums_from_dict(dictionary):
    nums = []
    for char, count in dictionary:
        nums.append(count)
    return sorted(nums)

def get_chars_from_dict(dictionary):
    chars = []
    for char in dictionary:
        chars.append(char)
    return sorted(chars)