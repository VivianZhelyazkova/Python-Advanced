def words_sorting(*args):
    words = {}
    result = ""
    for word in args:
        words[word] = sum(ord(letter) for letter in word)

    if sum(words.values()) % 2 != 0:
        sorted_words = dict(sorted(words.items(), key=lambda x: x[1], reverse=True))
    else:
        sorted_words = dict(sorted(words.items(), key=lambda x: x[0]))
    for word, number in sorted_words.items():
        result += f"{word} - {number}\n"
    return result
