# day 4 passport check
import re
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
goodPassports = []
for passport in inputs:
    check = passport.split()
    temp = {}
    if len(check) == 7:
        if all('cid' not in i for i in check):
            validPassport +=1 
            for i in check:
                holder = i.split(':')
                temp.update({holder[0]:(holder[1])})
            goodPassports.append(temp)
    elif len(check) == 8:
        validPassport +=1
        for i in check:
            holder = i.split(':')
            temp.update({holder[0]:(holder[1])})
        goodPassports.append(temp)



print(validPassport)

# part 2
validPassportp2 = 0

for i in goodPassports:
    if (
    ( int(i['byr']) >= 1920 and int(i['byr']) <= 2002 and len(i['byr']) == 4 ) and
    ( int(i['eyr']) >= 2020 and int(i['eyr']) <= 2030 and len(i['eyr']) == 4 ) and
    ( int(i['iyr']) >= 2010 and int(i['iyr']) <= 2020 and len(i['iyr']) == 4 ) and
    (re.search(r"(1[5-8]\dcm|19[0-3]cm)|(59in|6\din|7[0-6]in)",i['hgt'])) and
    (re.search(r"#[a-f0-9]{6}",i['hcl'])) and
    (re.search(r"(amb|blu|brn|gry|grn|hzl|oth)",i['ecl'])) and
    (re.search(r"\d{9}",i['pid']))
    ):
        validPassportp2 += 1

print(validPassportp2)
#111

#110 too low - 112 too high probably due to data error?