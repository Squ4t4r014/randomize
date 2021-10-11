import sys
import secrets

elems = sys.argv
n_elems = []

# argv[0]はスクリプトのパスなので削除
del elems[0]

i = len(elems)

while i > 0:
    # 選出
    e = secrets.choice(elems)

    # 新リストへ追加
    n_elems.insert(-1, e)

    # 旧リストからの削除
    p_index = elems.index(e)
    del elems[p_index]
    i-=1

print(n_elems)
