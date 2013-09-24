Lists
=====

A **list** is an ordered collection of values. The values that make up a
list are called its **elements**, or its **items**. We will use the term
element or item to mean the same thing. Lists are similar to strings,
which are ordered collections of characters, except that the elements of
a list can be of any type. Lists and strings --- and other collections
that maintain the order of their items --- are called **sequences**.

List values
-----------

There are several ways to create a new list; the simplest is to enclose
the elements in square brackets (`[` and `]`):

The first example is a list of four integers. The second is a list of
three strings. The elements of a list don't have to be the same type.
The following list contains a string, a float, an integer, and
(amazingly) another list:

A list within another list is said to be **nested**.

Finally, a list with no elements is called an empty list, and is denoted
`[]`.

We have already seen that we can assign list values to variables or pass
lists as parameters to functions:

Accessing elements
------------------

The syntax for accessing the elements of a list is the same as the
syntax for accessing the characters of a string --- the index operator:
`[]` (not to be confused with an empty list). The expression inside the
brackets specifies the index. Remember that the indices start at 0:

Any expression evaluating to an integer can be used as an index:

If you try to access or assign to an element that does not exist, you
get a runtime error:

It is common to use a loop variable as a list index.

Each time through the loop, the variable `i` is used as an index into
the list, printing the `i`'th element. This pattern of computation is
called a **list traversal**.

The above sample doesn't need or use the index `i` for anything besides
getting the items from the list, so this more direct version --- where
the `for` loop gets the items --- might be preferred:

List length
-----------

The function `len` returns the length of a list, which is equal to the
number of its elements. If you are going to use an integer index to
access the list, it is a good idea to use this value as the upper bound
of a loop instead of a constant. That way, if the size of the list
changes, you won't have to go through the program changing all the
loops; they will work correctly for any size list:

The last time the body of the loop is executed, `i` is
`len(horsemen) - 1`, which is the index of the last element. (But the
version without the index looks even better now!)

Although a list can contain another list, the nested list still counts
as a single element in its parent list. The length of this list is 4:

List membership
---------------

`in` and `not in` are Boolean operators that test membership in a
sequence. We used them previously with strings, but they also work with
lists and other sequences:

Using this produces a more elegant version of the nested loop program we
previously used to count the number of students doing Computer Science
in the section nested\_data:

List operations
---------------

The `+` operator concatenates lists:

Similarly, the `*` operator repeats a list a given number of times:

The first example repeats `[0]` four times. The second example repeats
the list `[1, 2, 3]` three times.

List slices
-----------

The slice operations we saw previously with strings let us work with
sublists:

Lists are mutable
-----------------

Unlike strings, lists are **mutable**, which means we can change their
elements. Using the index operator on the left side of an assignment, we
can update one of the elements:

The bracket operator applied to a list can appear anywhere in an
expression. When it appears on the left side of an assignment, it
changes one of the elements in the list, so the first element of `fruit`
has been changed from `"banana"` to `"pear"`, and the last from
`"quince"` to `"orange"`. An assignment to an element of a list is
called **item assignment**. Item assignment does not work for strings:

but it does for lists:

With the slice operator we can update a whole sublist at once:

We can also remove elements from a list by assigning an empty list to
them:

And we can add elements to a list by squeezing them into an empty slice
at the desired location:

List deletion
-------------

Using slices to delete list elements can be error-prone. Python provides
an alternative that is more readable. The `del` statement removes an
element from a list:

As you might expect, `del` causes a runtime error if the index is out of
range.

You can also use `del` with a slice to delete a sublist:

As usual, the sublist selected by slice contains all the elements up to,
but not including, the second index.

Objects and references
----------------------

After we execute these assignment statements

we know that `a` and `b` will refer to a string object with the letters
`"banana"`. But we don't know yet whether they point to the *same*
string object.

There are two possible ways the Python interpreter could arrange its
memory:

> ![List illustration](illustrations/list1.png)

In one case, `a` and `b` refer to two different objects that have the
same value. In the second case, they refer to the same object.

We can test whether two names refer to the same object using the `is`
operator:

This tells us that both `a` and `b` refer to the same object, and that
it is the second of the two state snapshots that accurately describes
the relationship.

Since strings are *immutable*, Python optimizes resources by making two
names that refer to the same string value refer to the same object.

This is not the case with lists:

The state snapshot here looks like this:

> ![State snapshot for equal different lists](illustrations/mult_references2.png)

`a` and `b` have the same value but do not refer to the same object.

Aliasing
--------

Since variables refer to objects, if we assign one variable to another,
both variables refer to the same object:

In this case, the state snapshot looks like this:

> ![State snapshot for multiple references (aliases) to a list](illustrations/mult_references3.png)

Because the same list has two different names, `a` and `b`, we say that
it is **aliased**. Changes made with one alias affect the other:

Although this behavior can be useful, it is sometimes unexpected or
undesirable. In general, it is safer to avoid aliasing when you are
working with mutable objects (i.e. lists at this point in our textbook,
but we'll meet more mutable objects as we cover classes and objects,
dictionaries and sets). Of course, for immutable objects (i.e. strings,
tuples), there's no problem --- it is just not possible to change
something and get a surprise when you access an alias name. That's why
Python is free to alias strings (and any other immutable kinds of data)
when it sees an opportunity to economize.

Cloning lists
-------------

If we want to modify a list and also keep a copy of the original, we
need to be able to make a copy of the list itself, not just the
reference. This process is sometimes called **cloning**, to avoid the
ambiguity of the word copy.

The easiest way to clone a list is to use the slice operator:

Taking any slice of `a` creates a new list. In this case the slice
happens to consist of the whole list. So now the relationship is like
this:

> ![State snapshot for equal different lists](illustrations/mult_references2.png)

Now we are free to make changes to `b` without worrying that we'll
inadvertently be changing `a`:

Lists and `for` loops
---------------------

The `for` loop also works with lists, as we've already seen. The
generalized syntax of a `for` loop is:

So, as we've seen

It almost reads like English: For (every) friend in (the list of)
friends, print (the name of the) friend.

Any list expression can be used in a `for` loop:

The first example prints all the multiples of 3 between 0 and 19. The
second example expresses enthusiasm for various fruits.

Since lists are mutable, we often want to traverse a list, changing each
of its elements. The following squares all the numbers in the list `xs`:

Take a moment to think about `range(len(xs))` until you understand how
it works.

In this example we are interested in both the *value* of an item, (we
want to square that value), and its *index* (so that we can assign the
new value to that position). This pattern is common enough that Python
provides a nicer way to implement it:

`enumerate` generates pairs of both (index, value) during the list
traversal. Try this next example to see more clearly how `enumerate`
works:

List parameters
---------------

Passing a list as an argument actually passes a reference to the list,
not a copy or clone of the list. So parameter passing creates an alias
for you: the caller has one variable referencing the list, and the
called function has an alias, but there is only one underlying list
object. For example, the function below takes a list as an argument and
multiplies each element in the list by 2:

If we add the following onto our script:

When we run it we'll get:

In the function above, the parameter `a_list` and the variable `things`
are aliases for the same object. So before any changes to the elements
in the list, the state snapshot looks like this:

> ![State snapshot for multiple references to a list as a parameter](illustrations/mult_references4.png)

Since the list object is shared by two frames, we drew it between them.

If a function modifies the items of a list parameter, the caller sees
the change.

> > **Use the Python visualizer!**
> >
> > We've already mentioned the Python visualizer at
> > <http://netserv.ict.ru.ac.za/python3_viz>. It is a very useful tool
> > for building a good understanding of references, aliases,
> > assignments, and passing arguments to functions. Pay special
> > attention to cases where you clone a list or have two separate
> > lists, and cases where there is only one underlying list, but more
> > than one variable is aliased to reference the list.

List methods
------------

The dot operator can also be used to access built-in methods of list
objects. We'll start with the most useful method for adding something
onto the end of an existing list:

`append` is a list method which adds the argument passed to it to the
end of the list. We'll use it heavily when we're creating new lists.
Continuing with this example, we show several other list methods:

Experiment and play with the list methods shown here, and read their
documentation until you feel confident that you understand how they
work.

Pure functions and modifiers
----------------------------

Functions which take lists as arguments and change them during execution
are called **modifiers** and the changes they make are called **side
effects**.

A **pure function** does not produce side effects. It communicates with
the calling program only through parameters, which it does not modify,
and a return value. Here is `double_stuff` written as a pure function:

This version of `double_stuff` does not change its arguments:

An early rule we saw for assignment said "first evaluate the right hand
side, then assign the resulting value to the variable". So it is quite
safe to assign the function result to the same variable that was passed
to the function:

> **Which style is better?**
>
> Anything that can be done with modifiers can also be done with pure
> functions. In fact, some programming languages only allow pure
> functions. There is some evidence that programs that use pure
> functions are faster to develop and less error-prone than programs
> that use modifiers. Nevertheless, modifiers are convenient at times,
> and in some cases, functional programs are less efficient.
>
> In general, we recommend that you write pure functions whenever it is
> reasonable to do so and resort to modifiers only if there is a
> compelling advantage. This approach might be called a *functional
> programming style*.

Functions that produce lists
----------------------------

The pure version of `double_stuff` above made use of an important
**pattern** for your toolbox. Whenever you need to write a function that
creates and returns a list, the pattern is usually:

Let us show another use of this pattern. Assume you already have a
function `is_prime(x)` that can test if x is prime. Write a function to
return a list of all prime numbers less than n:

Strings and lists
-----------------

Two of the most useful methods on strings involve conversion to and from
lists of substrings. The `split` method (which we've already seen)
breaks a string into a list of words. By default, any number of
whitespace characters is considered a word boundary:

An optional argument called a **delimiter** can be used to specify which
string to use as the boundary marker between substrings. The following
example uses the string `ai` as the delimiter:

Notice that the delimiter doesn't appear in the result.

The inverse of the `split` method is `join`. You choose a desired
**separator** string, (often called the *glue*) and join the list with
the glue between each of the elements:

The list that you glue together (`wds` in this example) is not modified.
Also, as these next examples show, you can use empty glue or
multi-character strings as glue:

`list` and `range`
------------------

Python has a built-in type conversion function called `list` that tries
to turn whatever you give it into a list.

One particular feature of `range` is that it doesn't instantly compute
all its values: it "puts off" the computation, and does it on demand, or
"lazily". We'll say that it gives a **promise** to produce the values
when they are needed. This is very convenient if your computation
short-circuits a search and returns early, as in this case:

In the second test, if range were to eagerly go about building a list
with all those elements, you would soon exhaust your computer's
available memory and crash the program. But it is cleverer than that!
This computation works just fine, because the `range` object is just a
promise to produce the elements if and when they are needed. Once the
condition in the `if` becomes true, no further elements are generated,
and the function returns. (Note: Before Python 3, `range` was not lazy.
If you use an earlier versions of Python, YMMV!)

> > **YMMV: Your Mileage May Vary**
> >
> > The acronym YMMV stands for *your mileage may vary*. American car
> > advertisements often quoted fuel consumption figures for cars, e.g.
> > that they would get 28 miles per gallon. But this always had to be
> > accompanied by legal small-print warning the reader that they might
> > not get the same. The term YMMV is now used idiomatically to mean
> > "your results may differ", e.g. *The battery life on this phone is 3
> > days, but YMMV.*

You'll sometimes find the lazy `range` wrapped in a call to `list`. This
forces Python to turn the lazy promise into an actual list:

Nested lists
------------

A nested list is a list that appears as an element in another list. In
this list, the element with index 3 is a nested list:

If we output the element at index 3, we get:

To extract an element from the nested list, we can proceed in two steps:

Or we can combine them:

Bracket operators evaluate from left to right, so this expression gets
the 3'th element of `nested` and extracts the 1'th element from it.

Matrices
--------

Nested lists are often used to represent matrices. For example, the
matrix:

> ![image](illustrations/matrix2.png)

might be represented as:

`mx` is a list with three elements, where each element is a row of the
matrix. We can select an entire row from the matrix in the usual way:

Or we can extract a single element from the matrix using the
double-index form:

The first index selects the row, and the second index selects the
column. Although this way of representing matrices is common, it is not
the only possibility. A small variation is to use a list of columns
instead of a list of rows. Later we will see a more radical alternative
using a dictionary.

Glossary
--------

Exercises
---------

1.  What is the Python interpreter's response to the following?

    The three arguments to the *range* function are *start*, *stop*, and
    *step*, respectively. In this example, `start` is greater than
    `stop`. What happens if `start < stop` and `step < 0`? Write a rule
    for the relationships among `start`, `stop`, and `step`.

2.  Consider this fragment of code:

    Does this fragment create one or two turtle instances? Does setting
    the color of `alex` also change the color of `tess`? Explain in
    detail.

3.  Draw a state snapshot for `a` and `b` before and after the third
    line of the following Python code is executed:

4.  What will be the output of the following program?

    Provide a *detailed* explanation of the results.

5.  Lists can be used to represent mathematical *vectors*. In this
    exercise and several that follow you will write functions to perform
    standard operations on vectors. Create a script named `vectors.py`
    and write Python code to pass the tests in each case.

    Write a function `add_vectors(u, v)` that takes two lists of numbers
    of the same length, and returns a new list containing the sums of
    the corresponding elements of each:

6.  Write a function `scalar_mult(s, v)` that takes a number, `s`, and a
    list, `v` and returns the [scalar
    multiple](http://en.wikipedia.org/wiki/Scalar_multiple) of `v` by
    `s`. :

7.  Write a function `dot_product(u, v)` that takes two lists of numbers
    of the same length, and returns the sum of the products of the
    corresponding elements of each (the
    [dot\_product](http://en.wikipedia.org/wiki/Dot_product)).

8.  *Extra challenge for the mathematically inclined*: Write a function
    `cross_product(u, v)` that takes two lists of numbers of length 3
    and returns their [cross
    product](http://en.wikipedia.org/wiki/Cross_product). You should
    write your own tests.

9.  Describe the relationship between `" ".join(song.split())` and
    `song` in the fragment of code below. Are they the same for all
    strings assigned to `song`? When would they be different?

10. Write a function `replace(s, old, new)` that replaces all
    occurrences of `old` with `new` in a string `s`:

    *Hint*: use the `split` and `join` methods.

11. Suppose you want to swap around the values in two variables. You
    decide to factor this out into a reusable function, and write this
    code:

    Run this program and describe the results. Oops! So it didn't do
    what you intended! Explain why not. Using a Python visualizer like
    the one at <http://netserv.ict.ru.ac.za/python3_viz> may help you
    build a good conceptual model of what is going on. What will be the
    values of `a` and `b` after the call to `swap`?


