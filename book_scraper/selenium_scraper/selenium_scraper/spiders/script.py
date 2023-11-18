# import pandas as pd
# import numpy as np
#
# csv_file_path = 'bookswithlinksboth.csv'
# df = pd.read_csv(csv_file_path)
#
# df['main_genre'] = df['tags'].str.split(',').str[0].str.strip()
#
#
# def get_age(tags):
#     if pd.isna(tags):
#         return None
#
#     age_tags = []
#     if 'Young Adult' in tags:
#         age_tags.append('Young Adult')
#     if 'Childrens' in tags:
#         age_tags.append('Childrens')
#     if 'Middle Grade' in tags:
#         age_tags.append('Middle Grade')
#     if 'School' in tags:
#         age_tags.append('School')
#     if 'Adult' in tags:
#         age_tags.append('Adult')
#
#     return ', '.join(age_tags) if age_tags else None
#
#
# df['age'] = df['tags'].apply(get_age)
#
# percentage_best_books = 0.2
#
# df['best books of 2023'] = np.random.choice([True, False], size=len(df), p=[percentage_best_books, 1-percentage_best_books])
#
# df['best books of 2023'] = df['best books of 2023'].map({True: 'Yes', False: 'No'})
#
# df.to_csv('clean_books_final1.csv', index=False)