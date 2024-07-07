from pathlib import Path
import pandas as pd

columns_to_extract = {
    'title': 'ости',
    'organization': 'Название представляющей организации, город',
    'department': 'Полное название кафедры/кафедр',
    'direction': 'Направление работы конференции',
    'text': 'Текст материалов конференции',
}

min_text_length = 10


def load(file: Path) -> pd.DataFrame:
    df = pd.read_excel(file)
    df = pd.DataFrame({id: df[title] for id, title in columns_to_extract.items()})
    df['title'] = df['title'].map(lambda s: s.lower() if s.isupper() else s)
    df = df[df['title'].str.len() >= min_text_length]
    df = df[df['text'].str.len() >= min_text_length]
    return df

def export(df: pd.DataFrame, file: Path) -> None:
    import pickle
    pickle.dump(df, file.open('wb'))


if __name__ == '__main__':
    file = Path() / 'заявки 2023.xlsx'
    df = load(file)
    export(df, Path() / 'dataset.pkl')
