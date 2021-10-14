import argparse
import secrets

# 引数のパーサー
a_parser = argparse.ArgumentParser(description="Randomize inputs.")
a_parser.add_argument("--rich", action="store_true", help="Provide rich view.")
a_parser.add_argument("elems", nargs="*", help="Some elements that is need randomized.")

args = a_parser.parse_args()
elems = args.elems
n_elems = []

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

if args.rich:
    for i in range(len(n_elems)):
        e = n_elems[i]

        # 選出順位を表示
        print(i + 1, end = "")

        # 上罫線の表示
        j = 0
        while j < len(e) + 3:
            print("-", end = "")
            j += 1

        # 選出されたelementを表示
        print("\n|", e, "|")

        # 下罫線の表示
        j = 0
        while j < len(e) + 4:
            print("-", end = "")
            j += 1

        # リスト最後の"↓"は不要なのでbreak
        if i == len(n_elems) - 1:
            print()
            break

        print("\n↓")

else:
    print(n_elems)
