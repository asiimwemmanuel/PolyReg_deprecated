# 9:56 PM 21/11/22
This project is to modularize my math functions and formulae, specifically *resistance in parallel* and the *general formula for quadratic sequences*.

**Go to ./theory/theory_v1 for documentation**

<p style="font-family: consolas; font-size: 20px;">Languages used: C++23, Python3</p>

## Resources
	- Abbott: Understanding Analysis
	- John K. Hunter: An Introduction to Real Analysis
	- Robert G. Bartle | Donald R. Sherbert: Introduction to Real Analysis
	- William F. Trench: Introduction to Real Analysis
	- Attached documentation

<br/>

# 2:09 AM 20/12/22

The next step in this project is the generalisation for any magnitude of series, involving Real Analysis.

This generalisation should not have compounding complexity ie. it should not have efficiency dependent on the magnitude of the series, hopefully at least O(n^2)

<br/>

# 11:25 AM 16/02/2023

## ANALYSIS OF QUADRATIC SERIES

> To be soon succeeded by a program analysing series of varying orders, not just quadratic under polynomial complexity
>
> *For **unique** & **non-repeating** terms a, b, c in quadratic series;*
> > - *α = b - a* </br>
> > - *x = c - b - α* </br> <!-- x = c + a - 2b*-->
> <p style="font-family: Gabriola; font-size: 35px; text-align: center;">nth term = α + ∑ (xi + α - x) from i = 1 to n-1</p>
> <p style="font-size: 15px; text-align: right;">(proof in the attached documentation)</p>

<br/>

## ANALYSIS OF RESISTANCE IN PARALLEL

> For n resistors in parallel connection, ***the total resistance is the reciprocal of the sum of the reciprocals of the resistors***. </br>
> <p style="font-family: Gabriola; font-size: 35px; text-align: center;">Ωt = 1/(∑ (1/Ωx) from x = 1 to n)</p>

<br/>

# 11:52 AM 20/03/2023

Investigate the difference in rounding & display errors between cppver & pyver (through very precise progressions with differences of 10^-8, which is arbitrary), as well as how C++23 automatically rounds off doubles, and find a way to apply the same for Python.

Also look to fix variable duplication, and managing the math_tools class.

***OPEN-RESEARCH POINT: What else should the class include, other than progession-related tools?***

Focus on how to get the best out of each language (through a .json file or an API) for the most optimal (if ever needed) *math-toolbox*.

Also compare the correct formula in the eqtn-ref branch with the control, and the limitations (eg. managing reducing progressions) of each.

<br/>

# 11:14 AM 31/03/2023

Investigate "oscillating" progressions eg. 1, 3, 3, 5, 5, 7, 7, ...

Hypothesis: Such series have repeating terms in a supposedly fixed frequency eg. in the above example, f = 2

Note: These have been termed "oscillating" since the table of differences is (supposedly) never-ending and has any given difference past a certain (yet to be determined) threshold obtained via extrapolating or inferring from previous differences in a circular fashion.

In the example, the first array of differences goes between 2 and 0. The inferred array goes between -2 and +2. The next between +4 and -4. The next between -8 and +8. (Note the order of the variables). The next array shall have terms that are twice as large as the previous.

<p style="text-align: center;">Further investigation is required. </p>