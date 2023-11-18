import pandas as pd
import numpy as np

csv_file_path = 'books_filtered.csv'
df = pd.read_csv(csv_file_path)

df['main_genre'] = df['genres'].str.split(',').str[0].str.strip()


def get_age(genres):
    if pd.isna(genres):
        return None

    age_tags = []
    if 'Young Adult' in genres:
        age_tags.append('Young Adult')
    if 'Childrens' in genres:
        age_tags.append('Childrens')
    if 'Middle Grade' in genres:
        age_tags.append('Middle Grade')
    if 'School' in genres:
        age_tags.append('School')
    if 'Adult' in genres:
        age_tags.append('Adult')

    return ', '.join(age_tags) if age_tags else None


df['age'] = df['genres'].apply(get_age)

percentage_best_books = 0.2

df['best books of 2023'] = np.random.choice([True, False], size=len(df), p=[percentage_best_books, 1-percentage_best_books])

df['best books of 2023'] = df['best books of 2023'].map({True: 'Yes', False: 'No'})

df.to_csv('books_final.csv', index=False)