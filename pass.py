import string, itertools, time

def password_cracker(password):
    #function creates every single possible password combination 
    #until it lands on the correct one
    characters = string.ascii_letters + string.digits + "!@#$%^&*()-_=+[]{}|;:\",.<>/?`~\\"
    attempts = 0
    
    for pass_length in range (1,9):
        for combination in itertools.product(characters, repeat=pass_length):
            attempts += 1
            combination = ''.join(combination)
            if combination == password:
                print(f"Password {password} guessed in {attempts} attempts")
                return
    print("Failure")


def crack():
    #function reads input from a .txt file and generates passwords using
    #password_cracker() until it lands on the correct one
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
