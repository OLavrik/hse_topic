from contextualized_topic_models.models.ctm import ZeroShotTM
import pickle


class ModelCTM:
    def __init__(self, topic_model, size, n_tp, epochs):
        if not topic_model == None:
            self.model = ZeroShotTM(
                bow_size=len(topic_model.vocab), contextual_size=size, n_components=n_tp, num_epochs=epochs
            )

    def fit(self, train_data):
        self.model.fit(train_data)

    def save_model(self, path):
        with open(path, "wb") as f:
            pickle.dump(self.model, f)

    def load_model(self, path):
        with open(path, "rb") as f:
            self.model = pickle.load(f)

    def topic(self):
        return self.model.get_topics()

    def cloud(self, topic_id=1, n_words=10):
        self.model.get_wordcloud(topic_id=topic_id, n_words=n_words)

    def predict_topic(self, id_, n):
        return self.model.get_thetas(id_, n=n)
