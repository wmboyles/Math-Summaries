# Math-Summaries
These are LaTeX summaries of various math courses. They are meant to be longer and more in-depth than a formula sheet and also shorter and less formal than a textbook.

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
8. Sequences L'Hopital's Rule, & Improper Integrals
9. Infinite Series
10. Additional Materials


## Multivaraible Calculus (multiCalc)
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

## How to Compile (make into a PDF)
Simply download the folders for each work you like to build and compile the main.tex file using a tool like pdflatex. Most LaTeX IDEs (like TeXStudio) have this functionality built-in. You can also use pdflatex to compile directly from the commandline by running 
```bash
$pdflatex main.tex
```

## How to Contribute
The easiest way to contribute is to fork the repository, make your changes in the LaTeX documents, and submit a pull request. However, if you don't know LaTeX, there are till other ways to contribute. One of the most-needed non-LaTeX items are figures: to avoid copyright claims, images should either be created by contributors themselves the public domain.

## Notes
* The differential equations work has the option to not include certain chapters or examples in certain chapters when compiled to a PDF. By default, all chapters and examples are included. If you would like to change these options before compiling change the relevant \\def line in the main.tex file.
