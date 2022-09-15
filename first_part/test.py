from first_part import fizz_buzz, fibo_list, word_counter

def test_fizz_buzz():
    numbers = [x for x in range(101)]
    assert fizz_buzz(numbers) == ['Fizz Buzz', 1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz', 11, 'Fizz', 13, 14, 'Fizz Buzz', 16, 17, 'Fizz', 19, 'Buzz', 'Fizz', 22, 23, 'Fizz', 'Buzz', 26, 'Fizz', 28, 29, 'Fizz Buzz', 31, 32, 'Fizz', 34, 'Buzz', 'Fizz', 37, 38, 'Fizz', 'Buzz', 41, 'Fizz', 43, 44, 'Fizz Buzz', 46, 47, 'Fizz', 49, 'Buzz', 'Fizz', 52, 53, 'Fizz', 'Buzz', 56, 'Fizz', 58, 59, 'Fizz Buzz', 61, 62, 'Fizz', 64, 'Buzz', 'Fizz', 67, 68, 'Fizz', 'Buzz', 71, 'Fizz', 73, 74, 'Fizz Buzz', 76, 77, 'Fizz', 79, 'Buzz', 'Fizz', 82, 83, 'Fizz', 'Buzz', 86, 'Fizz', 88, 89, 'Fizz Buzz', 91, 92, 'Fizz', 94, 'Buzz', 'Fizz', 97, 98, 'Fizz', 'Buzz']
    assert fizz_buzz([3,5,6,7,9,15]) == ['Fizz','Buzz','Fizz',7,'Fizz','Fizz Buzz']

def test_fibo_list():
    assert fibo_list(15) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377]
    assert fibo_list(50) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040, 1346269, 2178309, 3524578, 5702887, 9227465, 14930352, 24157817, 39088169, 63245986, 102334155, 165580141, 267914296, 433494437, 701408733, 1134903170, 1836311903, 2971215073, 4807526976, 7778742049]
    assert fibo_list(2)[0] == 0
    assert fibo_list(2)[1] == 1

def test_word_counter():
    assert word_counter('Hi, hi, hI, HI') == {'hi':4}
    assert word_counter("Hi i'm im IM Agustin agustin aguSTIN Piccoli picCOLI and aN??D thi!!s i,,,s my test! Test teSt") == {'hi': 1, 'im': 3, 'agustin': 3, 'piccoli': 2, 'and': 2, 'this': 1, 'is': 1, 'my': 1, 'test': 3}



