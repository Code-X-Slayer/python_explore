import csv

with open('names.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    # print(csv_reader)
    # <_csv.reader object at 0x00000257955C6680>
    # generator object
    
    # for line in csv_reader:
    #     print(line)

    # if we want just email
    # for line in csv_reader:
    #     print(line[2])

    # if we dont want to print 1st header line
    # next(csv_reader)
    # for line in csv_reader:
    #     print(line)

    # with open('names_copy.csv', 'w') as write_file:
    #     csv_writer = csv.writer(write_file, delimiter='-')
    #     for line in csv_reader:
    #         csv_writer.writerow(line)
    # this comes with a lot of issues
    # first one extra lines since we dont mention in newline=''
    # its gonna add extra line after writing a row which itself has a new line
    # second whenever u use a delimiter where values contains it
    # its gonna use "" to enclose value to sep delimeter actual and value containing it

    # with open('names_copy.csv', 'w', newline='') as write_file:
    #     csv_writer = csv.writer(write_file, delimiter='-')
    #     for line in csv_reader:
    #         csv_writer.writerow(line)
    # this resolves the 1st issue that is extra lines
    # as we left it to csv to handle new line instead adding extra one
    # the issue with values surrounded by "" was we chosen delim which values contains
    # so make sure you use better delimiter with less cost and not existing

    # lets use tab ie \t whihc is better
    # with open('names_copy.csv', 'w', newline='') as write_file:
    #     csv_writer = csv.writer(write_file, delimiter='\t')
    #     for line in csv_reader:
    #         csv_writer.writerow(line)

    # now lets read the new tab sep file using wrong del other that tab
    # with open('names_copy.csv', 'r') as f:
    #     csv_reader = csv.reader(f)
    #     for line in csv_reader:
    #         print(line) 
    # as you can we are getting list with single value whole 3 cols at each row
    # since it tried to split using , since it dont have one itconsidered it as single val
    # so we have to explicitly mention delim in such cases

    # with open('names_copy.csv', 'r') as f:
    #     csv_reader = csv.reader(f, delimiter='\t')
    #     for line in csv_reader:
    #         print(line)

# till now we use csv reader and writer
# lets see a better implementation using DictReader and DictWriter
with open('names.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    # for line in csv_reader:
    #     print(line)
    # as you can see output its constructs orderedDict with keys as firstrow
    # {'first_name': 'John', 'last_name': 'Doe', 'email': 'john-doe@bogusemail.com'}
    # {'first_name': 'Mary', 'last_name': 'Smith-Robinson', 'email': 'maryjacobs@bogusemail.com'}

    # its better to write line['email'] over line[2]
    # for line in csv_reader:
    #     print(line['email'])

    # for writer we have to provide field names
    # with open('names_copy.csv', 'w', newline='') as f:
    #     field_names = ['first_name', 'last_name', 'email']
    #     csv_writer = csv.DictWriter(f, fieldnames=field_names, delimiter='\t')
    #     csv_writer.writeheader()
    #     for line in csv_reader:
    #         csv_writer.writerow(line)

    # lets say we wanted to have a copy of selected columns
    # with open('names_copy.csv', 'w', newline='') as f:
    #     field_names = ['first_name', 'last_name']
    #     csv_writer = csv.DictWriter(f, fieldnames=field_names, delimiter='\t')
    #     csv_writer.writeheader()
    #     for line in csv_reader:
    #         del line['email']
    #         csv_writer.writerow(line)
