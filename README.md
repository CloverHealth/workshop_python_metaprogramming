# Python Metaprogramming Workshop
###### by Clover Health

## About this Workshop

This workshop explores metaprogramming in a Python context, specifically metaclasses. Metaclasses are a powerful way to greatly reduce the amount of boilerplate code in object oriented programming. With careful use and documentation, programs become easier to understand and more maintainable.

Although this is broadly applicable to both Python 2 and Python 3, the specifics of syntax (and examples) are geared towards Python 3.

## What You'll Learn

1. Object Lifecycle - `__new__` vs. `__init__`
2. Classes as Callables - `__call__` vs. `class:`
3. Class as Type Wrapper - `type()` vs. `class:`
4. Class Templates - `metaclass=`

## Intro to Metaprogramming and Metaclasses

### What is Metaprogramming?

Metaprogramming is a fancy word for code that generates code. On a basic level, functional programming is already a form of metaprogramming - for example, functions that return new functions. Programming languages with true macro systems (where arguments are unevaluated symbols - almost like passing in snippets of code as strings) are a more advanced form of the same.

### Why Metaprogramming?

All of this provides for much smaller code due to increased code reuse. Composability is key to increasing code reuse, and the ability to generate functions out of other functions (a core feature of functional programming) is key to that.

### What is Metaprogramming in Python?

Python has functional programming features - limited lambdas, etc. However, the word metaprogramming in the context of Python is strongly correlated with a feature limited to a few languages - metaclasses.

### What are Metaclasses?

Metaclasses are templates for classes. Just as objects are instances of classes, classes are instances of metaclasses.

## Object Lifecycle

Because we are dealing with classes, we are dealing with units of code that create objects. Therefore, we must understand object creation at a basic level.

### Object Instantiation / Creation

When an object is created, `__new__` is first called, followed by `__init__`.

- `__new__` is called to actually allocate memory for the new object.
- `__init__` is called to initialize the memory - i.e. set the object up with initial attributes.

This means that you can override `__new__` in custom classes, to control things such as:

- Memory allocation - return an existing object instead of allocating a new one at all.
- Immutability - set the attributes of an object where the class does not allow the attributes to change.

### Example

See the [01_object_lifecycle](01_object_lifecycle/object_lifecycle.py) Python 3 file.

We are demonstrating the [Flyweight object-oriented design pattern](https://en.wikipedia.org/wiki/Flyweight_pattern).

#### Notes:

- When `__new__` is run, it has no `self`. That object does not exist. (It's `__new__`'s job to create it.)
- `__new__` gets a reference to the class instead. This is to allow `super()`, which gets the base class, which you would call `__new__` on to create the object.
- `__new__` returns the object, as opposed to `__init__` which is not allowed to return anything.

## Classes as Callables

Syntactically, classes are used as if they were functions, which internally they are! For example, objects are constructed like:

        my_object = MyClass(init_arg_1, init_arg_2)

Note the parentheses after the class. That's just like a function call, except the function name is CamelCase!

### Example

See the [02_classes_as_callables](02_classes_as_callables/classes_as_callables.py) Python 3 file.

#### Notes

- See `def Bookshelf()`. It's a function that returns an object.
- The function goes through the same sequence that `class:` goes through:
    - `__new__` and `__init__`
    - Make the `add_book()` function accessible. __(This is the syntactic sugar part.)__
- The one difference is that `add_book()` is a different copy for every object created by the function version. In the class, it's a single function that gets shared.
- Note how JavaScript-y the function version is.

## Class as Type Wrapper

Underneath the hood, defining `class` is just calling `type` to instantiate the class. You can define a class in the same way by calling `type()` directly and defining the members of that class as arguments.

### Example

See the [03_class_vs_type_wrapper](03_class_vs_type_wrapper/class_vs_type_wrapper.py) Python 3 file.

#### Notes

- Note how the object created with `BookshelfAsType` responds properly to `type()`.

## Class Templates

Just as classes are templates for objects, metaclasses are templates for classes. They can modify the definition of a class __before__ it is allocated, as well as initialize the attributes of the class after.

### Example

See the [04_class_templates](04_class_templates/class_templates.py) Python 3 file.

#### Notes

- Ultimately, the base class of all metaclasses is `type`. Therefore, the arguments in the `class` header are the same as the arguments to the `type()` function.
- In general, use `__new__` to define functions, and `__init__` to define class variables.
- In Python 3, metaclasses are assigned as a keyword argument in the `class` header.
