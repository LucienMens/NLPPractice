# -*- coding: utf-8 -*-
"""
Quiz 2 for Natural Language Processing
"""

from re import findall
S1 = ('To our sister republics south of our border, we offer a special pledge: '
      'to convert our good words into good deeds, '
      'in a new alliance for progress, to assist free men and free governments in casting off the chains of poverty. '
      'But this peaceful revolution of hope cannot become the prey of hostile powers. '
      'Let all our neighbors know that we shall join with them to oppose aggression or subversion '
      'anywhere in the Americas. '
      'And let every other power know that this hemisphere intends to remain the master of its own house.')
plurals = findall(' ((\w+)[s]) ', S1)
plurals.sort()
print(plurals)
propnoun = findall('[A-Z][a-z]{6}', S1)

print("The proper noun is " + propnoun[0] + ".")
S2 = ('We observe today not a victory of party, but a celebration of freedom -- '
      'symbolizing an end, as well as a beginning -- signifying renewal, as well as change. '
      'For I have sworn before you and Almighty God the same solemn oath our forebears '
      'prescribed nearly a century and three-quarters ago.')
ing = findall('[a-z]*ing', S2)
print("The number of stems are " + str(len(ing))+".")
val1 = findall('([A-Za-z][a-z]{7})ing', S2)
val2 = findall('([A-Za-z][a-z]{6})ing', S2)
val3 = findall('([A-Za-z][a-z]{4})ning', S2)
print("The stems are "+val1[0]+ ", " +val3[0] +", and " +val2[1]+".")