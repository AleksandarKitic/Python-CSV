import csv

# READING CSV FILES
def application1():
    with open('csv_app.txt') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0

        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are{",".join(row)}')
                line_count += 1
            else:
                print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
                line_count += 1

            print(f'Processed {line_count} lines.')

def application2():
    with open('csv_app.txt', mode='r') as csv_file: # MODE='R' ----- MODE FOR READING FILES
        csv_reader = csv.DictReader(csv_file)
        line_count = 0

        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            print(
                f'\t{row["name"]} works in the {row["department"]} department, and was born in {row["birthday month"]}.')
            line_count += 1
        print(f'Processed {line_count} lines.')


# WRITING CSV FILES
def writing():
    with open('csv1_app1.txt', mode='w') as employ_file:
        employ_writer = csv.writer(employ_file, delimiter=',', quotechar='"', quoting= csv.QUOTE_MINIMAL)
        employ_writer.writerow(['Chris', 'Accouting', 'November'])
        employ_writer.writerow(['Eminem', 'Medical', 'April'])




application1()
print('*' * 50)
application2()
print('~' * 100)
writing()
