import WordCloud from word_cloud
import pandas
import cleaning
import stemming
import matplotlib.pyplot as plt


def word_cloud(t: str):
    csv_data = pandas.read_csv(t, usecols=['title', 'text'], encoding='UTF-8')
    csv_data = ''.join(csv_data['title'])
    csv_data = cleaning.cleaning_text(csv_data)
    csv_data = stemming.stemmer(csv_data)
    unique = list(set(csv_data))
    bow = {w: csv_data.count(w) for w in unique}
    wc = WordCloud(width=640, height=480, background_color='grey')
    cloud = wc.generate_from_frequencies(bow)
    plt.axis("off")
    plt.imshow(cloud, interpolation='bilinear')
    plt.show()
