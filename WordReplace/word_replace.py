def replace_word():
    str = "hi guys, I am hao, and hi hi hi"
    print(str)
    word_to_replace = input("Enter the word you want to replace: ")
    word_replacement = input("Enter the word replacement: ")
    print(str.replace(word_to_replace, word_replacement))


if __name__ == "__main__":
    replace_word()
