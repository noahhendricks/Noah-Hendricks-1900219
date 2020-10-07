# Noah Hendricks
# 1900219
# Part a

# defined function for date format
def date_formatter(num_month):
    # date format
    new_day = 00
    year = 0
    new_date = input_date.split(' ')

    # for loop for the new date
    for x in range(len(new_date)):
        # parsing the comma out of  the middle number (day)
        if x == 1:
            day = new_date[x]
            new_day = day.split(',')
            new_day = new_day[0]

        # new year format
        if x == 2:
            year = new_date[x]

    # date format restrictions for day
    if len(new_day) > 2:
        print('Incorrect day format')
    elif int(new_day) > 31:
        print('Incorrect day of month')

    # date format restrictions for year
    elif len(year) > 4 or len(year) < 4:
        print('Incorrect year format')

    # joining string together and separating them with "/"
    else:
        newer_date = (str(num_month), str(new_day), str(year))
        separator = '/'
        format_date = separator.join(newer_date)
        print(format_date)

# dictionary is not used just there for reference and reminder!


dictionary = {'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5, 'June': 6, 'July': 7, 'August': 8,
              'September': 9, 'October': 10, 'November': 11, 'December': 12}

# program runs: while loop is triggered when data is set to 1
new_data = 1
while new_data == 1:
    # user input of date and it has to be in the correct date format
    input_date = str(input())

# if, else, and elif statements for all months and coverts each to its specified number using find() command
    if input_date.find('January') != -1:
        month = 1
        date_formatter(month)

    elif input_date.find('February') != -1:
        month = 2
        date_formatter(month)

    elif input_date.find('March') != -1:
        month = 3
        date_formatter(month)

    elif input_date.find('April') != -1:
        month = 4
        date_formatter(month)

    elif input_date.find('May') != -1:
        month = 5
        date_formatter(month)

    elif input_date.find('June') != -1:
        month = 6
        date_formatter(month)

    elif input_date.find('July') != -1:
        month = 7
        date_formatter(month)

    elif input_date.find('August') != -1:
        month = 8
        date_formatter(month)

    elif input_date.find('September') != -1:
        month = 9
        date_formatter(month)

    elif input_date.find('October') != -1:
        month = 10
        date_formatter(month)

    elif input_date.find('November') != -1:
        month = 11
        date_formatter(month)

    elif input_date.find('December') != -1:
        month = 12
        date_formatter(month)

    # ends program when "-1" is entered
    elif input_date == '-1':
        new_data = 0

    # if incorrect format is inputted, then program will not run but will allow you a chance to input again correctly
    else:
        print('incorrect month format')
