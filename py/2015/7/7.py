import re
from functools import cache

f = '7.in'
# f = '7_test.in'
D = open(f).read().strip()

V = {}
for line in D.splitlines():
    expr, node = line.split('->')
    expr = expr.strip()
    node = node.strip()
    if 'NOT' in expr:
        expr = ('~', expr[4:])
    elif 'AND' in expr:
        a, b = expr.split('AND')
        a, b = a.strip(), b.strip()
        expr = ('&', [a, b])
    elif 'OR' in expr:
        a, b = expr.split('OR')
        a, b = a.strip(), b.strip()
        expr = ('|', [a, b])
    elif 'LSHIFT' in expr:
        a, b = expr.split('LSHIFT')
        a, b = a.strip(), b.strip()
        expr = ('<<', [a, b])
    elif 'RSHIFT' in expr:
        a, b = expr.split('RSHIFT')
        a, b = a.strip(), b.strip()
        expr = ('>>', [a, b])
    V[node] = expr

print(V)

def eval_value(n):
    if '0' <= n[0] <= '9':  # number
        return int(n)
    return eval_node(n)

def as_uint16(val):
    return val & 0xFFFF

cache = {}
def eval_node(node):
    if node in cache:
        return cache[node]
    n = V[node]
    if isinstance(n, tuple):
        op = n[0]
        vals = n[1]
        if op == '~':
            val = vals
            cache[node] = as_uint16(~eval_value(val))
        elif op == '&':
            cache[node] = as_uint16(eval_value(vals[0]) & eval_value(vals[1]))
        elif op == '|':
            cache[node] = as_uint16(eval_value(vals[0]) | eval_value(vals[1]))
        elif op == '>>':
            cache[node] = as_uint16(eval_value(vals[0]) >> eval_value(vals[1]))
        elif op == '<<':
            cache[node] = as_uint16(eval_value(vals[0]) << eval_value(vals[1]))
    else:
        cache[node] = as_uint16(eval_value(n))
    return cache[node]

val_a = eval_value('a')
print(val_a)

cache.clear()
V['b'] = str(val_a)
val_a2 = eval_value('a')
print(val_a2)