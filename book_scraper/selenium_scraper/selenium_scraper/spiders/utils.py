# import csv
#
#
# def read_csv(input_file_path):
#     data = []
#     with open(input_file_path, 'r', newline='') as csvfile:
#         reader = csv.DictReader(csvfile)
#         for row in reader:
#             data.append(row)
#     return data
#
#
# def remove_duplicates(data, key_column):
#     seen = set()
#     unique_data = []
#     for row in data:
#         if row[key_column] not in seen:
#             seen.add(row[key_column])
#             unique_data.append(row)
#     return unique_data
#
#
# def write_csv(input_file_path, data, fieldnames):
#     with open(input_file_path, 'w', newline='') as csvfile:
#         writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#         writer.writeheader()
#         writer.writerows(data)
#
#
# def delete_rows_with_empty_fields(input_file_path, output_file_path):
#     with open(input_file_path, 'r', encoding='utf-8') as input_file, open(output_file_path, 'w', encoding='utf-8', newline='') as output_file:
#         reader = csv.DictReader(input_file)
#         fieldnames = reader.fieldnames
#         writer = csv.DictWriter(output_file, fieldnames=fieldnames)
#         writer.writeheader()
#
#         for row in reader:
#             # Check if any of the specified fields are empty
#             if all(row[field] for field in ['title', 'author', 'rating', 'url', 'cover_url', 'summary', 'tags',
#                                             'number_of_pages', 'time', 'amazon_link', 'audible_link', 'year_release',
#                                             'language', 'isbn', 'isbn13', 'format']):
#                 writer.writerow(row)
#
#
# # Usage
# input_csv_file_path = 'bookswithlinksboth.csv'
# output_csv_file_path = 'filtered_booksall.csv'
# key_column = 'title'
#
# data = read_csv(input_csv_file_path)
# unique_data = remove_duplicates(data, key_column)
#
# fieldnames = data[0].keys()
#
# write_csv(input_csv_file_path, unique_data, fieldnames)
#
#
# delete_rows_with_empty_fields(input_csv_file_path, output_csv_file_path)