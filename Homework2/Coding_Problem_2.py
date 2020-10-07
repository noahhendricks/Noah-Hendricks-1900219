# Noah Hendricks
# 1900219
# Part b

# defined function for date format
def date_formatter(num_month):
    new_day = 00
    new_date = single_line.split(' ')
    new_year = 0000

    # for loop for the new date
    for x in range(len(new_date)):
        # parsing the comma out of  the middle number (day)
        if x == 1:
            day = new_date[x]
            new_day = day.split(',')
            new_day = new_day[0]

        # parse split of the return line at the end of year
        if x == 2:
            year = new_date[x]
            new_year = year.split('\n')
            new_year = new_year[0]
            # new year format

    # date format restrictions for day
    if len(new_day) > 2:
        print('Incorrect day format')
    elif int(new_day) > 31:
        print('Incorrect day of month')

    # date format restrictions for year
    elif len(new_year) > 4 or len(new_year) < 4:
        print('Incorrect year format')
    # correct format of date that separates it with "/"
    else:
        newer_date = (str(num_month), str(new_day), str(new_year))
        separator = '/'
        format_date = separator.join(newer_date)
        print(format_date)

# dictionary is not used just there for reference and reminder!


dictionary = {'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5, 'June': 6, 'July': 7, 'August': 8,
              'September': 9, 'October': 10, 'November': 11, 'December': 12}

# program runs: while loop is triggered when data is set to 1
new_data = 1

# file being inputted into program
file_name = str(input())

# opens the input file as read only
with open(file_name, 'r') as txt_file:
    # program runs: while loop is triggered when data is set to 1
    while new_data == 1:
        single_line = txt_file.readline()

        # if and elif statements for all months and coverts each to its specified number using find() command
        if single_line.find('January') != -1:
            month = 1
            date_formatter(month)

        elif single_line.find('February') != -1:
            month = 2
            date_formatter(month)

        elif single_line.find('March') != -1:
            month = 3
            date_formatter(month)

        elif single_line.find('April') != -1:
            month = 4
            date_formatter(month)

        elif single_line.find('May') != -1:
            month = 5
            date_formatter(month)

        elif single_line.find('June') != -1:
            month = 6
            date_formatter(month)

        elif single_line.find('July') != -1:
            month = 7
            date_formatter(month)

        elif single_line.find('August') != -1:
            month = 8
            date_formatter(month)

        elif single_line.find('September') != -1:
            month = 9
            date_formatter(month)

        elif single_line.find('October') != -1:
            month = 10
            date_formatter(month)

        elif single_line.find('November') != -1:
            month = 11
            date_formatter(month)

        elif single_line.find('December') != -1:
            month = 12
            date_formatter(month)

        # ends program when "-1" is read
        elif single_line == '-1':
            new_data = 0
