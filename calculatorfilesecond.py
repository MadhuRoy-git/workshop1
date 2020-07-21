
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

with open("step_2_goto.txt", 'r') as f:
    first_line = f.readline()
    inputs = first_line.split( )
        if inputs[0] == 'goto' and inputs[1] != 'calc':
            goto inputs[1]
        if inputs[0] == 'calc':
            result = operation(inputs[1], inputs[2], inputs[3])


    list_of_lines = []
    list_of_lines = f.read().splitlines()
    for line in list_of_lines :
        inputs = line.split( )
        if inputs[0] == 'goto' and inputs[1] != 'calc':
            goto inputs[1]
    sum = 0
    for line in list_of_lines :
        inputs = line.split( )
        result = operation(inputs[1], inputs[2], inputs[3])
        sum = sum + result
    print (sum)
