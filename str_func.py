def title_letters(word=input("Введите слово: ")):
    """все буквы большие"""
    word_with_title = word.upper()
    return word_with_title


def super_title_letters(word=input("Введите слово: ")):
    """стартует слово с заглавной буквы"""
    title_word = word.title()
    return title_word


print(title_letters())
print(super_title_letters())
# hotfix hotfix hotfix
