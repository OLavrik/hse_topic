from process.sentense_prepare import TextPrepare
from utils.file_methods import get_dataset
from contextualized_topic_models.models.ctm import ZeroShotTM
from contextualized_topic_models.utils.data_preparation import TopicModelDataPreparation


def prepare_dataset(path="pycharm_issues.json", lemma=True):
    text_prepare = TextPrepare()
    data = [elem["summary"] for elem in get_dataset(path)]
    clear_data = [text_prepare.main_prepare_query(elem,lemma=True) for elem in data]
    vocab = text_prepare.get_vocab()
    topic_model = TopicModelDataPreparation("paraphrase-distilroberta-base-v2")
    train_dataset = topic_model.fit(text_for_contextual=data, text_for_bow=clear_data)
    return train_dataset, clear_data, topic_model
