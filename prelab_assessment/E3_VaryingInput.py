#function receives a parameter -- could be a number or a string
#if number, it's the radius of a circle and calc the area
#if string, return the first letter of the string
import math

def param_to_output(param):
    if isinstance(param, (int, float)): #takes in numbers as int or float
        area = (math.pi)*((param)**2)
        return area
    elif isinstance(param, str):
        return param[0] #the first letter
    else:
        print("Invalid input type, please enter a number or a string")
    
#test cases
input = "hello"
#input = 5, 5.01, "sweet potato", ["earth", "mars", "jupyter"]
print(f"Input: {input} --> Output: {param_to_output(input)}")


#learned
    #isinstance --> tells you true or false to the type listed
    #type() --> tells you the variable type
    #f before string: f-strings, allow you to replace variables in curly brackets with their found values

