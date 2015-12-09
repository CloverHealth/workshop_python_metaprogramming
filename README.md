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

Metaprogramming is a fancy word for code that generates code. On a basic level, functional programming is already a form of metaprogramming - functions that return new functions. Programming languages with true macro systems (where arguments are unevaluated symbols) are a more advanced form of the same.

### Why Metaprogramming?

All of this provides for much smaller code due to increased code reuse. Composability is key to increasing code reuse, and the ability to generate functions out of other functions (a core feature of functional programming) is key to that.

### What is Metaprogramming in Python?

Python has functional programming features - limited lambdas, etc. However, the word metaprogramming in the context of Python is strongly correlated with a feature limited to a few languages - metaclasses.

### What are Metaclasses?

Metaclasses are templates for classes. Just as objects are instances of classes, classes are instances of metaclasses.

## Object Lifecycle
`__new__` is called before `__init__` on Python object creation. __new__ is called for the creation of a new class, while __init__ is called after the class is created, to perform additional initialization before the class is handed to the caller: this means that you can override `__new__` for custom implementations before the object actually initializes (like returning an already allocated object instead of allocating a new one). When overriding `__new__()` you can change things like the ‘name’, ‘bases’ and ‘namespace’ arguments before you call the super constructor and it will have an effect, but doing the same thing in `__init__()` you won’t get any results from the constructor call.

## Classes as Callables
Classes are "syntactic sugar" for functions. Through closure, we can achieve the same effect as a class structure where we define and make methods available, which have access to enclosed variables that are accessible only to their own context.

## Class as Type Wrapper
Underneath the hood, defining `class` is just calling `type` to instantiate the object. You can define a class in the same way by calling the `type` function directly and defining the members of that class as arguments.

## Class Templates

## More Resources
