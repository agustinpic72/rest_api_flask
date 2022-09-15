def fizz_buzz(numbers):
    result = []
    for number in numbers:
        if number % 3 == 0 and number % 5 == 0:
            result.append('Fizz Buzz')
        elif number % 3 == 0:
            result.append('Fizz')
        elif number % 5 == 0:
            result.append('Buzz')
        else:
            result.append(number)
    return result
            
if __name__ == '__main__':
    print('** First excercise "FizzBuzz" **\n')
    numbers = [x for x in range(101)]
    print(fizz_buzz(numbers),'\n\n')

# ---------------------------------------------

def fibo_list(number):
    __base = [0,1]
    fibo_list = __base
    for n in range(0,number-2):
        fibo_list.append(fibo_list[-1]+fibo_list[-2])
    return fibo_list

if __name__ == '__main__':
    print('** Second excercise "Fibonacci Sequence" **\n')
    print(fibo_list(15),'\n\n')

# ---------------------------------------------

def word_counter(text):
    punctuation= '''!()-[]{};:'"\\,<>./?@#$%^&*¡=¿_~'''
    for simbol in punctuation:
        text=text.replace(simbol,'')
    text = text.lower()
    text = text.split(' ')
    result = {word.strip() : text.count(word) for word in text}
    return result 

if __name__ == '__main__':
    print('** Third excercise "Word Counter" **')
    print(word_counter("H!i ho!w ar!e th??i,,ngs? $,Ho!!w ar¿¡e you? Ar$$e you a!!! developer? I a{}m also a d=)(eveloper"))