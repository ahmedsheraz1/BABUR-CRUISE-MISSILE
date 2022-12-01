Python 3.10.2 (v3.10.2:a58ebcc701, Jan 13 2022, 14:50:16) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
import re
m = re.search('(?<=abc)def', 'abcdef')
m.group(0)
'def'
m = re.search(r'(?<=-)\w+', 'spam-egg')
m.group(0)
'egg'
re.split(r'\W+', 'BABUR, BABUR, BABUR.')
['BABUR', 'BABUR', 'BABUR', '']
re.split(r'(\W+)', 'BABUR, BABUR, BABUR.')
['BABUR', ', ', 'BABUR', ', ', 'BABUR', '.', '']
re.split(r'\W+', 'BABUR, BABUR, BABUR.', 1)
['BABUR', 'BABUR, BABUR.']
re.split('[a-f]+', '0a3B9', flags=re.IGNORECASE)
['0', '3', '9']
re.split(r'(\W+)', '...BABUR, BABUR...')
['', '...', 'BABUR', ', ', 'BABUR', '...', '']
re.split(r'\b', 'BABUR, BABUR, BABUR.')
['', 'BABUR', ', ', 'BABUR', ', ', 'BABUR', '.']
re.split(r'\W*', '...BABUR...')
['', '', 'B', 'A', 'B', 'U', 'R', '', '']
re.split(r'(\W*)', '...BABUR...')
['', '...', '', '', 'B', '', 'A', '', 'B', '', 'U', '', 'R', '...', '', '', '']
re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')
['foot', 'fell', 'fastest']
re.findall(r'(\w+)=(\d+)', 'set width=20 and height=10')
[('width', '20'), ('height', '10')]
m = re.match(r"(\w+) (\w+)", "BABUR CRUISE MISSILE")
m.group(0)
'BABUR CRUISE'
m.group(1)
'BABUR'
m.group(2)
'CRUISE'
m.group(1, 2)
('BABUR', 'CRUISE')
