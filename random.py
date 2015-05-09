class Node(object):

    def __init__(self, item):
	self.item = item
	self.next = None

class LinkedStack(object):

    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def push(self, item):
        tempNode = Node(item)
        tempNode.next = self.head
        self.head = tempNode

    def pop(self):
        if self.isEmpty(): raise IndexError("can't pop empty stack")
        popNode = self.head
        self.head = self.head.next
        return popNode.item

    def peek(self):
	if self.isEmpty(): raise IndexError("can't pop empty stack")
        return self.head.item

stack = LinkedStack()
expression = raw_input('Expression to Evaluate:\n')

#----------------------------------------------------------------
#infix to RPN (foreign)
LEFT_ASSOC = 0
RIGHT_ASSOC = 1

OPERATORS = {'+' : (0, LEFT_ASSOC),
             '-' : (0, LEFT_ASSOC),
             '*' : (5, LEFT_ASSOC),
             '/' : (5, LEFT_ASSOC),
             '%' : (5, LEFT_ASSOC),
             '^' : (10, RIGHT_ASSOC)}

def isOperator(token):
    return token in OPERATORS.keys()

def isAssociative(token, assoc):
    if not isOperator(token):
        raise ValueError('Invalid token: %s' % token)
    return OPERATORS[token][1] == assoc

def cmpPrecedence(token1, token2):
    if not isOperator(token1) or not isOperator(token2):
        raise ValueError('Invalid tokens: %s %s' % (token1, token2))
    return OPERATORS[token1][0] - OPERATORS[token2][0]

def infixToRPN(tokens):
    out = []
    stackArray = []

    for token in tokens:
        if isOperator(token):

            while len(stackArray) != 0 and isOperator(stackArray[-1]):
                if (isAssociative(token, LEFT_ASSOC)
                    and cmpPrecedence(token, stackArray[-1]) <= 0) or
                    (isAssociative(token, RIGHT_ASSOC)
                    and cmpPrecedence(token, stackArray[-1]) < 0):
                        out.append(stackArray.pop())
                    continue
                break

            stackArray.append(token)
        elif token == '(':
            stackArray.append(token)
        elif token == ')':
            while len(stackArray) != 0 and stackArray[-1] != '(':
                out.append(stackArray.pop())
            stackArray.pop()
        else:
            out.append(token)
    while len(stackArray) != 0:

        out.append(stackArray.pop())
    return out
#--------------------------------------
#expression = '3, 1, +, 6, 4, -, *'
expression = raw_input('Expression to Evaluate: ')


if ', ' in expression:
    expression = expression.split(', ')
elif ' ' in expression:
    expression = expression.split(' ')
else ',':
    expression = expression.split(',')

expression = infixToRPN(expression)

for char in expression:
    if char.isdigit():
        stack.push(char)

    else:
        varOne = int(stack.pop())
        varTwo = int(stack.pop())

        if char == '+':
            stack.push(varTwo + varOne)

        elif char == '-':
            stack.push(varTwo - varOne)

        elif char == '*':
            stack.push(varTwo * varOne)

        else:
            if varOne == 0 or varOne == 0.0:
                raise ZeroDivisionError('division by zero')

            stack.push(varTwo / varOne)

print stack.peek()
