# Variable/Identifier names are case-sensitive
# For example, these are all different:
# my_var, my_Var, ham, Ham

# They must follow some rules and should follow some conventions

# Must: start with underscore or letters followed by any number of underscores (_), letters or digits
# They can not be reserved words.

# Conventions: If you have a single underscore this is a convention to indicate "internal use" or "private" objects
# Objects named this way will not get imported by a statement such as: from module import *

# If it uses double underscore which is used to "mangle" class attributes - useful in inheritance chains.

# If both start and end with double underscores, it is used for system-defined names that have a special meaning to
# the interpreter. Don't invent them, stick to the ones pre-defined by Python! For example: __init__

# Other naming conventions: PEP 8

# Packages should be names: short, all-lowercase names. Preferably no underscores.
# Modules should be named: short, all-lowercase names. Can have underscores.
# Classes should be named: CapWords (upper camel case) convention
# Functions should be named: lowercase, words seperated by underscores (snake_case)
# Variables should be named: lowercase, words seperated by underscores (snake_case)
# Constants should be named: all-uppercase, words seperated by underscores.