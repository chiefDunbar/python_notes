# Write your solution here
def prime_numbers():

    def is_prime(number: int):
        for div in range(2, number):
            if number % div == 0:
                return False
        return True
    
    prime = 2
    while True:
        if is_prime(prime):
            yield prime
        prime += 1

