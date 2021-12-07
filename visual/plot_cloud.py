from collections import Counter

import nltk
import numpy as np
import plotly.express as px
from wordcloud import WordCloud

nltk.download("stopwords")

def get_word_cloud_plot_freq(documents):
    keywords_list = []

    for doc in documents:
        keywords_list.extend(doc.split(" "))

    keywords = Counter(keywords_list)
    print(keywords.most_common(100))
    x, y = np.ogrid[:1200, :1200]

    mask = (x - 600) ** 2 + (y - 600) ** 2 > 590 ** 2
    mask = 255 * mask.astype(int)
    word_cloud = WordCloud(collocations=True, background_color='white',
                           max_words=50, width=1200, height=1200,
                           mask=mask, contour_width=3, contour_color='black', ).generate_from_frequencies(
        dict(keywords))

    fig = px.imshow(word_cloud, title=f"Main words from description frequency")
    fig.update_xaxes(visible=False)
    fig.update_yaxes(visible=False)
    fig.show()
