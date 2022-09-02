# 608-mod3
Notes and exercises for Module 3

Chapter 4 Notes: 

Defining functions: 
- Custom functions that you create yourself. 
- Function definition - begins with def keyword followed by function name, set of paranetheses and a colon. This shows you the parameter list, comma separated representing the data that the function needs to perform its task. 
- Can add a Docstring after colon that explains functions purpose. 
- Finally, after executing the return line returns the answer to the user. 
- To access a functions docstring, write functionname? or functionname?? to include source code. 

Functions with multiple parameters: 
- Take in specified values through a comma-separated list. 

Random-Number Generation:
- Random module - import random 
- randrange function generates an integer from the first argument up to but not including second argument. 
- randrange generate pseudorandom numbers, based on an internal calculation that begins with a numeric value known as a seed. 
- You can use random.seed to generate a seed number and test for logic errors. 
- Tuple = an immutable sequence of values. 

Python Standard Library: 
- Package groups related modules. 
- List of common used mmodules on page 132

Math Module Functions: 
- Math module defines functions for performing various common mathematical calculations. 
- Functions within this module are on page 133

Using Ipython tab completion for discovery: 
- Tab completion - a discovery feature that speeds your codind and learning process. 
- Can view math identifiers by using math.<Tab>
- Uses CamelCase. 
  
Default Parameter Values: 
- You can specify that a parameter has a default parameter value. It will automatically insert if inputs aren't taken in.
- If multiple inputs are asked for and only one is given, input will take first parameters slot, and autofill other parameters. 
  
Keyword Arguments:
- Use keyword arguments to pass arguments in any order. 
- IE: def rectangle_area(length, width): uses two keyword arguments. 
  
Arbitrary Argument lists
- Functions with arbitrary argument lists, can recieve any number of arguments
- Min and max for example. 
- Using *args allows you to recieve any number of arguments. 
- The * operator, when applied to an iterable argument in a function, upacks the elements in a list. 
  
Methods: Functions that Belong to Objects
- A Method is a function that you call on an object using the form object_name.method_name(arguments)
  
Scope Rules:
- Each identifier has a scope that determines where you can use it in your program. 
- A Local Variable's identifier has local scope ie only used within the function. 
- Identifiers defined outside of a function have global scope - functions, variables, and classes. 
- can use global statement to declare a variable as global. 
  
import: Deeper look
- Can import multiple modules using comma separated list. 
- Can import all identifiers defined in a module with a wildcard import of the form: from modulename import*
- You can use as to simplify a modules name
  import statistics as stats

Passing Arguments to Functions: Deeper Look 
- pass_by_value: the called function recieves a copy of the arguments value and works exclusively with that copy
- pass_by_reference: the called function can access the arguments value in the caller directly and modify the value if it's mutable. 
- can use id function to obtain a unique int value identifying that object. 
- the is operator returns true if it's two operands have the same identity. 

Function-Call Stack: 
- Stacks are known as last-in, first-out data structures - that last item pushed onto the stack is the first item popped out from the stack. 
- The function call stack supports the function call/return mechanism. 
- For each function call, the interpreter pushes an entry called a stack frame that contains the return location. 
- If a function-call stack runs out of memory it creates a fatal error known as stack overflow. 
- Principle of least privelege: says that code should be granted only the amount of privelege and access that it needs to accomplish its designated task, and no more. 
  
Functional-Style Programming:
- Pure functions: result depends only on the argument you pass to it. 
  
Intro to Data Science: Measures of Dispersion
- Variance: Squaring the difference of each value helps to identify outliers. Used as statistics.pvariance
- Standard Deviation: Square root of the variance. Used as statistics.pstdev
  - The smaller the variance and standard deviation, the closer the data values are to the mean and the less overall dispersion. 
  
  
  
  
  
