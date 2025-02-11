# VARIABLES       
#                  int = whole number, float = decimal number, string = text boolean = True or False
# #price = 10
# #price = 20   # eto ang lalabas kasi ito ang last na line na binasa

# #print (price)

# patient_name = "John Smith"
# age = 20
# is_new = True
# is_old = False
# print(patient_name)
# print(age)
# print(is_new)


#RECEIVING INPUT

#name = input('what is your name? ')     #input para mapa print yung nasa loob ng ''
#print ('Hi ' + name)


#exercise

# name = input('What is you name? ')
# print ('hello '+ name)
# color = input ('What is your favourite color? ') #nag dagdag ng bagong variable para malaman ang color
# print (name +' likes the color ' +color )



#TYPE CONVERSION

#birth_year = input ('Brith year: ')

#age = 2025 - int(birth_year)    #kaya may int kase we are subtracting int '2025' sa string 'birth_year'
#print (age)                     # int() para ma convert and string to int (text to number)
                                #float() para ma convert string to float (text to number with decimal point)
                                #str() para ma convert and int to string (number to text)
                                #bool() para ma convert and string to boolean value
                                #tuwing gagamit ng input() function, laging string ang ma babasa, if numerical value ang gusto mapa labas, tsaka gagamit ng sting or float

#exercise
# weight_lbs = input ('what is your weight in lbs?: ')
# weight_kg = int(weight_lbs) * .453
# print ('Your weight in kg is: ' + str(weight_kg) + ('kg'))




#STRINGS

# course = "Python's for Beginners"   # '' para magamit ang "" and vice versa pero kapag ginagamit parehas need ay """ """" (triple quote)
# print (course[1:-1])                  # 0: = pinaka unang letter hanngang dulo, pag -1 ang una, sa pinaka last ang start 
                                    # [1:-1] hindi kasama ang pinaka last letter (ython's for Beginner)






#FORMATTED STRINGS

# first_name = 'Angelo'
# last_name = 'Untalan' 
# message = f'{first_name} {last_name} is a coder'      #dito na gamit ang fiormatted strings para mas malinis ang code
# print (message) 





#STRING METHODS

# course = 'Python for beginners'
# print (len(course))                                        #para malaman ang length ng value ng variable
# print (course.lower())
# print (course.find('f')                                    #kapag wala yung hinahanap -1 lalabas
# print (course.replace('beginners', 'not beginners'))       #case sensitive ang python kaya dapat double check lagi
# print ('Python' in course)                                   # in = boolean value = do we have it or not. TRUE OR FALSE








#ARITHMETIC OPERATIONS
# print (10 ** 3)                            #+, -, *, ** exponent = n to the power of n, / = float value lalabas meaning may decimal, // = integer whole number lalabas, % yung remainder ng division ang lalabas
# x = 10
# x -=3
# print (x)





#OPERATOR PRECEDENCE
                                #PEMDAS parin ang susundin
# x = (2+3) * 10 - 3
# print (x)





#MATH FUNCTIONS

# import math

# x = 12.6

# print(math.floor(2.9))       #ceil = ceiling, para ma round pa taas
# print(math.floor(x))           #floor = para ma round off sa pinaka mababa
# x = 2.9
# print(round(x))           #para ma round off yung value
# print(abs(-2.9))          # para maging absolute value = laging magiging positive





#IF STATEMENT

# is_hot = True                      #kapag true at false = its a hot day, kapag false at true = cold day, kapag parehas false, else ang babasahin
# is_cold = True                    #kapag parehas true, ang babasahin ay yung is_hot kase true.

# if is_hot:
#     print ('is a hot day')
#     print('drink plenty of water')

# elif is_cold:
#     print("it's a cold day")
#     print("wear come warm clothes")

# else:
#     print("it's a good day")
# print('enjoy your day')


#EXERCISE

# price = 1000000
# good_credit = True


# if good_credit:
#    down_payment = .1 * price

# else:
#     down_payment = .2 * price

# print (f"Your total down payment is ${down_payment}")


    


#LOGICAL OPERATORS
                        # AND = both, OR = atleast one, NOT =  

# good_credit = True
# has_criminal_record = True


# if good_credit and not has_criminal_record:
#     print('eligable for loan')

# else:
#     print ('not eligable for loan')




#COMPARISON OPERATORS

# name = "gelo"                               # WAG KALILIMUTAN NA KAPAG STRING ANG VALUE NG VARIALE LAGING MAY QUOTATION ""

# if len(name) < 3:
#     print('name must be atleast 3 characters')

# elif len(name) > 50:
#     print ("name can be a maximum of 50 characters ")

# else:
#     print("name looks good")





#WEIGHT CONVERTER PROGRAM   

# weight = int(input ("Weight: "))              #int() para maging integet ang value nung nasa loob kase i mumultiply siya
# symbol = input ("(L)bs or (K)g:")

# if symbol.upper() == "L":                     #.upper() == "L" para maging uppercase lahat ng ilalagay sa input
#     converted = weight * 0.45
#     print(f"your weight is {converted} Kilos")

# else:
#     converted = weight // 0.45
#     print (f"your weight is {converted} Lbs")





#WHILE LOOPS

# i = 1 

# while i <= 5:
#     print('*' * i)
#     i = i + 1                         #pag hindi ginawa to, i will be 1 forever kaya magiging infinite loop
# print("Done")


#EXERCISE GUESSING GAME


# secret_number = 17
# guess_count = 0
# guess_limit = 3

# while guess_count < guess_limit:
#     guess = int(input('Guess the secret number: '))
#     guess_count += 1

#     if guess == secret_number:
#         print (" you've guessed the secret number!")
#         break
# else:
#     print('no more tries')
 


#BUILDING A CAR GAME

command = ""                                # kaya " " kasi depende kung ano ang i tytype, walang exact value yung variable
started = False



while True: #command != "quit":         pinalitan ng TRUE kase it makes sure the loop always runs until we choose to stop it with break
    command = input("> ").lower()           #.lower() para hindi paulit ulit yung .lower sa comamnd
    if command == "start":
        if started:
            print ("the car is already started")
        else:
            started = True
            print ("car started...")            #need i double check kung naka aling yung print kasi minsan magulo hahah
    elif command== "stop":
         if not started:
            print("the car is already at stop.")
         else:
            started = False
            print ("the car has stopped")
    elif command == "help":
        print ('''  
        start - to start the car
        stop - to stop the car 
        quit - to quit  ''' )
    elif command == "quit":
        print (" thank you for using!")
        break
        
    else: 
        print ("sorry i dont understand that.")

#test kung mag rereflect


