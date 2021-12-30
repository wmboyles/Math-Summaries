# Math-Summaries

These are LaTeX summaries of various math courses. They are meant to be longer and more in-depth than a formula sheet and also shorter and less formal than a textbook.

# Quick view

-   [Single Variable Calculus](https://raw.githubusercontent.com/wmboyles/Math-Summaries/master/calc/main.pdf)
-   [Differential Equations](https://raw.githubusercontent.com/wmboyles/Math-Summaries/master/diffEq/main.pdf)
-   [Multivariable Calculus](https://raw.githubusercontent.com/wmboyles/Math-Summaries/master/multiCalc/main.pdf)
-   [Linear Algebra](https://raw.githubusercontent.com/wmboyles/Math-Summaries/master/linAlg/main.pdf)

## Single Variable Calculus (calc)

This covers topics you'd find on the AP AB/BC exams, which are the same topics you'd see in undergraduate Calc I and Calc II courses.
The chapters are:

1. Background & Review
2. Limits & Continuity
3. Derivatives
4. Applications of the Derivative
5. Integrals
6. Applications of Integrals
7. Parametrics, Vector, & Polar Functions
8. Sequences, L'Hôpital's Rule, & Improper Integrals
9. Infinite Series
10. Additional Materials

## Multivariable Calculus (multiCalc)

This covers topics typically found and an undergraduate multivaraible calculus course, like multiple integrals, Green's Theorems, and Stokes's Theorem.
The chapters are:

1. Background & Review
2. Vector-Valued Functions (VVFs)
3. Differential Multivariable Calculus
4. Multiple Integrals
5. Curvilinear Coordinates
6. Line and Surface Integrals
7. Vector Analysis
8. Additional Materials

## Differential Equations (diffEq)

This covers topics typically found in an undergraduate introductory differential equations course. Most discussion is limited to Ordinary Differential Equations (ODEs).
The chapters are:

1. Background & Review
2. The Basics of Differential Equations
3. 1st Order Linear ODE's
4. Higher Order ODE's
5. Linear Systems of Differential Equations
6. Laplace Transforms
7. Additional Resources

## Linear Algebra (linAlg)
This covers topics typically found in an undergraduate linear algebra course.
The chapters are:

1. Background & Review
2. TODO TODO TODO

## How to Compile (make into a PDF)

Simply download the folders for each work you like to build and compile the main.tex file.
You'll need to use a typesetting engine that supports unicode characters, like [XeLaTeX](https://www.tug.org/texlive/download-install.html).
Most LaTeX IDEs (like TeXStudio) have this functionality built-in.
You can also use pdflatex to compile directly from the command line by running

```bash
$ xelatex main.tex
```

in the appropriate project folder (i.e. `diffEq`)

## How to Contribute

The easiest way to contribute is to fork the repository, make your changes in the LaTeX documents, and submit a pull request. However, if you don't know LaTeX, there are still other ways to contribute. One of the most-needed non-LaTeX items are figures: to avoid copyright claims, images should either be created by contributors themselves or belong to the public domain.
