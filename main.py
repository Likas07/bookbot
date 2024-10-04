def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    chars_dict_list = get_chars_dict_list(chars_dict)
    sorted_chars_dict_list = sorted(chars_dict_list, key=sort_on, reverse=True)
    
    print(f'-------------------------Report of {book_path}-------------------------')
    print(f'there are {num_words} words in the text') 
    print(f'there are {len(chars_dict)} unique characters in the text') 
    
    for char_dict in sorted_chars_dict_list:
        if char_dict['letter:'].isalpha()==True:
            print(f'{char_dict["letter:"]} appears {char_dict["count"]} times')
    
    print('-------------------------End of Report-------------------------')
        

def get_num_words(text):
    words = text.split()
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

def get_chars_dict_list(chars_dict):
    return [{'letter:': c, 'count': chars_dict[c]} for c in chars_dict]

def get_book_text(path):
    with open(path) as f:
        return f.read()

def sort_on(dict):
    return dict['count']



main()