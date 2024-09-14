import random

def gacha():
    #1%が当たったらTrue,外れたらfalseを返します
    hit = random.random()
    if hit < 0.01:
        return True
    else:
        return False



judg = False
count = 0
while judg == False:
    count += 1
    judg = gacha()
print(f"{count}回で排出されました")
