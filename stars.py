#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

freq_space = 25
freq_star1 = 4
freq_star2 = 2
freq_star3 = 1

choices = []
choices.extend(freq_space * " ")
choices.extend(freq_star1 * ".")
choices.extend(freq_star2 * "*")
choices.extend(freq_star3 * "`")

print("```")
for line in range(10):
    stars = []
    for c in range(114):
        item = random.choice(choices)
        stars.append(item)
    print("".join(stars))
print("```")
