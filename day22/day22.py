import csv
import pandas

with open('./medical_records.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count != 0:
            print(f'\t{row[0]} has the following problem; {row[1]} and should {row[2]}.')
            line_count += 1
        else:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
    print(f'Processed {line_count} lines.')





with open('records.csv', mode='w') as records:
    records_writer = csv.writer(records, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    records_writer.writerow(['Fru Ben ', 'Teacher ', 'Paid'])
    records_writer.writerow(['"Telmar ngwa"', 'Student', 'NotPaid'])

    # csv_reader = csv.reader(csv_file, delimiter=',')




# df = pandas.read_csv('last.txt' , index_col='Hire Date', parse_dates=['Hire Date'])

df = pandas.read_csv('last.txt', 
            index_col='Employee', 
            parse_dates=['Hired'], 
            header=0, 
            names=['Employee', 'Hired','Salary', 'Sick Days'])

# print(df)

df.to_csv('last_modified.csv')
print(type(df['Sick Days'][0]))
