import CHaser # 同じディレクトリに CHaser.py がある前提
import random # 乱数を使う時に必要

"""
このファイルを直接実行したときに実行する関数．
実行するまでの経緯はファイルの下部に記載．

get_ready() → 行動関数 → get_ready() → ... の順で必ず処理を行う．
行動関数は「内容_方向()」の命名規則に従って名付けられる．

内容は「walk」「look」「search」「put」の4種類．
方向は「right」「up」「left」「down」の4種類．この組み合わせで関数を命名．
例) walk_up()，search_right() など

行動関数が返すリストは行動後のマップ情報9つ．
[ ][x][x]
[ ][C][♡]
[H][ ][ ]
このときは [0, 2, 2, 0, 0, 3, 1, 0, 0] が返る．
"""
def main():
    value = [] # フィールド情報を保存するリスト
    client = CHaser.Client() # サーバーと通信するためのインスタンス

    while(True):
        value = client.get_ready() # サーバーに行動準備が完了したと伝える
        rand  = random.randint(0,3) # 変数randに0から3までの乱数（整数）を入れる
        if rand == 0: # もしrandが0なら
            value = client.walk_up() # 上に行く
        elif rand == 1: # もしrandが1なら
            value = client.walk_down() # 下に行く
        elif rand == 2: # もしrandが2なら
            value = client.walk_left() # 左に行く 
        elif rand == 3: # もしrandが3なら
            value = client.walk_right() # 右に行くく       
        
        

"""
python sample.py のようにこのファイルを直接実行すると，
__name__ は "__main__" となる．これを利用して main() を実行する．
"""
if __name__ == "__main__":
    main()