def fizz_buzz (number):
    if number in range(1000, 20001):
        number1 = number % 3 
        number2 = number % 5
        if number1 == 0 and   number2  == 0:
            print('FizzBuzz')
        elif number1 == 0:
            print('Fizz')
        elif number2 == 0:
            print('Buzz')
        else:
             print('Число не нодится в данном промежутке')
  