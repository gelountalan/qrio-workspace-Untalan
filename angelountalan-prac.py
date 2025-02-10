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

course = 'Python for beginners'
# print (len(course))                                        #para malaman ang length ng value ng variable
# print (course.lower())
# print (course.find('f')                                    #kapag wala yung hinahanap -1 lalabas
# print (course.replace('beginners', 'not beginners'))       #case sensitive ang python kaya dapat double check lagi
# print ('Python' in course)                                   # in = boolean value = do we have it or not. TRUE OR FALSE








#ARITHMETIC OPERATIONS


