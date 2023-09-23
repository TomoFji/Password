import string, itertools, time

def password_cracker(password):
    characters = string.ascii_letters + string.digits + "!@#$%^&*()-_=+[]{}|;:\",.<>/?`~\\"
    attempts = 0
    
    for pass_length in range (1,9):
        for permutation in itertools.product(characters, repeat=pass_length):
            attempts += 1
            permutation = ''.join(permutation)
            if permutation == password:
                print(f"Password {password} guessed in {attempts} attempts")
                return
    print("Failure")


def crack():
    passwords = []
    with open("Passwords.txt", 'r') as file:
        for line in file:
            passwords.append(line.strip())

    for password in passwords:
        start = time.time()
        password_cracker(password)
        end = time.time()
        print(end - start)

crack()