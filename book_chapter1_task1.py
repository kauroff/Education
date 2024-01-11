import timeit


def is_palindrome1(word):
    word = word.replace(' ', '')
    for element in word:
        if not element.isalpha():
            word = word.replace(element, '')
    if word.lower() == word.lower()[::-1]:
        return True


def is_palindrome2(word):
    word = word.replace(' ', '')
    for element in word:
        if not element.isalpha():
            word = word.replace(element, '')
    while len(word) > 1:
        if word.lower()[0] != word.lower()[-1]:
            return False
        word = word.lower()[1:-1]
    return True



print(timeit.timeit("is_palindrome1('Я не стар, брат Сеня!')", setup="from __main__ import is_palindrome1"))
print(timeit.timeit("is_palindrome2('Я не стар, брат Сеня!')", setup="from __main__ import is_palindrome2"))
