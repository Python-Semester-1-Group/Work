# Connor White
# Brad Wiersema

# Group Programming Assignment


answer = 0

while answer != 'N':
    print('Hi, User, please selct from the following menu: ')
    print('1. Add')
    print('2. Subtract')
    print('3. Multiply')
    print('4. Divide')
    print('5. Modulo')
    print('6. Quit')

    user_choice = input('Enter your choice here: ')

    if user_choice == 'Add':
        num1 = (int(input('Enter First Number: ')))
        num2 = (int(input('Enter Second Number: ')))
        print('Your answer is: ', num1 + num2)
    
    if user_choice == 'Subtract':
        num1 = (int(input('Enter First Number: ')))
        num2 = (int(input('Enter Second Number: ')))
        print('Your answer is: ', num1 - num2)
    
    if user_choice == 'Multiply':
        num1 = (int(input('Enter First Number: ')))
        num2 = (int(input('Enter Second Number: ')))
        print('Your answer is: ', num1 * num2)

    if user_choice == 'Divide':
        num1 = (int(input('Enter First Number: ')))
        num2 = (int(input('Enter Second Number: ')))
        print('Your answer is: ', num1 / num2)

    if user_choice == 'Modulo':
        num1 = (int(input('Enter First Number: ')))
        num2 = (int(input('Enter Second Number: ')))
        print('Your remainder is: ', num1 % num2)

    if user_choice == 'Quit':
        break
    
    answer = input('Do you want to return to menu(Y/N): ')
    
print('Thank you for using our calculator!')
