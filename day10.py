# Day 10 Adapter Array
from functools import cache
test = '''28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3'''
inputs = '''99
151
61
134
112
70
75
41
119
137
158
50
167
60
116
117
62
82
31
3
72
88
165
34
8
14
27
108
166
71
51
42
135
122
140
109
1
101
2
77
85
76
143
100
127
7
107
13
148
118
56
159
133
21
154
152
130
78
54
104
160
153
95
49
19
69
142
63
11
12
29
98
84
28
17
146
161
115
4
94
24
126
136
91
57
30
155
79
66
141
48
125
162
37
40
147
18
20
45
55
83'''

a = [int(i) for i in inputs.split('\n')]
a.sort()
adapters = {1:1, 2:0, 3:1}

# part 1
def part1():
    for i in range(len(a)-1):
        difference = a[i+1] - a[i]
        adapters[difference] += 1

part1()
print(adapters, adapters[1]*adapters[3]) # 3 minutes? I KNOW YOU ARE HIDDING SOMETHING ...
# ___ part 2 ____

a.insert(0,0)
a.append(max(a)+3)
print(a)

@cache
def part2(n):
    x = [i for i in range(n-3, n) if i in a]
    #print(x)
    if n <= 0:
        return 1
    return sum(part2(i) for i in x)

print(part2(max(a)+3))
