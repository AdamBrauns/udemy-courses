# Warm up Problems
def lesser_of_two_evens(a, b):
    '''
    LESSER OF TWO EVENS: Write a function that returns the lesser of two 
    given numbers if both numbers are even, but returns the greater if 
    one or both numbers are odd
    '''
    if a % 2 == 0 and b % 2 == 0:
        return min(a, b)
    else:
        return max(a, b)

#print(lesser_of_two_evens(2, 4))
#print(lesser_of_two_evens(2, 5))

def animal_crackers(text):
    '''
    ANIMAL CRACKERS: Write a function takes a two-word string and returns 
    True if both words begin with same letter
    '''
    space_split = text.lower().split()
    return space_split[0][0] == space_split[1][0]

#print(animal_crackers('Levelheaded Llama'))
#print(animal_crackers('Crazy Kangaroo'))

def makes_twenty(n1,n2):
    '''
    MAKES TWENTY: Given two integers, return True if the sum of the
    integers is 20 or if one of the integers is 20. If not, return False
    '''
    return (n1 + n2) == 20 or n1 == 20 or n2 == 20

#print(makes_twenty(20, 10))
#print(makes_twenty(2, 3))

# Level 1 Problems
def old_macdonald(name):
    '''
    OLD MACDONALD: Write a function that capitalizes the first and
    fourth letters of a name
    '''
    first_half = name[:3].capitalize()
    second_half = name[3:].capitalize()
    return first_half + second_half

#print(old_macdonald('macdonald'))

def master_yoda(text):
    '''
    MASTER YODA: Given a sentence, return a sentence with the words reversed
    '''
    wordlist = text.split()
    reversed_wordlist = wordlist[::-1]
    return ' '.join(reversed_wordlist)

#print(master_yoda('I am home'))
#print(master_yoda('We are ready'))

def almost_there(n):
    '''
    ALMOST THERE: Given an integer n, return True if n is within 10 of
    either 100 or 200
    '''
    return (abs(n - 100) <= 10) or (abs(n - 200) <= 10)

#print(almost_there(90))
#print(almost_there(104))
#print(almost_there(150))
#print(almost_there(209))

# Level 2 Problems 
def has_33(nums):
    '''
    Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.
    '''
    for i in range(0, len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False

#print(has_33([1, 3, 3]))
#print(has_33([1, 3, 1, 3]))
#print(has_33([3, 1, 3]))

def has_33_2(nums):
    '''
    Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.
    '''
    for i in range(0, len(nums) - 1):
        if nums[i:i + 2] == [3, 3]:
            return True
    return False

#print(has_33_2([1, 3, 3]))
#print(has_33_2([1, 3, 1, 3]))
#print(has_33_2([3, 1, 3]))

def paper_doll(text):
    '''
    PAPER DOLL: Given a string, return a string where for every character
    in the original there are three characters
    '''
    return_str = ''
    for letter in text:
        return_str += letter * 3
    return return_str

#print(paper_doll('Hello'))
#print(paper_doll('Mississippi'))

def blackjack(a, b, c):
    '''
    BLACKJACK: Given three integers between 1 and 11, if their sum is less
    than or equal to 21, return their sum. If their sum exceeds 21 and there's
    an eleven, reduce the total sum by 10. Finally, if the sum (even after adjustment)
    exceeds 21, return 'BUST'
    '''
    if sum([a, b, c]) <= 21:
        return a + b + c
    elif 11 in [a, b, c] and sum([a, b, c]) <= 31:
        return sum([a + b + c]) - 10
    return 'BUST'

#print(blackjack(5, 6, 7))
#print(blackjack(9, 9, 9))
#print(blackjack(9, 9, 11))

def summer_69(arr):
    '''
    SUMMER OF '69: Return the sum of the numbers in the array, except ignore
    sections of numbers starting with a 6 and extending to the next 9 (every 6
    will be followed by at least one 9). Return 0 for no numbers.
    '''
    flag = False
    total = 0
    for num in arr:
        if num == 6:
            flag = True
        elif num == 9:
            flag = False
        else:
            if flag == False:
                total += num
    return total

#print(summer_69([1, 3, 5]))
#print(summer_69([4, 5, 6, 7, 8, 9]))
#print(summer_69([2, 1, 6, 9, 11]))

def summer_69_2(arr):
    '''
    SUMMER OF '69: Return the sum of the numbers in the array, except ignore
    sections of numbers starting with a 6 and extending to the next 9 (every 6
    will be followed by at least one 9). Return 0 for no numbers.
    '''
    total = 0
    add = True

    for num in arr:
        while add:
            if num != 6:
                total += num
                break
            else:
                add = False
        while not add:
            if num != 9:
                break
            else:
                add = True
                break
    return total

#print(summer_69_2([1, 3, 5]))
#print(summer_69_2([4, 5, 6, 7, 8, 9]))
#print(summer_69_2([2, 1, 6, 9, 11]))

# Challenging Problems
def spy_game(nums):
    '''
    SPY GAME: Write a function that takes in a list of integers and returns
    True if it contains 007 in order at any point (cannot be extra 0 or 7 in between)
    '''
    zero_count = 0
    for num in nums:
        if num == 0:
            zero_count += 1
        elif num == 7:
            if zero_count != 2:
                zero_count = 0
            else:
                return True    
    return False

#print(spy_game([1,2,4,0,0,7,5]))
#print(spy_game([1,0,2,4,0,5,7]))
#print(spy_game([1,7,2,0,4,5,0]))

def spy_game_2(nums):
    '''
    SPY GAME: Write a function that takes in a list of integers and returns
    True if it contains 007 in order at any point (can be extra 0 or 7 in between)
    '''
    code = [0, 0, 7, 'x']
    for num in nums:
        if num == code[0]:
            code.pop(0)
    return len(code) == 1

#print(spy_game_2([1,2,4,0,0,7,5]))
#print(spy_game_2([1,0,2,4,0,5,7]))
#print(spy_game_2([1,7,2,0,4,5,0]))

def count_primes(num):
    '''
    COUNT PRIMES: Write a function that returns the number of prime
    numbers that exist up to and including a given number
    '''
    # Check for 0 or 1 input
    if num < 2:
        return 0

    # 2 or greater
    primes = [2]
    x = 3

    # x is going through every number up to the input num
    while x <= num:
        # Check if x is prime
        for y in primes:
            if x % y == 0:
                x += 2
                break
        else:
            primes.append(x)
            x += 2
    print(primes)
    return(len(primes))

#print(count_primes(100))

def print_big(letter):
    patterns = {1:'  *  ',2:' * * ',3:'*   *',4:'*****',
                5:'**** ',6:'   * ',7:' *   ',8:'*   * ',
                9:'*    ',10:'*  **'}

    alphabet = {'A':[1,2,4,3,3],'B':[5,3,5,3,5],'C':[4,9,9,9,4],
                'D':[5,3,3,3,5],'E':[4,9,4,9,4],'F':[4,9,4,9,9], 
                'G':[4,9,10,3,4],'H':[3,3,4,3,3],'I':[4,1,1,1,4]}

    for pattern in alphabet[letter.upper()]:
        print(patterns[pattern])

#print_big('i')