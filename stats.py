
def get_num_words(contents):
    words = contents.split()
    num_words = 0
    for word in words:
        num_words += 1
    return num_words

def get_num_letters(contents):
    book_characters = {}

    words = contents.split()
    for word in words:
        for i in range(len(word)):
            if word[i].lower() in book_characters:
                book_characters[word[i].lower()] += 1
            else: 
                book_characters[word[i].lower()] = 1

    return book_characters


def sort_on(items):
    return items["num"]


def sort_book(contents: dict):
    book_list = []
    new_dict = {}
    for content in contents:
        new_dict["char"] = content
        new_dict["num"] = int(contents[content])
        book_list.append(new_dict)
        new_dict = {}

    book_list.sort(key=sort_on, reverse=True)
        
    return book_list


        
