#! /usr/bin/env python3
from math import comb

parts = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety",
    100: "hundred",
    1000: "thousand",
    "and": "and"
}


def written_number(n: int) -> str:
    """ Translates an integer into its written counterpart, in english. """
    if n == 0:
        return ''

    if n <= 20:
        return parts[n]

    if n < 100:
        return parts[10 * (n // 10)] + ' ' + ('' if n % 10 == 0 else parts[n % 10])

    if n < 1_000:
        written = parts[n // 100] + " hundred"

        sub = n % 100
        if sub == 0:
            return written

        if sub <= 20:
            return written + " and " + parts[sub]

        subsub = n%10
        return written + " and " + parts[10 * (sub // 10)] + ' ' + ('' if subsub == 0 else parts[subsub])

    if n < 10_000:
        return parts[n // 1000] + " thousand " + written_number(n % 1000)


written_numbers = []
for i in range(1, 1_001):
    res = written_number(i)
    res = res.replace(' ', '').strip()
    written_numbers.append(res)

print(sum([len(num) for num in written_numbers]))
