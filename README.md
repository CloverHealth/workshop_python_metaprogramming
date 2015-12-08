# Python Metaprogramming Workshop
###### by Clover Health

## About this Workshop

This workshop explores metaprogramming in a Python context, specifically metaclasses. Metaclasses are a powerful way to greatly reduce the amount of boilerplate code in object oriented programming. With careful use and documentation, programs become easier to understand and more maintainable.

## What You'll Learn

1. Object Lifecycle - `__new__` vs. `__init__`
2. Classes as Callables - `__call__` vs. `class:`
3. Classes as Syntactic Sugar - `type()` vs. `class:`
4. Class Templates with Extensions - `metaclass=`

## Table of Contents

1. Intro to Metaprogramming and Metaclasses

## Intro to Metaprogramming and Metaclasses

### What is Metaprogramming?

Metaprogramming is a fancy word for code that generates code. On a basic level, functional programming is already a form of metaprogramming - functions that return new functions. Programming languages with true macro systems (where arguments are unevaluated symbols) are a more advanced form of the same.

### Why Metaprogramming?

All of this provides for much smaller code due to increased code reuse. Composability is key to increasing code reuse, and the ability to generate functions out of other functions (a core feature of functional programming) is key to that.

### What is Metaprogramming in Python?

Python has functional programming features - limited lambdas, etc. However, the word metaprogramming in the context of Python is strongly correlated with a feature limited to a few languages - metaclasses.

### What are Metaclasses?

Metaclasses are
