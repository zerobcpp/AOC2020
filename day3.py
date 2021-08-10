from functools import reduce
inputs = [
".......#..#....#...#...#......#",
"..##..#...##.###.#..#.....#.#..",
"#..#.#....#......#..#.........#",
".#..##...#........#....#..#..#.",
"#.#.#....###...#........#.....#",
".#...#.#.##.#.##...#.#.........",
"####......#.......###.##.#.....",
"..#...........#...#.#.#........",
".#.......#....###.####..#......",
"...##........#....##.......##..",
".###......##.#......##....#.#.#",
"........#.#......##...#......#.",
"#....##.#..#...#.......#.......",
".#..##........##.........#....#",
".#..#..#...#....#.#......#.#...",
"..#.#......##.#.......#....##..",
"......##......#.#..##.#..#...#.",
".....##.......#.#....#.#.......",
"........#.....#.....#..###.#...",
"#........#..#.....#...#.#.#..#.",
".#..#.....#...#........#.....#.",
".#.#.....#.....#...#...........",
".....#.#..#..#...#..#..#..##..#",
"##.#...#....#..#.##..#.....#.#.",
"#.......####......#..#.#....#..",
"......#.#...####.........#.#..#",
".#.........#..#.#...#..........",
"...#####.#....#.#..#......#.#.#",
"##....#.###....##...##..#.....#",
"...........####.##.#....##.##..",
"#.#.#..........#.#..##.#.######",
"##...#..#...........###..#....#",
".#.#.#...##..........##.#...#..",
"...#.#........#..##...#....#...",
"......#..#...#..##....#.......#",
".#..#.......#..#......##....##.",
".......#.......#........#..##..",
"...#...#...#.##......#.##.#....",
".........#.........#.#.#.##....",
"..#...................#....#..#",
".........#..#.....#.#...#....#.",
"#.#.#...#........#..###.#......",
"#.#.#.####......##...#...#....#",
"#...........##..#.#.#....#..#..",
"........#..#.#...........##.#.#",
".#.........#...........#..#....",
"#............##.#..#....##...##",
".#....##..#.#....#.......#..#..",
"..#.#...#.#......####.......#..",
"...#.#.......###......#.....#..",
"#......#.......#.#...#.#..##...",
"...#.....#...##.#.....#.#......",
"#.#.#............#..#......#..#",
"....#...#...##.##.##...##.#....",
"..##........#..#........#...##.",
".......#..#...#.........#.....#",
"...........#.#......#...#......",
"...##..##..##..###..#..#..#..#.",
"#..##.......##..#....#....#.#..",
"#.#.##.#..##.....#....#.#......",
"....#..##......#.#..#....#....#",
".#.#.........##...#......##.##.",
"##...........#..#.....#.###....",
".#.###........#...#....##..#...",
"......##.....#.................",
".#.##..#.#.......#......#.#.#..",
".#...#....#.##..........##.##..",
"#...##......####.#....#....#...",
".#...#.##.#.#.....#...#........",
".#................#.##.#.###...",
"...#.#..#.#.....##.....##....#.",
"..##.#..#..##.....#....#...#.##",
"........###.##..#..###.....#..#",
"..##.....#.......#.#...##......",
"#.#..###...##.###.##.#..#...#..",
"#..#..#.#...#....#...##.....#.#",
"#..................#........#..",
"#.....#.......#.##....##....#..",
"...#.............#.....#...#...",
"...#...#.##..##.....#........#.",
".......#........##....###..##..",
".#....#....#.#..#......#....#.#",
"..........#..#.#.....##...#.##.",
".#...##.#...........#.#.......#",
"..#.##.....#.###.#.............",
"..#....###..........#.#.#......",
"#.....#.####..#.#......#..#.#.#",
"...#........#..#...............",
".###.#.##.....#.#...........#..",
"..#....#..#....#..##....#......",
"......#..#.....#.#.##.......#.#",
"###..#...#.#..#....#..##.###..#",
".#....##.###........##...##.#.#",
"........##..##.#....##..#....#.",
"...#..#....#.#....#...#...##...",
"#.....#......#.##........#....#",
"....#....###.##...#.#.##....#..",
"......#.##..#.#..........#...#.",
"...........#...#....##...#....#",
"......#.#.........#....#.#.#...",
".###..........#.###.##....#...#",
"...##.......#......#....#....#.",
"#..#...#.#..####...#......#..#.",
"....##..#.#.........#..........",
".##.###.##....##.####....#...#.",
"..##.......#........#...#..#...",
"....#####..........###....#....",
".#.#..#.#.#....#..#............",
"........#.....#....#.......##..",
"...........##....##..##.....##.",
"..###........#.#.#..#....##...#",
".....#...........##......#..#..",
"...##........#.##.#......##..#.",
"##..#....#............##..#..#.",
".#.....#...##.##..............#",
"#..##........#...#...#......##.",
"......##.....#.......####.##..#",
"...#.#....#...#..#.............",
"..#...#..##.###..#..#.......##.",
"##....###.......#...#..#.......",
"#..#.....###.....#.#.........#.",
"#.#....#.............#...#.....",
"..#.#.##..........#.....##.#...",
".....##......#..#..#.....#..#..",
"##.#..#..#.##......###....#..#.",
"...#............##...#..##.....",
".#..#....#.........#......#.##.",
".##.##...#..............#..#.##",
"...#....#...###...#...#....#..#",
"..#...#..####..#....#.#...##..#",
"..............##.##.......##...",
"..##.#..##...........#.#.#...#.",
"..................##.####.###..",
".#...........#.......#......#..",
".#.#.#...#....#.........##...##",
"....#..........#.#....#.#.....#",
"..........#.#..........#.#.....",
"...........#.....#.#......#....",
"........#..#.#.#.#.............",
"...###...##...##..####.##......",
".#..#......###.....#...#.....#.",
".........##............#.#.....",
"#.#..#.#.#....###.#.#..#..#..##",
"..........#...#.##.#..#..#....#",
"#..#.......##....#..##........#",
"##.#...#....##.............#...",
"....#........#......##..#..#.##",
".................#.#.#.#.#.....",
"...........#.#.....#.......#...",
"#.......#.......#............#.",
"....#...........#.#.##.....#..#",
"#...#.....#....#..##...#.......",
"..#.....#.....#.##.##....#.....",
".#.#..#...#..#..##.....##..#...",
".#.#....#.........####.........",
"#...#..####.....#...#..##......",
"..#...##.#.....#...#.....##....",
".#...#.....#.#.#......#.......#",
"..#.....##.#..#.#...##.........",
"##.#...#..#....#....#.##.##...#",
".#..#....#..##.#.......#..#....",
"...##.#......#...###.......#...",
"...#..#.........##.####........",
"#.#..#..##...........#..#......",
".#...#.#......#.#..........#...",
"...###...#.......#.....#.#...##",
"..#....#.#.##..........##...#..",
".....###.........#.....#..##..#",
".......##.....#.#.....#.#..##..",
".#.#.###..##.......##...#......",
"......#.....#................##",
".#......##..##.#.#...#...#...##",
".#...#......#.......#.#........",
".#..........###...#..#...#.....",
".........##.....#.#..#..#.#...#",
"#...#...#.........#..#..#....#.",
"###.......#.#.....#....##......",
".#..#......#..#...........#..#.",
"..##....##..##...#......#......",
".#........#....#...#....#.....#",
".#.......#...#...#..##.#.#..#..",
"#...#........#.##.....#.....#..",
"#..##.....#..........#...#...##",
"............#...............#..",
".#.##...#.....#.#..#..#..#.....",
".#.#.#...#........#....#...##..",
"##......#.....#.###.#...#.#..#.",
".........##..#..#.#...#...#...#",
"#...#.#....#..#..#.....#.......",
".......#.###...#.............#.",
"..#.....#.#.#..###.#....#.....#",
"....#...#.#....#.#..........#..",
"..#......#.###.#.#..#.....#...#",
"#............#..##...##......#.",
"#...........#..#....#.###..###.",
".#.##.#.#.......#.............#",
"..............#................",
"..#.#.....#.....#...#......#...",
".#.#.#..#..#.#...........##....",
".....##.#......#..#.##....#....",
".......##..#.#.#..#............",
"..#.....#.....#.###..#.....#.#.",
"......##.....#..##.#...#.....#.",
"...#...#....#..#..#........#...",
"..#.##..#....#.........#.#..#..",
"#....#.....###.....#......#....",
"##.....#..#..##.........#.##.##",
".#.#....#.#..........#.........",
".##.#...#..#.......#.##...#....",
"...#...#.....#....#...#.#..#...",
".....#....#.....#.....#.#......",
"...........#.#.......#.......#.",
".........##.###.##........#....",
"#..##.....#...#.#..............",
".#...#....##........#.#..#....#",
"..#...#........#...#..#.##.#..#",
"........#...#.....##.#.#....#.#",
"#..#.......###.#....#.#.#......",
".......#...##....#...#..##..#..",
".....##........#.#.#..#....##..",
".#....#..#.#...........#......#",
"...##....#.##.....##.......#...",
".##..#..#....#.#....#..#....##.",
"..#....#.....###.......#..##..#",
"....#.......#....##..#....#..##",
"....#......##..#....#.#...#.#..",
".##.#......##..................",
"##.#....#........#..#..#...##.#",
".......#..#.#...##.....#.#.....",
"..##.#...........#.#.#..#.#.#..",
".....#....#......#..#.......#..",
"#.#...#.####..##.......#..##...",
"...#....#.....#.##.#..#.##..#..",
".#.......#......##........##.#.",
".......#.#...#..#...#..##.#....",
".#....#........#.#.....##..#..#",
"#..#.....#..#.............#...#",
"#...#....#..#...###..#...#.#...",
".#..#.....#..........#..##.####",
"#.#.#.#.##.#.#.....##.#........",
"...#....##....#...#..##.......#",
"..##.##.#.#........#..........#",
"..###........###..#..........#.",
"...#......#..##.#........#..#..",
"#.#.#..#........#..#..........#",
"...#........#..##.#...#.###....",
"##......#.####.#....#......#...",
".#..#......#................#..",
"#.#........#.#.....##.....##...",
"#...............#..#.......#.#.",
".##..#...........##..#..#.#....",
"#......#.#.......#.#.#.##..#.##",
".....##.#..###.............##..",
"....##.........#..#...#........",
".....#.....#.#.#..#.#..........",
"#.........#....##.#.##.....#..#",
".#.........#......#.#.##.#.#...",
"##.........#.....#..#.#..#.##.#",
"....#......##...#.....#..#..###",
"..#..............#...#..####...",
"#....#...##.#.......#...#..#...",
"#.......###.#.#.......#.......#",
"...##....#.#...........#...###.",
"...........#..#.#.....#..##..#.",
"..#.........#..###..#.....#...#",
"..#.#.....#.#.#...#.#.#......#.",
"........#.....#.#......##....##",
"##.#.#...#.#........#.....#...#",
"........#....#...............#.",
"##.###......####...#####..#....",
"...##...#..#....#........#...#.",
"...###.#..................##.#.",
"##.#.......###.......#...#.#...",
"....#..#.#...#...#....#.#.#..##",
"....#...........#..#...........",
"#..#.#..#...#...#..#...........",
"...#...#.#....#..#....#........",
"#....#.......#.##........#..#..",
".....#...#..#................#.",
"#......#.......#..........##..#",
".#....#.#......#.#...#....##..#",
"...#.##...#......#.#...##...##.",
"..#...#..##...#...#....#.......",
".....#....#.#.#..........#.#...",
"...#...#..#....#..#.#..........",
"......#.#..........##.......#..",
".#...##.#.#...#..##..#...#.....",
"..#..#.........#........#.#.#..",
"#.#..##..#.....##......#.....#.",
"#..#.....#.#....#...#.#....#.#.",
"......#........##.#..#...#.....",
"...#.##.#.#......#.#..##...#..#",
"....#..###..#..#.....###....##.",
".....#...#.#.....#..........#.#",
".#...##..##.....#..#...#.#.#...",
".##.#......##...##..#...#.....#",
".#.##....#...#.##.#.#...#.#...#",
"....#.#...#....###.#.....#.....",
"#.....####................#..#.",
"....#.....#...#.#.......##.#...",
".#...##.#...#..#...........#.#.",
"..#####..#.#...#...##........#.",
"...#...##........#...#.#....###",
"........#.#.#..#.....#.......#.",
"...#...#..##............##.....",
"#.#..###....###.#...#.#...##.##",
"..#.##...#......#..#.........##",
".##..#..#.....#..#.........#.#.",
".#..#.#....#.##...#..#.##....##",
"..#...#.#...##.#.#...#...#....#",
"#..........#.......##..##....#.",
"#...###.#......#....#.........#",
"#.....#...##.......##....##....",
".##.#..#.##......#.##....#..#..",
"............#.#....##.#..#....#",
".#.........##.##...#....#.....#",
"##....##..#..#....##...#.....##",
"...#.....#...........#.....##..",
"......#...#.........#.......#..",
"............#...##.#.....#.#.#.",
".#........##..........#.....#.#",
".###.........#.....#.##...#....",
".##..#...##...#..#..#.##......."
]

"""
General idea: 
Horizontal movement mod by 31, each iteration moves to the right by 3, FORCED.
vertical movement, if it is passed = cleared.
"""

x = 0
y = len(inputs)
# print(len(inputs[0]))
encounter = 0
for i in inputs:
    if i[x%31] == '#':
        encounter += 1
    x+=3

print(encounter)

# part 2
movement = ((1,1),
            (3,1),
            (5,1),
            (7,1),
            (1,2)
            )


encounterp2 = []


for slope in movement:
    tree = 0
    xslope = slope[0]
    yslope = slope[1]
    x = 0
    for i in range(0, len(inputs),yslope):
        if inputs[i][x%31] == '#':
            tree += 1
        x += xslope
    encounterp2.append(tree)

print(encounterp2)

# product = reduce(lambda x,y : x * y, encounterp2)
loopproduct = 1
for i in encounterp2:
    loopproduct *= i

print(loopproduct)
