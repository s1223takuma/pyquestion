無限ループとrandomモジュールの問題です

詰まったら下の関数をお使いください

```
def gacha():
    hit = random.random()
    if hit < 0.01:
        return True
    else:
        return False
```

この関数はガチャを回してSSRが出た時に戻り値としてTrueを返します。
あとはWhileでTrueになるまで無限ループをさせて何回かかったかカウントしてみたらいいかも！