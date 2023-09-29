'''for i in range(1, 11):
    if i == 6:
        break
    print(i)
    
for i in range(1, 20):
    if i % 2 == 0:
        continue
    print(i)


n = int(input())
lis = []

for i in range(n):
 lis.append(int(input()))

for v in range (len(lis)):
 for x in range(v):
  if lis[x] > lis[v]:
   temp = lis[x]
   lis[x] = lis[v]
   lis[v] = temp

print(lis)

n = int(input())
lst = []

for i in range(n):
 lst.append(int(input()))

#tạo một list con chứa các số cần hiển thị
lstcon = []
for i in lst:
 if i % 2 == 1:
  lstcon.append(i)

print(lstcon)

s = input()
scon = []
if len(s) < 2:
 print("")
else:
 for i in range(-2, 2):
  scon.append(s[i])

print(scon)

s1 = input()
s2 = input()

s1.split(" ")
print(s1)

for i in range (len(s1)): 
 print(s1[i])

for i in range(len(s2)): 
 print(s2[i])




def show(s):
    t_lower = 0
    t_upper = 0
    for c in s:
     if c.islower() == True:
      
      t_lower += 1
     if c.isupper() == True:
      t_upper += 1
    print(s)
    print("Number of uppercase letters: ", t_upper)
    print("Number of lowercase letters: ", t_lower)


s = str(input())
show(s)


#Initial list
res = []

# Input lengths
lengths = int(input())

# Add element
for i in range(lengths):
    # Input elements
    n = int(input())
    res.append(n)

def evenNum(res):
 even = []
 for i in res:
  if i % 2 == 0:
   even.append(i)
 print(even)

evenNum(res)
'''

#Phương pháp tìm ước chung lớn nhất euclid:
'''
ta có: a = 234 và b = 192
 234 chia hết cho 192 được 1 dư 42, a = 192 và b = 42
 192 chia hết cho 42 được 4 dư 24, a = 42 và b = 24
 42 chia hết cho 24 được 1 dư 18, a = 24 và b = 18
 24 chia hết cho 18 được 1 dư 6, a = 18 và b = 6
 18 chia hết cho 6 được 3 dư 0, a = 6 và b = 0
 


def common(a, b):
    while b > 0:
        sum = a % b
        a , b = b , sum
    return a


a = int(input())
b = int(input())

print(common(a, b))

a = int(input())
b = int(input())
c = int(input())
if (a, b, c) != 0:
  if a == b == c:
   print("Equilateral triangle")
  elif a == b or b == c or a == c:
   print("Isosceles triangle")
  else:
   print("Scalene triangle")



   #Initial list
res = []

# Input lengths
lengths = int(input())

# Add element
for i in range(lengths):
    # Input elements
    n = int(input())
    res.append(n)
s = list(map(str, res))
print("".join(s))


s = str(input())

def format(s):
 st1 = s[-3:]
 st2 = "ing"
 st3 = "ly"
 if len(s) >= 3:
  if st1 != st2: 
   return(s + st2)
  if st1 == st2:
   return(s + st3)
 else:
  return s

print(format(s))



n = int(input())

def sumOfAll(n):
 sum = 0
 for i in range(1, n):
  if n % i == 0:
   sum +=i
 if sum > n:
  return "true"
 return "false"
print(sumOfAll(n))




num = int(input())
def pow_two(num):
 x = (2 ** num) % ((10 ** 9) + 7)
 return x

print(pow_two(num))



x = int(input())
if x > 0:
 n = x ** 0.5
 if  n % (n // 1) == 0:
    print("YES")
 else:
    print("NO")
else:
  print("NO")
'''

'''
ds = input().split()
i = 1
total = ds[0]
while i < len(ds):
    if ds[i] == '+' and ds[i + 2] != '*' and ds[i + 2] != '/':
        total += format(ds[i + 1])
    elif ds[i]== '-' and ds[i + 2] != '*' and ds[i + 2] != '/':
        total -= float(ds[i + 1])
    elif i == '*'and ds[i - 2] != '*' and ds[i - 2] != '/' and ds[i + 2] != '*' and ds[i + 2] != '/':
        if ds[i - 2] == '+':
            total += float(ds[i - 1]) * float(ds[i + 1])
        elif ds[i - 2] == '-':
            total -= float(ds[i - 1]) * float(ds[i + 1])
    elif i == '/'and ds[i - 2] != '*' and ds[i - 2] != '/' and ds[i + 2] != '*' and ds[i + 2] != '/':
        if ds[i - 2] == '+':
            total += float(ds[i - 1]) / float(ds[i + 1])
        elif ds[i - 2] == '-':
            total -= float(ds[i - 1]) / float(ds[i + 1])
    i +=2
print(len(ds))
print(total)

'''
n = int(input())
s = 0
if 2 <= n <= 10000:
    for i in range(2, n + 1):
      s += 1/i
print("{:.4f}".format(s))
djfsakjflkd
fdjasklfjd
asdjflkjasldkf
lakdsjflkajdslfk
laksdjflkajdslkfj
alkdsjflkajsdlkfj
lakdjfjalsdkfja
alkjdsflkajsdlkfj
lakdsflkjalkdsjf
laksdjflkajsldkfj
laksdjfklajdlksfj
alksdjflkjaldkjf
