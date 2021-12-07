import itertools
import re
from utils.eng import is_english_word
import nltk
from nltk.corpus import stopwords

from process.normalization import normalize, separate_token


# Good website for lemmantization: https://cst.dk/tools/index.php#output

class TextPrepare():
    regular_language = r'\#.*?\s'
    english_stopwords = stopwords.words("english")
    porter = nltk.PorterStemmer()
    vocab = []

    def main_prepare_query(self, query, lemma=True, english=False):
        query = re.sub(r' +', " ", query)
        query = self.separate_query(query)
        tokens = query.split(" ")
        if lemma:
            tokens = normalize(tokens)
        tokens = self.remove_stop_words(tokens)
        if english:
            res=[]
            for _ in tokens:
                if is_english_word(_):
                    res.append(_)
            tokens=res
        self.vocab.extend(tokens)
        self.vocab = list(set(self.vocab))
        return " ".join(tokens).strip()

    def get_vocab(self):
        return self.vocab

    def remove_stop_words(self, tokens):
        return [elem for elem in tokens if elem not in self.english_stopwords]

    def nouns_and_verbs(self, query):
        not_important = ["IN", "PP", "RP"]
        tokens = self.remove_stop_words(query.split(" "))
        pos_tagged = nltk.pos_tag(tokens)
        return " ".join([elem[0] for elem in pos_tagged if elem[1] not in not_important]).strip()

    @staticmethod
    def separate_query(query):
        tokens_separated = list(itertools.chain(*map(lambda name: separate_token(name), query.split(" "))))
        return " ".join(tokens_separated).strip()


if __name__ == "__main__":
    print(TextPrepare.separate_query("AAAnnnA A"))
