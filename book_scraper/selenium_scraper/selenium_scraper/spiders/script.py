import pandas as pd

csv_file_path = 'bookswithlinksboth.csv'
df = pd.read_csv(csv_file_path)

df['main_genre'] = df['tags'].str.split(',').str[0].str.strip()

df.to_csv('clean_books.csv', index=False)