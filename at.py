import CHaser # 同じディレクトリに CHaser.py がある前提
import random
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
    client = CHaser.Client() # サーバーと通信するためのインスタンス"
    muki = "down" # mukiをdownにする
    turn = 0

    while(True):
        value = client.get_ready() # 行動する前には必ず get_ready() する
        rand  = random.randint(0,3)

        if turn == 10: # もしturnが10なら
            if rand == 0: #　もしrandが0なら上にいく
                value = client.walk_up()
                muki = "up"
                turn = 0
            elif rand == 1: #　もしrandが1なら右にいく
                value = client.walk_right()
                muki = "right"
                turn = 0
            elif rand == 2: #　もしrandが2なら左にいく
                value = client.walk_left()
                muki ="left"
                turn = 0
            elif rand == 3: #　もしrandが3なら上にいく
                value = client.walk_down()
                muki = "down" 
                turn = 0

        elif muki == "down": # もしmukiがdownなら
            if value[7] != 2 or value[7] == 3: # もし自分の下がブロックではないなら またはアイテムなら
                value = client.walk_down() # 下に行く   
                turn += 1 
            elif value[3] != 2 or value[3] == 3: # もし自分の下がブロックで左がブロックではないなら
                value = client.walk_left()
                muki = "left"
                turn += 1
            elif value[5] != 2 or value[5] == 3: # もし左と下がブロックで右がブロックでないなら右に行く
                value = client.walk_right() # 右に行く  
                muki = "right"
                turn += 1 
            else: # もし右と左と下がブロックなら上にいく
                value = client.walk_up() # 上に行く
                muki = "up" 
                turn += 1 

        elif muki == "up": # もしmukiがupなら
            if value[1] != 2 or value[1] == 3: # もし自分の上がブロックではないなら    
                value = client.walk_up() # 上に行く    
                turn += 1   
            elif value[5] != 2 or value[5] == 3: # もし上がブロックで右がブロックでないなら     
                value = client.walk_right() # 右に行く    
                turn += 1 
                muki = "right"
            elif value[3] != 2 or value[3] == 3: # もし上と右がブロックで左がブロックではないなら左に行く
                value = client.walk_left()
                muki = "left"
                turn
            else: # もし上も左も右もブロックなら下に行く
                value = client.walk_down()
                muki = "down"
        elif muki == "right": # もしmukiがrightなら
            if value[5] != 2 or value[5] == 3: # もし自分の右がブロックではないなら 
                value = client.walk_right() # 右に行く   
            elif value[7] != 2 or value[7] == 3: # 右がブロックで下がブロックでないなら
                value = client.walk_down() # 下に行く 
                muki = "down"
            elif value[1] != 2 or value[1] == 3: # 右と下がブロックで上がブロックでないなら
                value = client.walk_up()
                muki = "up"
            else: # 右も上も下もブロックなら
                value = client.walk_left()
                muki = "left"
        elif muki == "left": # もしmukiがleftなら
            if value[3] != 2 or value[3] == 3: # もし自分の左がブロックではないなら 
                value = client.walk_left() # 左に行く   
            elif value[1] != 2 or value[1]: # 左がブロックで上がブロックでないなら
                value = client.walk_up() # 上に行く 
                muki = "up"
            elif value[7] != 2 or value[7]: #左も上もブロックで下がブロックでないなら
                value = client.walk_down() # 下に行く 
                muki = "down"
            else: # 左も上も下もブロックなら
                value = client.walk_right() # 右に行く
                muki = "right"
"""
python sample.py のようにこのファイルを直接実行すると，
__name__ は "__main__" となる．これを利用して main() を実行する．
"""
if __name__ == "__main__":
    main()