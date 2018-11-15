students = 0
num_of_pc = 0
while students < 1:
    try:
        students = int(input('Enter the number of students there are: '))
    except ValueError:
        print('That value for number of students is not valid. Please try again.')
while num_of_pc < 1:
    try:
        num_of_pc = int(input('Enter the number of PCs there are in each lab: '))
    except ValueError:
        print('That value for number of PCs is not valid. Please try again.')

students % num_of_pc == 0
if students % num_of_pc == 0:
    num_of_labs = str(students // num_of_pc)
else:
    num_of_labs = str(students // num_of_pc + 1)
if num_of_labs == '1':
    print('You need 1 lab for all the students.')
else:
    print('You need ' + num_of_labs + ' labs for all the students.')