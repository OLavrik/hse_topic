import enchant

english_vocab = enchant.Dict("en_US")
only_eng=['comparator', 'nano', 'yes', 'no']

def is_english_word(word, res=[]):
    only_eng.extend(res)
    try:
        if word in only_eng:
            return True
        if len(word.split(" ")) > 1:
            for elem in word.split(" "):
                if not english_vocab.check(elem):
                    return False
            return True
        return english_vocab.check(word)
    except:
        False