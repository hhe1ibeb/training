def f(x): return 2*x-3
def g(x, y): return 2*x + y - 7
def h(x, y, z): return 3*x - 2*y + z


stack = []
for symbol in reversed(input().split()):
    stack.append(
        f(stack.pop()) if symbol == 'f'
        else g(stack.pop(), stack.pop()) if symbol == 'g'
        else h(stack.pop(), stack.pop(), stack.pop()) if symbol == 'h'
        else int(symbol)
    )

print(stack.pop())
