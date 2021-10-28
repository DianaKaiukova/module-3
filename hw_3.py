def plural_form (number, form0, form1, form2):
     if number % 10  == 1 or number == 1:
         print(number, form0)
     elif number % 10 >= 2 and number % 10 <= 4 or number >=2 and number <=4:
         print(number, form1)
     else:
         print(number, form2)
