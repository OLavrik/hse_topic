import itertools
import re
import sys

import spacy
from nltk.stem import WordNetLemmatizer



# TODO: logger required
#   from util.logging.init_logger import logger

SEPARATOR = '~'
no_lemma = ["os", "pass", "logos", "es", "takings"]
nlp = spacy.load("en_core_web_sm")
lemmatizer = WordNetLemmatizer()
lemmatizer.lemmatize("start")

currentFuncName = lambda n=0: sys._getframe(n + 1).f_code.co_name


def normalize(tokens):
    res = []
    for curr_token in tokens:
        if curr_token not in no_lemma:
            try:
                curr_token = lemmatizer.lemmatize(curr_token)
            except Exception as e:
                raise e

        res += [curr_token]
    return res


def separate_token(initial_scope):
    regex_pipeline = [r'(?<=[A-Za-z])(?=[A-Z][a-z])', r'[^\w\s]', r'[_\-]']

    for reg in regex_pipeline:
        initial_scope = re.sub(reg, SEPARATOR, initial_scope)

    initial_scope = re.split(SEPARATOR, initial_scope)

    result = []
    for elem in filter(None, initial_scope):
        prev = elem[-1].isupper()
        for i in range(len(elem) - 2, 0, -1):
            next_elem = elem[i].isupper()
            if prev ^ next_elem:
                elem = '~'.join((elem[:i + int(prev)], elem[i + int(prev):]))
                prev = next_elem

        result.extend(itertools.chain(*[re.split(r'(\d+)', _) for _ in re.split('~', elem)]))

    return normalize([elem.lower() for elem in result])


if __name__ == "__main__":
    print(separate_token("AAACats43aAAA"))
    print("['aaa', 'cat', '43', 'aaa']")
