# 問題1
あなたはお使いに行くことになりました。
買い物リストは以下の通りです（辞書型で作成 {key:品名, value:値段}）：


```memo = {"卵":300, "大根":200, "ちくわ":200, "はんぺん":250, "こんにゃく":150, "もち巾着":400,"しらたき":100,"ごぼう巻き":100,"牛すじ":500,"さつま揚げ":250,"つくね":200,"たけのこ":300,"昆布":30,"からし":20}```

やること：
1. 買い物リスト（memo辞書）の内容を表示してください。
2. リストにある品物の合計金額を計算し、表示してください。
3. 最も高価な商品とその価格を表示してください。
4. 200円以下の商品を、「商品名：金額」と表示してください。また、200円以下の商品の合計金額も表示してください


# 問題2
あなたは人気のモバイルゲームで使われているガチャ（ランダムアイテム抽選）システムをシミュレートするプログラムを作成しています。
ゲーム内の最高レアリティキャラクター「SSR」の排出確率は1%です。

やること：
1. SSRキャラクターが出るまでガチャを繰り返し引くプログラムを作成してください。
2. SSRキャラクターが出たら、何回目の挑戦で引けたかを表示してください。


# 問題3
以下のコードのエラーを修正してください。
```
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
print(name + "さんは未成年です。")

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
count =0

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

result = num1/count

print("計算結果:", result)

# プログラムの終了
print("プログラムを終了します。お疲れ様でした！")
```
