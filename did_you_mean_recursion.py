def count_down(num):
    if (num == 0): #base case
        print('Time to go home lmao')

    else: #recursive else #1
        print('    in else #1: Number is currently',num)
        num = num-1
        print('    in else #1: Subtracted 1')
        count_down(num) #calling function recursivley
    

input_number = int(input('Hey enter a number you want to count to 0 from\n'))

if(input_number<0): #blocking input that is <0
    while input_number<0:
        input_number = int(input('Please enter a number > 0\n'))

count_down(input_number) #calling recursive count down function