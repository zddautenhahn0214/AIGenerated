#
import csv
import json



def main():
    csv_file = 'input.csv'
    json_file = 'output.json'

    data = []
    with open(csv_file) as f:
        csv_reader = csv.DictReader(f)
        for row in csv_reader:
            data.append(row)

    with open(json_file, 'w') as f:
        json.dump(data, f)
    
if __name__ == '__main__':
    main()