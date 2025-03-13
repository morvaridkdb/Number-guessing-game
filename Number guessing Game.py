import random

def number_guessing_Game():
    print('Welcome to the Game')
    print( 'I choose One Number between 10 to 50.Try to find it.')

    secret_Number = random.randint(10,50)
    attempts = 0

    while True:
        try:
              guess = int(input('Enter your guess: '))
              attempts += 1

              if guess > secret_Number:
                   print('Enter a smaller Number')
              

              elif guess < secret_Number :
                   print('Enter a bigger Number')
              

              else:
                   print(f'Congratulation , you guess Number{secret_Number} in {attempts} tries.')
                   break
        except ValueError:
             print("Please enter a valid integer.")

number_guessing_Game()
         
             
            
             
                    

              
           

