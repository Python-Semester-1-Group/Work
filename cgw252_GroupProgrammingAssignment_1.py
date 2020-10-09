'''
Connor White
Brad Wiersema

Group Programming Assignment
'''
#We assigned the variable so that an error doesn't appear on the first line of our while loop.
answer = 0

# Loop prints the menu to the user and asks for a choice. The loop will start back if the user types Y to return to the menu.
while answer != 'N':
    print('Hi, User, please selct from the following menu: ')
    print('1. Add')
    print('2. Subtract')
    print('3. Multiply')
    print('4. Divide')
    print('5. Modulo')
    print('6. Quit')

    user_choice = input('Enter your choice here: ')
    
#Addition statements
    if user_choice == 'Add':
        num1 = (int(input('Enter First Number: ')))
        num2 = (int(input('Enter Second Number: ')))
        print('Your answer is: ', num1 + num2)
        
#Subtraction statements
    if user_choice == 'Subtract':
        num1 = (int(input('Enter First Number: ')))
        num2 = (int(input('Enter Second Number: ')))
        print('Your answer is: ', num1 - num2)
        
#Multiplication statements
    if user_choice == 'Multiply':
        num1 = (int(input('Enter First Number: ')))
        num2 = (int(input('Enter Second Number: ')))
        print('Your answer is: ', num1 * num2)
        
#Division statements
    if user_choice == 'Divide':
        num1 = (int(input('Enter First Number: ')))
        num2 = (int(input('Enter Second Number: ')))
        print('Your answer is: ', num1 / num2)
        
#Modulo statements
    if user_choice == 'Modulo':
        num1 = (int(input('Enter First Number: ')))
        num2 = (int(input('Enter Second Number: ')))
        print('Your remainder is: ', num1 % num2)
        
#Quit statement
    if user_choice == 'Quit':
        break
        
#input that determines whether the loop continues or stops.
    answer = input('Do you want to return to menu(Y/N): ')
    
#Statement that prints when the user decides to stop using the calculator or in other words, when the loop terminates.
print('Thank you for using our calculator!')
