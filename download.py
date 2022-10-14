import csv
import requests

filename = 'collection.csv'
output_dir = 'test_dir'  # Make sure directory exists
extension = 'jpg'

with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    first = True
    for row in datareader:
        if first:
            first = False
        else:
            url = row[0]   # Assume URL is in first column
            name = row[2]  # Assume name is in third column
            print(url, name)

            response = requests.get(url)
            open(test_dir + "/" + name + "." + extension, "wb").write(response.content)
