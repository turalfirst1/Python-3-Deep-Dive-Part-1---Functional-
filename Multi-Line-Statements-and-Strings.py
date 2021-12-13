# Python program:
#   physical lines of code     end with a newline character
#       logical lines of code  end with a logical NEWLINE token
#           tokenized

# physcial newline vs logical newline

# sometimes, physical newlines are ignored
# in order to combine multiple physcial lines
# into a single logical line of code
# terminated by a logical NEWLINE token

# Conversion can be implicit or explicit

# Implicit:

# Expressions in:
# list literals : []
# tuple literals : ()
# dictionary literals: {}
# set literals: {}
# function arguments/parameters

# Implicit physical lining supports inline comments

new_list = [1,
            2,
            3]

new_list_with_a_comment = [1, # item 1
                           2, # item 2
                           3 # item 3
                            ]

def my_func(a,
            b, # comment
            c):
    print(a,b,c)

my_func(10, #comment
        20, 30 )

# Explicit

# You can break up statements over multiple lines explicitly, by using the \ (backslash) character
# Multi-line statements are not implicitly converted to a single logical line.

#if a \
#    and b \
#    and c:

# Comments cannot be a part of a statement, not even a multi-line statement

# Multi-string-literals. Multi-line string literals can be created using triple delimeters ('single or " double)

'''This is a
multi - line string'''

"""This is a
multi-line string"""

# Be aware that non-visible characters such as newlines, tabs, etc. are actually part of the string - basically
# anything you type.

# You can use escaped characters (e.g. \n \t), use string formatting, etc.

# A multi-line string is just a string.

# Multi-line strings are not comments, although they can be used as such, especially with special comments called
# docstrings.

a = [1,2,3]

a = [1,2,
     3,4,5]

a = [1, # item 1
     2 ]

a = (1, # item 1
     2, # item 2
     3)

a = {'key1': 1, # value 1
     'key2': 2 # value for key 2
    }

def my_func(a, # This is used to indicate ...
            b, # Comment
            c):
    print(a,b,c)

my_func(10,
        20,
        30)

a = 10
b = 20
c = 30

if a > 5 \
and b > 10 \
and c > 20:
    print('yes')


a = '''This is a string'''

a = '''this
is a string'''

a = '''this
    is a string
        that is created over multiple lines'''

print(a)

a = '''some items:
        1. item 1
        2. item 2'''

print(a)

def my_func():
    a = '''a multi-line string
    that is indented in the second line'''
    return a

print(my_func())