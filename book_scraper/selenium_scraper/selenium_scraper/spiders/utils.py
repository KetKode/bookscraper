import csv


def delete_rows_with_empty_fields(input_file_path, output_file_path):
    with open(input_file_path, 'r', encoding='utf-8') as input_file, open(output_file_path, 'w', encoding='utf-8', newline='') as output_file:
        reader = csv.DictReader(input_file)
        fieldnames = reader.fieldnames
        writer = csv.DictWriter(output_file, fieldnames=fieldnames)
        writer.writeheader()

        for row in reader:
            # Check if any of the specified fields are empty
            if all(row[field] for field in ['title', 'author', 'rating', 'url', 'cover_url', 'rating_small', 'summary', 'genres']):
                writer.writerow(row)

# Usage
# input_csv_file_path = 'booksall.csv'
# output_csv_file_path = 'filtered_booksall.csv'
# delete_rows_with_empty_fields(input_csv_file_path, output_csv_file_path)