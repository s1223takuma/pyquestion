#結果表示時のために「円」を書き入れているため、無くても計算できていれば大丈夫です

memo = {"卵":300, "大根":200, "ちくわ":200, "はんぺん":250, "こんにゃく":150, "もち巾着":400,"しらたき":100,"ごぼう巻き":100,"牛すじ":500,"さつま揚げ":250,"つくね":200,"たけのこ":300,"昆布":30,"からし":20}

print("------Q1------")
print(memo)

print("------Q2------")
sumvalue = 0
for value in memo.values():
    sumvalue += value
print(str(sumvalue)+"円")

# print(sum(memo.values()))　別解

print("------Q3------")

maxvalue = 0
for key,value in memo.items():
    if value >= maxvalue:
        maxvalue = value
for key,value in memo.items():
    if value == maxvalue:
        print(f"{key}：{value}円")

#print(max(memo.items(), key=lambda x: x[1]))　別解


print("------Q4------")
sum = 0
for key,value in memo.items():
    if value <= 200:
        print(f"{key} {value}円")
        sum = sum + value
print(str(sum)+"円")