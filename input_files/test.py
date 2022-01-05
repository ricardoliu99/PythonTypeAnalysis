# simple if
def simple_if():
    if 1 > 0:
        x = 1
# 'simple_if|0': {'x': {5: {<class 'int'>}, 5.5: {<class 'int'>}}


# if with assignment
def simple_if_assign():
    x = 'str'
    if 1 > 0:
        x = 1
# 'simple_if_assign|0': {'x': {10: {<class 'str'>}, 12: {<class 'int'>}, 12.5: {<class 'str'>, <class 'int'>}}


# if else with assignment
def simple_if_else_assign():
    x = 'str'
    if 1 > 0:
        x = 1
    else:
        x = 1.23
# 'simple_if_else_assign|0': {'x': {18: {<class 'str'>}, 20: {<class 'int'>},
# 22: {<class 'float'>}, 22.5: {<class 'str'>, <class 'float'>, <class 'int'>}}


# if else, however variable is not covered in all branches
def simple_if_else_assign_partial():
    x = 'str'
    if 1 > 0:
        x = 1
    else:
        y = 1.23
# 'simple_if_else_assign_partial|0': {'x': {29: {<class 'str'>}, 31: {<class 'int'>},
# 33.5: {<class 'str'>, <class 'int'>}}, 'y': {33: {<class 'float'>}, 33.5: {<class 'float'>}}


# if with three branches
def if_else_elif():
    if 1 > 0:
        x = 1
    elif 2 > 1:
        x = 1.23
    else:
        x = False
# if_else_elif|0 : {'x': {41: {<class 'int'>}, 43: {<class 'float'>},
# 45: {<class 'bool'>}, 45.5: {<class 'int'>, <class 'float'>, <class 'bool'>}}}


# three branches if with assignment
def if_else_elif_assign():
    x = 't'
    if 1 > 0:
        x = 1
    elif 2 > 1:
        x = 1.23
    else:
        x = False
# if_else_elif_assign|0 : {'x': {52: {<class 'str'>}, 54: {<class 'int'>}, 56: {<class 'float'>},
# 58: {<class 'bool'>}, 58.5: {<class 'int'>, <class 'bool'>, <class 'str'>, <class 'float'>}}}


# nested if branches
def nested_if():
    if 1 > 0:
        if -1 < 0:
            y = 1
        else:
            y = 'str'
        x = 1
    elif 2 > 1:
        x = 1.23
    else:
        x = False
# nested_if|0 : {'y': {67: {<class 'int'>}, 69: {<class 'str'>}, 69.5: {<class 'str'>, <class 'int'>},
# 74.5: {<class 'str'>, <class 'int'>}}, 'x': {70: {<class 'int'>}, 72: {<class 'float'>},
# 74: {<class 'bool'>}, 74.5: {<class 'int'>, <class 'float'>, <class 'bool'>}}}


# nested if branches with assign
def nested_if_with_assign():
    x = 't'
    y = False
    if 1 > 0:
        y = 1.2
        if -1 < 0:
            y = 1
        else:
            y = 'str'
        x = 1
    elif 2 > 1:
        x = 1.23
    else:
        x = False
# nested_if_with_assign|0 : {'x': {82: {<class 'str'>}, 90: {<class 'int'>}, 92: {<class 'float'>},
# 94: {<class 'bool'>}, 94.5: {<class 'int'>, <class 'bool'>, <class 'str'>, <class 'float'>}},
# 'y': {83: {<class 'bool'>}, 85: {<class 'float'>}, 87: {<class 'int'>}, 89: {<class 'str'>},
# 89.5: {<class 'int'>, <class 'float'>, <class 'str'>},
# 94.5: {<class 'int'>, <class 'float'>, <class 'bool'>, <class 'str'>}}}


# nested if branches with assign scope testing
def nested_if_with_assign_scope():
    x = 't'
    y = False
    if 1 > 0:
        if -1 < 0:
            y = 1
        else:
            y = 'str'
        x = 1
    elif 2 > 1:
        x = 1.23
    else:
        x = False
# nested_if_with_assign_scope|0 : {'x': {104: {<class 'str'>}, 111: {<class 'int'>}, 113: {<class 'float'>},
# 115: {<class 'bool'>}, 115.5: {<class 'int'>, <class 'bool'>, <class 'str'>, <class 'float'>}},
# 'y': {105: {<class 'bool'>}, 108: {<class 'int'>}, 110: {<class 'str'>},
# 110.5: {<class 'int'>, <class 'bool'>, <class 'str'>}, 115.5: {<class 'int'>, <class 'bool'>, <class 'str'>}}}


# for loop, while loop, try catch nested with if. 'in' works the same for list, set, tuple, and string.
def for_loop_while_loop_try_catch_if_nesting():
    for i in [1, 'str']:
        while 1 > 0:
            try:
                x = 1
            except:
                x = 'str'
            finally:
                x = 1.23
            if 1 > 0:
                x = False
# for_loop_while_loop_try_catch_if_nesting|0 : {'i': {124: {<class 'int'>, <class 'str'>}},
# 'x': {127: {<class 'int'>}, 129: {<class 'str'>}, 131: {<class 'float'>},
# 133: {<class 'bool'>}, 133.5: {<class 'float'>, <class 'bool'>}}}


# for loop iterator with function call
def for_loop_iter():
    for i in range(1):
        y = 1
# for_loop_iter|0 :  {'i': {147: 'Ambiguous'}, 'y': {148: {<class 'int'>}}}


# for loop iterator with variable
def for_loop_iter_var():
    x = [1, 2]
    for i in x:
        y = 1
# for_loop_iter_var|0 :  {'x': {148: {<class 'list'>}}, 'i': {149: 'Ambiguous'}, 'y': {150: {<class 'int'>}}}


# unary operations not, ~, +, -
def unary():
    x = -1
    y = -x
    x = not x
    x = ~x
    x = +x
# unary|0 :  {'x': {156: {<class 'int'>}, 158: {<class 'bool'>}, 159: {<class 'int'>},
# 160: {<class 'int'>}}, 'y': {157: {<class 'int'>}}}


# binary operations +, -, *, /, %, **,
def binary():
    x = 1
    y = 2
    x = x ** y
    a = x + 1
    b = x + y
    x = [1, 2]
    x = x * y
    x = x + x
    x = x + y
# binary|0 :  {'x': {167: {<class 'int'>}, 169: {<class 'int'>}, 172: {<class 'list'>}, 173: {<class 'list'>},
# 174: {<class 'list'>}, 175: 'Error'}, 'y': {168: {<class 'int'>}},
# 'a': {170: {<class 'int'>}}, 'b': {171: {<class 'int'>}}}


# boolean operations and, or
def bool_op():
    x = 1
    x = x and x
    y = 0
    x = x and y
    y = [1, 2]
    y = y or x
# bool_op|0 :  {'x': {183: {<class 'int'>}, 184: {<class 'int'>}, 186: {<class 'int'>}},
# 'y': {185: {<class 'int'>}, 187: {<class 'list'>}, 188: {<class 'list'>}}}


# multi assign
def assign():
    a = b = c = d = 1
# assign|0 :  {'a': {195: {<class 'int'>}}, 'b': {195: {<class 'int'>}},
# 'c': {195: {<class 'int'>}}, 'd': {195: {<class 'int'>}}}


# aug assign
def aug_assign():
    b = 1.2
    a = 1
    a += b
# aug_assign|0 :  {'b': {202: {<class 'float'>}}, 'a': {203: {<class 'int'>}, 204: {<class 'float'>}}}


# local function call
def foo():
    return 1


def local_fn():
    x = foo()
# foo|0 :  {'return': {210: {<class 'int'>}}}
# local_fn|0 :  {'x': {214: {<class 'int'>}}}


# static function call
def static_fn():
    a = [1, 2]
    x = len(a)
# static_fn|0 :  {'a': {221: {<class 'list'>}}, 'x': {222: {<class 'int'>}}}


# library function call
def lib_fn():
    x = numpy.random.randint(2)
# lib_fn|0 :  {'x': {228: {<class 'int'>}}}


# parameter type inference
def foo(a):
    a = a + [1, 2]
    return 1
# foo|1 :
# {'a': {
# -1: {<class 'list'>, <class 'set'>, <class 'str'>, <class 'float'>, <class 'bool'>,
# <class 'tuple'>, <class 'int'>, <class 'dict'>},
# 234: {<class 'list'>}},
# 'return': {235: {<class 'int'>}}}

# object function call
def obj_fn():
    x = "a a a".split(" ")
# obj_fn|0 :  {'x': {245: {<class 'list'>}}}

# chaining function calls
def foooo():
    return [1,2]


def chain_fn():
    x = "a a a".split(" ").index("a")
    i = list(numpy.random.randint(2))
    z = foooo().index(1)
# foooo|0 :  {'return': {250: {<class 'list'>}}}
# chain_fn|0 :  {'x': {254: {<class 'int'>}}, 'i': {255: {<class 'list'>}}, 'z': {256: {<class 'int'>}}}


# overloading
def fn_ov():
    return 1


def fn_ov(a):
    return 1.2


def fn_ov(a, b):
    return True
# fn_ov|0 :  {'return': {263: {<class 'int'>}}}
# fn_ov|1 :  {'a': {-1: {<class 'list'>, <class 'set'>, <class 'str'>, <class 'float'>, <class 'bool'>,
# <class 'tuple'>, <class 'int'>, <class 'dict'>}}, 'return': {267: {<class 'float'>}}}
# fn_ov|2 :  {'a': {-1: {<class 'list'>, <class 'set'>, <class 'str'>, <class 'float'>, <class 'bool'>,
# <class 'tuple'>, <class 'int'>, <class 'dict'>}}, 'b': {-2: {<class 'list'>, <class 'set'>, <class 'str'>,
# <class 'float'>, <class 'bool'>, <class 'tuple'>, <class 'int'>, <class 'dict'>}}, 'return': {271: {<class 'bool'>}}}

