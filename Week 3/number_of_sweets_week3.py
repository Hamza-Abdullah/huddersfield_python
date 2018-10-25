valid_number = False
while valid_number is False:
    valid_number = True
    try:
        pupils = int(input('Enter how many pupils are in the class: '))
    except:
        print('An error occurred. Please enter a number.')
        valid_number = False
    else:
        try:
            sweets = int(input('Enter how many sweets there are: '))
        except:
            print('An error occurred. Please enter a number.')
            valid_number = False
    if pupils < 1 or sweets < 0:
        valid_number = False
        print('Please enter a valid number of pupils and sweets.')

each_pupil = sweets // pupils
sweets_left = sweets % pupils
print('Each pupil will get', each_pupil, 'sweets. There will be', sweets_left, 'left over.')
