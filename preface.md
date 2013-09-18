% How to Think Like a Computer Scientist

**Version 1.1.24+Kart [Python 3.2]**


Allen Downey\
Green Tea Press\
Needham, Massachusetts\
Copyright © 2008 Allen Downey.

Printing history:

April 2002:
:   First edition of *How to Think Like a Computer Scientist*.

August 2007:
:   Major revision, changed title to *How to Think Like a (Python)
    Programmer*.

June 2008:
:   Major revision, changed title to *Think Python: How to Think Like a
    Computer Scientist*.

Green Tea Press\
9 Washburn Ave\
Needham MA 02492

Permission is granted to copy, distribute, and/or modify this document
under the terms of the GNU Free Documentation License, Version 1.1 or
any later version published by the Free Software Foundation; with no
Invariant Sections, no Front-Cover Texts, and with no Back-Cover Texts.

The GNU Free Documentation License is available from www.gnu.org or by
writing to the Free Software Foundation, Inc., 59 Temple Place, Suite
330, Boston, MA 02111-1307, USA.

The original form of this book is LaTeX source code. Compiling this
LaTeX source has the effect of generating a device-independent
representation of a textbook, which can be converted to other formats
and printed.

The LaTeX source for this book is available from
<http://www.thinkpython.com>

Think Python: How to Think Like a Computer Scientist

Allen B. Downey

Version 1.1.24+Kart [Python 3.2]

Preface
=======

The strange history of this book {.unnumbered}
--------------------------------

In January 1999 I was preparing to teach an introductory programming
class in Java. I had taught it three times and I was getting frustrated.
The failure rate in the class was too high and, even for students who
succeeded, the overall level of achievement was too low.

One of the problems I saw was the books. They were too big, with too
much unnecessary detail about Java, and not enough high-level guidance
about how to program. And they all suffered from the trap door effect:
they would start out easy, proceed gradually, and then somewhere around
Chapter 5 the bottom would fall out. The students would get too much new
material, too fast, and I would spend the rest of the semester picking
up the pieces.

Two weeks before the first day of classes, I decided to write my own
book. My goals were:

-   Keep it short. It is better for students to read 10 pages than not
    read 50 pages.

-   Be careful with vocabulary. I tried to minimize the jargon and
    define each term at first use.

-   Build gradually. To avoid trap doors, I took the most difficult
    topics and split them into a series of small steps.

-   Focus on programming, not the programming language. I included the
    minimum useful subset of Java and left out the rest.

I needed a title, so on a whim I chose *How to Think Like a Computer
Scientist*.

My first version was rough, but it worked. Students did the reading, and
they understood enough that I could spend class time on the hard topics,
the interesting topics and (most important) letting the students
practice.

I released the book under the GNU Free Documentation License, which
allows users to copy, modify, and distribute the book.

What happened next is the cool part. Jeff Elkner, a high school teacher
in Virginia, adopted my book and translated it into Python. He sent me a
copy of his translation, and I had the unusual experience of learning
Python by reading my own book.

Jeff and I revised the book, incorporated a case study by Chris Meyers,
and in 2001 we released *How to Think Like a Computer Scientist:
Learning with Python*, also under the GNU Free Documentation License. As
Green Tea Press, I published the book and started selling hard copies
through Amazon.com and college book stores. Other books from Green Tea
Press are available at <greenteapress.com>.

In 2003 I started teaching at Olin College and I got to teach Python for
the first time. The contrast with Java was striking. Students struggled
less, learned more, worked on more interesting projects, and generally
had a lot more fun.

Over the last five years I have continued to develop the book,
correcting errors, improving some of the examples and adding material,
especially exercises. In 2008 I started work on a major revision—at the
same time, I was contacted by an editor at Cambridge University Press
who was interested in publishing the next edition. Good timing!

The result is this book, now with the less grandiose title *Think
Python*. Some of the changes are:

-   I added a section about debugging at the end of each chapter. These
    sections present general techniques for finding and avoiding bugs,
    and warnings about Python pitfalls.

-   I removed the material in the last few chapters about the
    implementation of lists and trees. I still love those topics, but I
    thought they were incongruent with the rest of the book.

-   I added more exercises, ranging from short tests of understanding to
    a few substantial projects.

-   I added a series of case studies—longer examples with exercises,
    solutions, and discussion. Some of them are based on Swampy, a suite
    of Python programs I wrote for use in my classes. Swampy, code
    examples, and some solutions are available from <thinkpython.com>.

-   I expanded the discussion of program development plans and basic
    design patterns.

-   The use of Python is more idiomatic. The book is still about
    programming, not Python, but now I think the book gets more leverage
    from the language.

I hope you enjoy working with this book, and that it helps you learn to
program and think, at least a little bit, like a computer scientist.

Allen B. Downey\
Needham MA\

Allen Downey is an Associate Professor of Computer Science at the
Franklin W. Olin College of Engineering.

Acknowledgements {.unnumbered}
----------------

First and most importantly, I thank Jeff Elkner, who translated my Java
book into Python, which got this project started and introduced me to
what has turned out to be my favorite language.

I also thank Chris Meyers, who contributed several sections to *How to
Think Like a Computer Scientist*.

And I thank the Free Software Foundation for developing the GNU Free
Documentation License, which helped make my collaboration with Jeff and
Chris possible.

I also thank the editors at Lulu who worked on *How to Think Like a
Computer Scientist*.

I thank all the students who worked with earlier versions of this book
and all the contributors (listed below) who sent in corrections and
suggestions.

And I thank my wife, Lisa, for her work on this book, and Green Tea
Press, and everything else, too.

