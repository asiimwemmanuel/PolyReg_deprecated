9:56 PM 21/11/22

This project is to modularize my math functions and formulae, specifically resistance in parallel and the general formula for quadratic sequences.

Languages used: C++, Python
Resources: Reference notes and attached documentation

2:09 AM 20/12/22

The next step in this project is the generalisation for any magnitude of series, involving Real Analysis
This generalisation should not have compounding complexity ie. it should not have efficiency dependent on the magnitude of the series, hopefully at least O(n^2)

11:25 AM 16/02/2023

--------------------------------------1.ANALYSIS OF QUADRATIC SERIES*-----------------------------------

* To be soon succeeded by a program analysing series of varying orders, not just quadratic under polynomial complexity

General formula (by me);
for terms a, b, c in quadratic series;
    α = b - a
    β = c - b
    x = β - α // x = c + a - 2b
nth term = a + ∑ (xi + α - x) from i = 1 to i = n-1 (proof in the attached documentation)

-----------------------------------2.ANALYSIS OF RESISTANCE IN PARALLEL---------------------------------

General formula;
For n resistors in parallel connection, the total resistance is the reciprocal of the sum of the reciprocals of the resistors
formally,
    Ωt = 1/(∑ (1/Ωx) from x = 1 to x = n)

11:52 AM 20/03/2023

Investigate the difference in rounding & display errors between cppver & pyver (through very precise progressions with differences of 10^-8 *arbitrarily*), as well as how C++20 automatically rounds off doubles, and find a way to apply the same for Python.

Also look to fix variable duplication, and managing the math_tools class.

OPEN RESEARCH POINT: What else should the class include, other than progession-related tools?

Focus on how to get the best out of each language (through a .json file or an API) for the most optimal (if ever needed) math-toolbox.

Also compare the correct formula in the eqtn-ref branch with the control, and the limitations (eg. managing reducing progressions) of each.