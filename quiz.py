question = input('Hey, Would you like to play a little quiz game? :').lower()
if question != 'yes':
    quit()

score = 0

answer = input('Ok, Here is your first question: "What is the primary color of Pikachu? :').lower()
if answer == 'yellow':
    print('Correct!')
    score += 1
else:
    print('Wrong!')
answer = input('What is H2O commonly known as? :').lower()
if answer == 'water':
    print('Correct!')
    score += 1
else:
    print('Wrong!')
        
answer = input('How many continents are there in the world? :').lower()
if answer == '7' or answer == 'seven':
    print('Correct!')
    score += 1
else:
    print('Wrong!')
        
answer = input('What is the chemical symbol for gold? :').lower()
if answer == 'au':
    print('Correct!')
    score += 1
else:
    print('Wrong')
    
answer = input('Which flower is known as the “king of flowers”? :').lower()
if answer == 'rose':
    print('Correct!')
    score += 1
else:
    print('Wrong!')

print(f'You got ' + str(score) + 'question correct!')