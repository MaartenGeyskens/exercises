# Write your code here
def last_digit(n):
    return n % 10

def remove_last_digit(n):
    return n // 10

def digit_sum(n):
    count = 0
    while n > 0:
        count += last_digit(n)
        n = remove_last_digit(n)
    return count
        