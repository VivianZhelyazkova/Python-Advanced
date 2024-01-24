def palindrome(word, index):

    last_index = len(word) - 1 - index

    if index >= last_index:
        return f"{word} is a palindrome"

    if word[index] != word[last_index]:
        return f"{word} is not a palindrome"
    else:
        return palindrome(word, index + 1)

