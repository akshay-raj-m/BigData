# Q1. Why do we call Python as a general purpose and high-level programming language? Ans1. Python is called general purpose because it can used to design and develop a wide variety of applications, across multiple domain. High-level programming language means it's more user-friendly. Coding in Python is like writing a story in English.

# Q2. Why is Python called a dynamically typed language? Ans2. Dynamically typed language means that variables are checked against types only when the program is executing. We don't need to declare the variable type, the interpreter automatically interprets it.

# Q3. List some pros and cons of Python programming language?

# Ans3. Pros:

# Easy to use
# Easy to integrate
# Multi-paradigm approach
# High library support
# Cons:

# Slow speed of execution compared to C,C++
# Absence from mobile computing and browsers
# Q4. In what all domains can we use Python?

# Ans4.

# Graphic design, image processing applications, Games, and Scientific/ computational Applications
# Web frameworks and applications
# Database Access
# Language Development
# Prototyping
# Software Development
# Data Science and Machine Learning
# Scripting
# Q5. What are variable and how can we declare them?

# Ans5. A variable is a symbolic name that is a reference or pointer to an object. Once an object is assigned to a variable, you can refer to the object by that name.

# var = 17
# Q6. How can we take an input from the user in Python?

# Ans6. By using input() function.

# Q7. What is the default datatype of the value that has been taken as an input using input() function? Ans7. string

# Q8. What is type casting?

# Ans8. Type casting means changing the datatype of the variable. We can only type casting the datatype having higher bit value to the lower bit value.

# Q9. Can we take more than one input from the user using single input() function? If yes, how? If no, why?

# Ans9. Yes.

x, y, z = input("Enter three values: ").split(",")
print("Total number of students: ", x)
print("Number of boys is : ", y)
print("Number of girls is : ", z)
print()
x = [int(x) for x in input("Enter multiple value: ").split(",")]
print("Number of list is: ", x) 
# Q10. What are keywords?

# Ans10. Keywords in Python are reserved words that can not be used as a variable name, function name, or any other identifier.

# Q11. Can we use keywords as a variable? Support your answer with reason.

# Ans11. Yes we can but we shoudn't as it will override the properties of the keyword.

# Q12. What is indentation? What's the use of indentaion in Python?

# Ans12. Indentation is the whitespace used in Python. Indentation is used to create block of statement.

# Q13. How can we throw some output in Python?

# Ans13. Using print() function.

# Q14. What are operators in Python?

# Ans14. Symbols or keywords used to perform certain operations on values or variable are known as operators. There are different types of operators like

# Arithmetic operators
# Comparison Operators
# Logical Operators
# Bitwise Operators
# Assignment Operators
# Q15. What is difference between / and // operators?

# Ans15. / is used for float division and // is used of floor (integer) division.

# Q16. Write a code that gives following as an output.

# Ans16.

# "iNeuron"*3
# Q17. Write a code to take a number as an input from the user and check if the number is odd or even. Ans17.

# num = float(input("Enter a number: "))
if num%2 == 0:
  print(f"{num} is even")
else:
  print(f"{num} is odd")
# Q18. What are boolean operator? Ans18. True , False , not , and , or are the only built-in Python Boolean operators.

# Q19. What will the output of the following?

# 1 or 0

# 0 and 0

# True and False and True

# 1 or 0 or 0
# Ans.19 Output of the following code will be

# 1 or 0 -> 1
# 0 and 0 -> 0
# True and False and True -> False
# 1 or 0 or 0 -> 1
# Q20. What are conditional statements in Python?

# Ans20. In large projects we have to control the flow of execution of our program and we want to execute some set of statements only if the given condition is satisfied, and a different set of statements when it’s not satisfied.

# Q21. What is use of 'if', 'elif' and 'else' keywords?

# Ans21. if is the first condition check for the condition.

# if "if" is False then elif's condition is checked.

# else is checked when all the upper condition fails.

# Q22. Write a code to take the age of person as an input and if age >= 18 display "I can vote". If age is < 18 display "I can't vote". Ans22.

# age = int(input("Enter you age: "))
# if age >= 18:
#     print("I can vote")
# else:
#     print("I can't vote") 
# Q23. Write a code that displays the sum of all the even numbers from the given list.

# numbers = [12, 75, 150, 180, 145, 525, 50]
# Ans23.

# numbers = [12, 75, 150, 180, 145, 525, 50]
# add = 0
# for num in numbers:
#   if num%2 == 0:
#     add = add+num
#   else:
#     continue
# print(add) 
# Q24. Write a code to take 3 numbers as an input from the user and display the greatest no as output. Ans24.

x, y, z = input("Enter 3 numbers seprated by comma: ").split(",")
if int(x) > int(y) and int(x) > int(z):
  print(f"{x} is greatest")
elif int(y) > int(z):
  print(f"{y} is greatest")
else:
  print(f"{z} is greatest")
# Q25. Write a program to display only those numbers from a list that satisfy the following conditions

# The number must be divisible by five

# If the number is greater than 150, then skip it and move to the next number

# If the number is greater than 500, then stop the loop

# numbers = [12, 75, 150, 180, 145, 525, 50]
# Ans25.

numbers = [12, 75, 150, 180, 145, 525, 50]
lst = []
for num in numbers:
  if num > 150:
    if num > 500:
      break
  elif num%5==0:
    lst.append(num) 

# print(lst)
# Q26. What is a string? How can we declare string in Python?

# Ans26. In Python, Strings are arrays of bytes representing Unicode characters.

# Q27. How can we access the string using its index?

# Ans27. Sqaure brackets can used to access the elements of the string.

# Q28. Write a code to get the desired output of the following

# string = "Big Data iNeuron"
# desired_output = "iNeuron"
# Ans28.

# string[9:16]
# Q29. Write a code to get the desired output of the following

# string = "Big Data iNeuron"
# desired_output = "norueNi"
# Ans29.

# string[15:8:-1]
# Q30. Resverse the string given in the above question. Ans30.

# string[::-1]
# Q31. How can you delete entire string at once?

# Ans31. We can delete the entire string at once by using del keyword.

# str1 = "Hello"
# del(str1)
# Q32. What is escape sequence?

# Ans32. The "backslash ()" character as an escape character. In other words, it has a special meaning when we use it inside the strings. As the name suggests, the escape character escapes the characters in a string for a brief moment to introduce unique inclusion.

# Q33. How can you print the below string?

# 'iNeuron's Big Data Course'
# Ans33. 'iNeuron's Big Data Course'

# Q34. What is a list in Python?

# Ans34. Python list are dynamically sized array, declared in languages like C++ and Java. A list is a collection of things, enclosed in [ ] and separated by commas.

# Q35. How can you create a list in Python?

# Ans35. You can create a list by opening and closing the square brackets.

# Q36. How can we access the elements in a list?

# Ans36. We can access the elements in a list by indexing.

# Q37. Write a code to access the word "iNeuron" from the given list.

# lst = [1,2,3,"Hi",[45,54, "iNeuron"], "Big Data"]
# Ans37.

# lst = [1,2,3,"Hi",[45,54, "iNeuron"], "Big Data"]
# lst[4][2]
# Q38. Take a list as an input from the user and find the length of the list.

# Ans38.

n = input("Enter number of elements seprated by space: ").split(" ")
print(len(n))
# Q39. Add the word "Big" in the 3rd index of the given list.

# lst = ["Welcome", "to", "Data", "course"]
# Ans39.

lst = ["Welcome", "to", "Data", "course"]
lst.insert(2, "Big")
# Q40. What is a tuple? How is it different from list?

# Ans40. Tuple is a collection of Python objects much like a list. The sequence of values stored in a tuple can be of any type, and they are indexed by integers. Tuples are immutable where as list are mutable. We can also faster through the tuples than the list.

# Q41. How can you create a tuple in Python?

# Ans41. We can create tuple using round brackets ().

# Q42. Create a tuple and try to add your name in the tuple. Are you able to do it? Support your answer with reason.

# Ans42. No, I can't as tuples are immutable. The work around is it typecast tuple to list and then append.

# tup = ()