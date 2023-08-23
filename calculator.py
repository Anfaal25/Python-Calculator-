# calculator.py
# NAME: Anfaal Mahbub 
# ENDG 233 F21
# UCID - 30140009
# A terminal-based calculator application for determining the result of a mathematical expression containing three values and two operators.





 


print('Welcome to The Calculator.')                                                        #User is greeted to The Calculator.
print('Please enter your first value = ', end = '')                                        #User is the prompted to input the integers and operators.
first_value = int(input())
print('Please enter your first operator = ', end = '')
first_operator = input()
print('Please enter your second value = ', end = '')
second_value = int(input())
print('Please enter your second operator = ', end ='')
second_operator = input()
print('Please enter your third value = ', end ='')
third_value = int(input())


print('Your final expression: ', end ='')                                                 #Program prints the users entire input as an expression.
print(first_value, first_operator, second_value, second_operator, third_value)



#All that follows are the different variations of the pair of operators that could potentially be inputted by the user.

#Program then calculates the final answer by referencing the inputted operators by the user.


if first_operator == '+' and second_operator == '/':                                      #Scenario where the first operator is (+) and the second operator is (/).
    if third_value == 0:                                                                  #As the possibility of the user inputing the value 0 exists, the program has an output designed to meet this scenario. 
        print('Math Error')
    else:
        final_answer = (second_value // third_value ) + first_value                       #Floor division is used here as the requirement is to show the final answer as an integer. 
        print('Your final answer =', final_answer) 

elif first_operator == '+' and second_operator == '*':                                    #Scenario where the first operator is (+) and the second operator is (*). 
    final_answer = first_value + (second_value * third_value)                             #This ensures that the calculator always follows the right order of calculations and thus giving an answer. 
    print('Your final answer =', final_answer)    
elif  first_operator == '-' and second_operator == '*':                                   #Scenario where the first operator is (-) and the second operator is (*).
    final_answer = ( -1 * second_value * third_value )   + first_value 
    print('Your final answer =', final_answer)
elif first_operator == '/' and second_value == '-':                                       #Scenario where the first operator is (/) and the second operator is (-).
    if second_value == 0:                                                                 #This is a scenario where the user tries to divide by zero. 
        print('Math Error')
    else:
        final_answer = (first_value // second_value ) - third_value                       #Floor division is used here as the requirement is to show the final answer as an integer. 
        print('Your final answer =', final_answer)       
elif first_operator == '-' and second_operator == '-':                                    #Scenario where the first operator is (-) and the second operator is (-).
    final_answer = first_value - second_value - third_value
    print('Your final answer =', final_answer)    
elif first_operator == '/' and second_operator == '*' :                                   #Scenario where the first operator is (/) and the second operator is (*).
    if second_value == 0:                                                                 #This is a scenario where the user tries to divide by zero.
        print('Math Error')
    else:
        final_answer = first_value // (second_value * third_value )                       #Floor division is used here as the requirement is to show the final answer as an integer. 
        print('Your final answer =', final_answer)        
elif first_operator == '/' and second_operator =='+':                                     #Scenario where the first operator is (/) and the second operator is (+).
    if second_value == 0:                                                                 #This is a scenario where the user tries to divide by zero.
        print('Math Error')
    else:
        final_answer = (first_value // second_value ) + third_value                       #Floor division is used here as the requirement is to show the final answer as an integer. 
        print('Your final answer =', final_answer)       
elif first_operator == '*' and second_operator =='*':                                     #Scenario where the first operator is (*) and the second operator is (*).
    final_answer = (first_operator * second_operator) * third_value
    print('Your final answer =', final_answer)  
elif first_operator == '*' and second_operator == '-':                                    #Scenario where the first operator is (*) and the second operator is (-).
    final_answer = (first_value * second_value) - third_value
    print('Your final answer =', final_answer)
elif first_operator == '*' and second_operator == '+':                                    #Scenario where the first operator is (*) and the second operator is (+).
    final_answer = (first_value * second_value) + third_value
    print('Your final answer =', final_answer) 
elif first_operator == '*' and second_operator == '/':                                    #Scenario where the first operator is (*) and the second operator is (/).
    if third_value == 0:                                                                  #This is a scenario where the user tries to divide by 0. 
        print('Math Error')                     
    else:
        final_answer = (first_value * second_value) // third_value                        #Floor division is used here as the requirement is to show the final answer as an integer. 
        print('Your final answer =', final_answer) 
elif first_operator == '/' and second_operator == '/' :                                   #Scenario where the first operator is (/) and the second operator is (/).
    if second_value == 0:                                                                 #This is a scenario where the user tries to divide by zero. 
        print('Math Error')
    elif third_value == 0:                                                                #This is a scenario where the user tries to divide by zero. 
        print('Math Error')
    else:    
        final_answer = (first_value // second_value) // third_value                       #Floor division is used here as the requirement is to show the final answer as an integer. 
        print('Your final answer =', final_answer) 
elif first_operator == '-' and second_operator == '/':                                    #Scenario where the first operator is (-) and the second operator is (/).
    if third_value == 0:                                                                  #This is a scenario where the user tries to divide by zero. 
        print('Math Error')
    else:
        final_answer = first_value - (second_value // third_value)                        #Floor division is used here as the requirement is to show the final answer as an integer. 
        print('Your final answer =', final_answer) 
elif first_operator == '+' and second_operator == '-':                                    #Scenario where the first operator is (+) and the second operator is (-).
    final_answer = (first_value + second_value) - third_value
    print('Your final answer =', final_answer) 
elif first_operator == '+'and second_operator == '+':                                     #Scenario where the first operator is (+) and the second operator is (+).
    final_answer = first_value + second_value + third_value
    print('Your final answer =', final_answer) 
elif first_operator == '-' and second_operator == '-':                                    #Scenario where the first operator is (-) and the second operator is (-). 
    final_answer = (first_value - second_value) - third_value
    print('Your final answer =', final_answer) 
elif first_operator == '-' and second_operator == '+':                                    #Scenario where the first operator is (-) and the second operator is (+).
    final_answer = first_value + ((-1 * second_value) + third_value)
    print('Your final answer =', final_answer)     
else:
    print('Please make sure that you have entered the values and/or the operators correctly.')         #This line of code exists if there is a scenario where the user inputs a wrong operator or an operator that the program does not identify. 

