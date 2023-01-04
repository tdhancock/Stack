''' This project is a infix to postfix converter using stack'''

from stack import Stack

def in2post(infix):
    '''Check for Value or Syntax Errors'''
    if type(infix) != str:
        raise ValueError
    if not str(eval(infix)):
        raise SyntaxError

    #Initialize result and Stack
    result = []
    s_adt = Stack()
    count = 0
    #Loop through string
    for i in infix:

        #If a # append to result
        if isOperand(i):
            result.append(i)

        #if a left paren push to stack
        elif i == '(':
            s_adt.push(i)

        #if a right paren check for left paren
        elif i == ')':
            while(not s_adt.isEmpty() and s_adt.top() != '('):
                count += 1
                a_val = s_adt.pop()
                result.append(a_val)

            if(not s_adt.isEmpty() and s_adt.top() != '('):
                return -1
            s_adt.pop()

        else:
            while(not s_adt.isEmpty() and not_greater(i,s_adt) ):
                result.append(s_adt.pop())
            s_adt.push(i)

    #push items to result
    while not s_adt.isEmpty():
        result.append(s_adt.pop())
    result =  "".join(result)
    return result

def isOperand(char):
    '''Checks if char is in num'''
    num = "1234567890"
    if char in num:
        return True
    return False

def isOperator(char):
    '''Checks if char is in operators'''
    operators = "+-*/^"
    if char in operators:
        return True
    return False

def not_greater(i,s):
    '''Checks who has precedence'''
    precedence = {'+':1, '-':1, '*':2, '/':2, '^':3}
    try:
        a_val = precedence[i]
        b_val = precedence[s.top()]
        return True if a_val <= b_val else False
    except KeyError:
        return False

def eval_postfix(exp):
    '''Evaluates postfix notation'''
    if exp is None:
        raise ValueError
    i = 0
    num = "1234567890"
    operators = "+-*/^"
    num_count = 0
    op_count = 0
    length = len(exp)
    if length >= 2:
        if (exp[0] not in num) and (exp[1] not in num):
            raise SyntaxError
        if exp[-1] not in operators:
            raise SyntaxError
        while i < len(exp):
            if exp[i] in num:
                num_count += 1
            if exp[i] in operators:
                op_count += 1
            i += 1

        if (num_count - op_count) != 1:
            raise SyntaxError

    x_adt = Stack()
    exp = exp.replace(' ', '')
    exp = exp.replace('(', '')
    exp = exp.replace(')', '')
    for i in exp:
        if i.isdigit():
            x_adt.push(i)
        else:
            val1= x_adt.pop()
            val2= x_adt.pop()
            x_adt.push(str(eval(val2 + i + val1)))

    return float(x_adt.pop())

def main():
    with open("data.txt", "r") as f:
        x_adt = list(f.read().replace(" ", "").split("\n"))
        #x = [i for i in f.read().replace(" ", "").split("\n")]
        if x_adt[-1] == "":
            x_adt.pop()

    w_file = open("Results.txt", "w")

    for item in x_adt:
        w_file.write(f'Infix: {item}\n')
        post = in2post(item)
        w_file.write(f'Postfix: {post}\n')
        result = eval_postfix(post)
        w_file.write(f'Answer: {result}\n\n')

if __name__ == "__main__":
    main()
