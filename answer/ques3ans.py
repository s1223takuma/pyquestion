# 変数の使用
name = "太郎"
age = 25
height = 170.5

# 画面に出力
print("こんにちは、世界！")
print("私の名前は" + name + "です。")
print("年齢は", age, "歳です。")
print("身長は", height, "cmです。")

# 基本的な計算
x = 10
y = 5
print("x + y =", x + y)
print("x - y =", x - y)
print("x * y =", x * y)
print("x / y =", x / y)

# if文による条件分岐
if age >= 20:
    print(name + "さんは成人です。")
else:
    print(name + "さんは未成年です。") #←ココ修正

# リストの使用
fruits = ["りんご", "バナナ", "オレンジ"]
print("果物リスト:", fruits)
print("最初の果物:", fruits[0])
print("最後の果物:", fruits[-1])

# リストへの要素の追加
fruits.append("ぶどう")
print("追加後の果物リスト:", fruits)

# for文によるループ
print("果物一覧:")
for fruit in fruits:
    print("- " + fruit)

# while文によるループ
count = 0
while count < 5:
    print("カウント:", count)
    count = count + 1
count = 0

# 文字列の操作
message = "Python is fun!"
print("元のメッセージ:", message)
print("大文字に変換:", message.upper())
print("小文字に変換:", message.lower())
print("単語数:", len(message.split()))

# 入力の受け取り
user_input = input("好きな食べ物を入力してください: ")
print("あなたの好きな食べ物は" + user_input + "ですね！")

# 数値の入力と型変換
birth_year = int(input("あなたの生まれ年を入力してください: "))
current_year = 2024
age = current_year - birth_year
print("あなたは約", age, "歳ですね。")

# 簡単な計算機
num1 = float(input("1つ目の数字を入力してください: "))
num2 = float(input("2つ目の数字を入力してください: "))

result = num1/num2 #←ココ修正

print("計算結果:", result)

# プログラムの終了
print("プログラムを終了します。お疲れ様でした！")