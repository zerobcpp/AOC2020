# day 6 Custom Customs
with open("6data.txt") as data:
    inputs = data.read()

# Valid string round = 0 2 4 6 8
# inputs round = 1 3 5 7
## Wrong interpretation, count the letter only

inputs = inputs.split('\n\n')


yesCount = 0


for i in inputs:
    occured = set()
    occured.update(i)
    try:
        occured.remove('\n')
    except:
        print("Some lines doesn't have '\\n'")

    yesCount += len(occured)



print(yesCount)

#6416
    #12322 too high
    #counted '\n'

#part 2
yesCountp2 = 0
print(inputs[0])
for i in inputs:
    i = i.split('\n')
    occured = set(i[0])
    for j in i:
        occured = occured.intersection(set(j))
    
    yesCountp2 += len(occured)

print(yesCountp2)

#3050