import pandas
from cleaning import cleaning_text
from stemming import stemmer

def read_file(path: str, col: str) -> list:
    data = pandas.read_csv(path,usecols=['title', 'text'], encoding='UTF-8')
    data = data.values.astype(str)

    data_cleared = []
    for row in data:
        data_cleared.append(cleaning_text(str(row)))
    return data_cleared