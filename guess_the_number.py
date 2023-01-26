import random

correct = 'you guessed correctly!'
too_low = 'too low'
too_high = 'too high'


def configure_range():
    """ Set the high and low values for the random number """
    return 1, 10


def generate_secret(low, high):
    """ Generate a secret number for the user to guess """
    return random.randint(low, high)


def get_guess():
    """ get user's guess, as an integer number """
    return int(input('Guess the secret number? '))


def check_guess(guess, secret):
    """ compare guess and secret, return string describing result of comparison """
    if guess == secret:
        return correct
    if guess < secret:
        return too_low
    if guess > secret:
        return too_high


def main():

    (low, high) = configure_range()
    secret = generate_secret(low, high)
    guess_count = 0

    while True:
        guess = get_guess()
        result = check_guess(guess, secret)
        print(result)

        if result == correct:
            break
        else:
            guess_count+=1
    
    oridnals = 'th'
    if ((guess_count + 1) == 1): 
        oridnals = 'st'
    elif ((guess_count + 1) == 2):
        oridnals = 'nd'
    elif ((guess_count + 1) == 3):
        oridnals = 'rd'
    else:
        oridnals = oridnals
    
    print(f'You got it right on {guess_count+1}{oridnals} guess')
    print('Thanks for playing the game!')


if __name__ == '__main__':
    main()
