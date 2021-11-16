def is_palindrome(word: str) -> bool:
    word = word.replace(' ','').lower() #Take out every space and convert to lowercase the entire string
    assert len(word) > 0 , 'Error: Cannot process empty words'
    return word == word[::-1]


def main():
    word: str = input('Write a word: ')
    if is_palindrome(word):
        print(f'{word} is a palindrome!')
    else:
        print(f'{word} is NOT a palindrome!')


if __name__ == '__main__':
    main()