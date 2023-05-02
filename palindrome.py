def input_word():
    word = input("문자열을 입력하시오 : ")
    return word

def check_palindrome(word):
    if word == word[::-1]:
        print('회문입니다')
    else:
        print('회문이 아닙니다')

if __name__ == '__main__':
    word = input_word()
    check_palindrome(word)