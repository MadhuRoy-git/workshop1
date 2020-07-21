
def operation( operator , number1 , number2 ):
    integer1 = int(number1)
    integer2 = int(number2)
    
    if operator == '+' :
        return ( integer1 + integer2 )
    if operator == '-' :
        return ( integer1 - integer2 )
    if operator == 'x' :
        return ( integer1 * integer2 )
    if operator == '/' :
        return ( integer1 / integer2 )

with open("step_2.txt", 'r') as f:
    list_of_lines = []
    list_of_lines = f.read().splitlines()
    sum = 0
    for line in list_of_lines :
        inputs = line.split( )
        result = operation(inputs[1], inputs[2], inputs[3])
        sum = sum + result
    print (sum)
