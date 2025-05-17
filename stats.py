def n_words(text):
    words = text.split()
    return len(words)

def get_chars_dict(text):
    chars = {}
    for char in text.lower():
        if char.isalpha():
            if char in chars:
                chars[char] += 1
            else: 
                chars[char] = 1
    return chars

def sort_dict(chars_dict):
    return sorted(chars_dict.items(), key=lambda item: item[1], reverse=True)