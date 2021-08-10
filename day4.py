# day 4 passport check
"""
byr (Birth Year)
iyr (Issue Year)
eyr (Expiration Year)
hgt (Height)
hcl (Hair Color)
ecl (Eye Color)
pid (Passport ID)
cid (Country ID)
"""
# data reform
inputs = []
inputstr = ""
with open ("day4data.txt") as data:
    for lines in data:
        if lines not in ['\r\n','\n']:
            inputstr += lines
        else:
            inputs.append(inputstr)
            inputstr = ""

# part 1

REQ = ['byr','iyr','eyr','hgt','hcl','ecl','pid']

validPassport = 0
for passport in inputs:
    check = passport.split()
    if all (i in check for i in REQ):
        validPassport +=1 
    


print(validPassport)

#232  too low 
#253 too high
# 1000 too high


#112 with 8 len