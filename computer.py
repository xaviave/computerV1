import re

from parser import parser
from process import process_equation

"""
Examples:
5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0
4 * X^0 + 4 * X^1 - 9.3 * X^2 = 0
5 * X^0 + 4 * X^1 = 4 * X^0
1 * X^0 + 4 * X^1 = 0
8 * X^0 - 6 * X^1 + 0 * X^2 - 5.6 * X^3 = 3 * X^0
5 * X^0 - 6 * X^1 + 0 * X^2 - 5.6 * X^3 = 0
5 + 4 * X^0 + X^2= X^2
0*X^2-5*X^1-10*X^0=0
X2-5X-10=0
5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0
- 5 * X^0 + 4 * X^1 = 4 * X^0
8 * X^0 - 6 * X^1 + 0 * X^2 - 5.6 * X^3 = 3 * X^0 + 5X / 2 +5  - -5 -9 - 70
"""

if __name__ == "__main__":
    norm_regex = re.compile(
        r'\s*(([+-=*/ ]|^)?\s*((?:-)?\d+(?:\.\d+)?)?\s*(?:(?:[*\\])?\s*(X)\s*(?:\^\s*((?:-)?\d+(?:\.\d+)?))?)?)')
    parsed_equations_list = parser(norm_regex)

    for parsed_equation in parsed_equations_list:
        process_equation(parsed_equation)
