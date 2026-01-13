x = [38, 46, 6, 119, 57, 31, 45, 63, 49, 95, 57, 114, 4, 22, 48, 8, 101, 63, 63, 61, 17, 38, 123, 39, 34, 96, 36, 27, 121, 59, 105, 109, 1, 13, 110, 80, 83, 88, 86, 44, 78, 117, 75, 129, 85, 121, 99, 70, 4, 65, 91, 61, 101, 23, 113, 105, 18, 24, 130, 38, 98, 50, 95, 14, 76, 47, 113, 77, 26, 35, 9, 119, 112, 107, 64, 98, 99, 94, 3, 10, 77, 124, 106, 57, 28, 49, 30, 24, 71, 56, 105, 22, 127, 125, 23, 22, 92, 11, 117, 48]

print("------Q1------")
def selfmax(l):
    num = 0
    for n in l:
        if num < n:
            num = n
    return num

def selfmin(l):
    num = l[0]
    for n in l:
        if num > n:
            num = n
    return num

print(selfmax(x))
print(selfmin(x))

print("------Q2------")
num = {}
for n in x:
    num[n] = 0
max_cnt = 0
for n in x:
    num[n] += 1
    if max_cnt < num[n]:
        max_cnt = num[n]
print(max_cnt)

print("------Q3------")
num = 0
for n in x:
    num += n
print(num)

print("------Q4------")
num = 0
cnt = 0
for n in x:
    num += n
    cnt += 1
print(num/cnt)
