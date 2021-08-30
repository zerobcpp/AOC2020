from math import ceil
test = '''939
7,13,x,x,59,x,31,19'''

accepted = '''1008833
19,x,x,x,x,x,x,x,x,41,x,x,x,x,x,x,x,x,x,643,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,17,13,x,x,x,x,23,x,x,x,x,x,x,x,509,x,x,x,x,x,37,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,29'''

a = test.split('\n')
b = accepted.split('\n')
time = int(b[0])
buses = [int(i) for i in b[1].split(',') if i.isdigit()]
buses.sort()

print(f'time is {time} \nbuses are: {buses}')

c = [i * ceil(time/i) for i in buses]
upperLimit = max(c)

arrivalTime = 0
arrivalBus = 0
found = False
for i in range(time,upperLimit):
    for bus in buses:
        if i % bus == 0:
            arrivalBus = bus
            arrivalTime = i
            found = True
    if found:
        break

print(f'''arrivalTime = {arrivalTime}, arrivalBus = {arrivalBus}
Result = {(arrivalTime - time)*arrivalBus}''')


# __ part 2 __  
# ( imagine trying to bruteforce this , what a digital dummy )

# for i in range(initialBus, 10000000000000):
#     if i % initialBus == 0:
#         count = 0
#         for j in range(i+1, 10000000000000):
#             print(f'checking from {i} and continuing at {j}')
#             disconnect = False
#             for index in range(count, len(part2Bus[1:])):
#                 if part2Bus[index+1] == 'x':
#                     count += 1
#                     break
#                 elif j % int(part2Bus[index+1]) == 0:
#                     count += 1
#                     break
#                 else:
#                     disconnect = True
#                     break
#             if disconnect:
#                 break
#             elif count >= 78:
#                 break
#     if count >= 78:
#         print(i)
#         break
    
# Chinese remainder theorem :
# a_i = remainder value
# N_i = Product of all modulus(Bus ID)/current BUS ID
# M_i*N_i + m_i*n_i = 1 
def modinverse(a, m):
    a %= m
    for i in range(1,m):
        if (a*i) % m == 1:
            return i
    return 1


part2Bus = b[1].split(',')
print(part2Bus)

arr = []
totalProduct = 1
for i, v in enumerate(part2Bus):
    if v != 'x':
        v = int(v)
        ai = i % v
        totalProduct *= v
        arr.append(((v-ai)%v,v))

print(totalProduct)
print(arr)
tot = 0
for t, modu in arr:
    Ni = totalProduct // modu
    minverse = modinverse(Ni, modu)
    #assert minverse*Ni % modu == 1
    #print(Ni, minverse, Ni*minverse, sep = '          ')
    xi = Ni * minverse * t
    tot += (Ni*minverse*xi)

print(tot%totalProduct)
