import turtle

screen = turtle.Screen()
screen.setup(500, 500)
screen.title("24 Game Solver - PythonTurtle.Academy")
turtle.hideturtle()
turtle.speed(0)
turtle.up()


def permutation(a):
    if len(a) == 1: return [[a[0]]]
    res = permutation(a[1:])
    r = []
    for x in res:
        # need to insert n into x: into all possible position
        for i in range(len(x) + 1):
            y = x.copy()
            y.insert(i, a[0])
            if y not in r:
                r.append(y)
    return r


op = ['+', '−', '×', '÷']


def evaluate(a):
    v = []
    for x in a:
        if type(x) is int:
            v.append(x)
        else:
            num2 = v.pop()
            num1 = v.pop()
            if x == '+':
                v.append(num1 + num2)
            elif x == '−':
                v.append(num1 - num2)
            elif x == '×':
                v.append(num1 * num2)
            else:
                if num2 != 0:
                    v.append(num1 / num2)
                else:
                    return 0
    return v[0]


class tree_node:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right


def inorder(root):
    if type(root.value) is int: return str(root.value)
    if type(root.left.value) is not int:
        left = '(' + inorder(root.left) + ')'
    else:
        left = inorder(root.left)
    if type(root.right.value) is not int:
        right = '(' + inorder(root.right) + ')'
    else:
        right = inorder(root.right)
    return left + root.value + right


def convert_to_infix(a):
    # convert to infix
    # convert to tree first
    v = list()
    for x in a:
        if type(x) is int:
            v.append(tree_node(x, None, None))
        else:
            t2 = v.pop()
            t1 = v.pop()
            v.append(tree_node(x, t1, t2))
    return inorder(v[0])


def twentyfour(a):
    # postfix
    # try n,n,n,n, p,p,p
    for i in range(4):
        for j in range(4):
            for k in range(4):
                b = a.copy()
                b.append(op[i])
                b.append(op[j])
                b.append(op[k])
                v = evaluate(b)
                if v == 24.0:
                    return (convert_to_infix(b))

    # try n,n,n,p,p,n,p
    for i in range(4):
        for j in range(4):
            for k in range(4):
                b = a[:3]
                b.append(op[i])
                b.append(op[j])
                b.append(a[3])
                b.append(op[k])
                v = evaluate(b)
                if v == 24.0:
                    return (convert_to_infix(b))

    # try n,n,n,p,n,p,p
    for i in range(4):
        for j in range(4):
            for k in range(4):
                b = a[:3]
                b.append(op[i])
                b.append(a[3])
                b.append(op[j])
                b.append(op[k])
                v = evaluate(b)
                if v == 24.0:
                    return (convert_to_infix(b))

    # try n,n,p,n,p,n,p
    for i in range(4):
        for j in range(4):
            for k in range(4):
                b = a[:2]
                b.append(op[i])
                b.append(a[2])
                b.append(op[j])
                b.append(a[3])
                b.append(op[k])
                v = evaluate(b)
                if v == 24.0:
                    return (convert_to_infix(b))
    # try n,n,p,n,n,p,p
    for i in range(4):
        for j in range(4):
            for k in range(4):
                b = a[:2]
                b.append(op[i])
                b.append(a[2])
                b.append(a[3])
                b.append(op[j])
                b.append(op[k])
                v = evaluate(b)
                if v == 24.0:
                    return (convert_to_infix(b))
    return ''


while True:
    fournumbers = []
    while len(fournumbers) != 4:
        numbers = screen.textinput("24 Game Solver", "Enter four numbers separated by spaces: ")
        fournumbers = list(map(int, numbers.split()))
    p = permutation(fournumbers)
    foundsolution = False
    turtle.clear()
    for a in p:
        r = twentyfour(a)
        if len(r) > 0:
            turtle.goto(0, 0)
            turtle.color('royal blue')
            turtle.write(r, font=('Courier', 45, 'bold'), align='center')
            foundsolution = True
            break
    if not foundsolution:
        turtle.color('red')
        turtle.write("No solution", font=('Courier', 45, 'bold'), align='center')