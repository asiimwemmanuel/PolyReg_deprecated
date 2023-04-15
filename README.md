<style>
	p, li {font-size: 20px;}
	img {width: 33.333%;}
	h2 {text-align: center; font-family: MV Boli;}
</style>

# 9:56 PM 21/11/22

This project is to modularize my math functions and formulae, specifically *resistance in parallel* and the *general formula for quadratic sequences*.

**Go to bottom for documentation**

<p style="font-family: consolas;">Languages used: C++23, Python3</p>

## Resources
	- Abbott: Understanding Analysis
	- John K. Hunter: An Introduction to Real Analysis
	- Robert G. Bartle | Donald R. Sherbert: Introduction to Real Analysis
	- William F. Trench: Introduction to Real Analysis
	- Attached documentation

<br/>

# 2:09 AM 20/12/22

The next step in this project is the generalisation for any magnitude of series, involving Real Analysis
This generalisation should not have compounding complexity ie. it should not have efficiency dependent on the magnitude of the series, hopefully at least O(n^2)

<br/>

# 11:25 AM 16/02/2023

## ANALYSIS OF QUADRATIC SERIES

> To be soon succeeded by a program analysing series of varying orders, not just quadratic under polynomial complexity
>
> *For terms a, b, c in quadratic series;*
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

# DOCUMENTATION
<img src="./theory/theory_v1/page 1.jpg" alt="docs-page-1" align="left"/>
<img src="./theory/theory_v1/page 2.jpg" alt="docs-page-2" align="center"/>
<img src="./theory/theory_v1/page 3.jpg" alt="docs-page-3" align="right"/>

<!-- ![doc-page-1](./theory/theory_v1/page%201.jpg)
![doc-page-2](./theory/theory_v1/page%202.jpg)
![doc-page-3](./theory/theory_v1/page%203.jpg)
![doc-page-1](https://github.com/asiimwemmanuel/my-math/blob/main/theory/theory_v1/page%201.jpg)
![doc-page-2](https://github.com/asiimwemmanuel/my-math/blob/main/theory/theory_v1/page%202.jpg)
![doc-page-3](https://github.com/asiimwemmanuel/my-math/blob/main/theory/theory_v1/page%203.jpg)
[image](http://github.com/asiimwemmanuel/my-math.git/theory/theory_v0.jpg) -->
