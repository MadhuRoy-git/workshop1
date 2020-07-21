
def operation( number1 , number2 , operator ):
    integer1 = int(number1)
    integer2 = int(number2)
    print('inside operation method')
    if operator == '+' :
        print( integer1 + integer2 )
    if operator == '-' :
        print( integer1 - integer2 )
    if operator == '*' :
        print( integer1 * integer2 )
    if operator == '/' :
        print( integer1 / integer2 )
    if operator == '%' :
        print( integer1 / integer2 )
    if operator == '^' :
        print( integer1 ^ integer2 )


number1 = input("What's the first number? ")
number2 = input("What's the second number? ")
operator = input("What's the operator? ")
operation(number1, number2, operator)
