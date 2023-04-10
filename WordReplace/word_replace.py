def replace_word():
    str = "hi guys, I am hao, and hi hi hi"
    print(str)
    word_to_replace = input("Enter the word you want to replace: ")
    if not word_to_replace:
        raise ValueError("Word To Replace cannot be empty")
    word_replacement = input("Enter the word replacement: ")
    if not word_replacement:
        raise ValueError("Word Replacement cannot be empty")

    replaced_string = str.replace(word_to_replace, word_replacement)
    print(replaced_string)
    return replaced_string


if __name__ == "__main__":
    replace_word()
