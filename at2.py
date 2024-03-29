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
# 左側から数える
def main():
    value = [] # フィールド情報を保存するリスト
    client = CHaser.Client() # サーバーと通信するためのインスタンス"
    muki = "down" # mukiをdownにする
    turn = 0

    while(True):
        value = client.get_ready() # 行動する前には必ず get_ready() する
        print(muki)
        print(turn)

        if value[1] == 1: # もし上が敵なら
            value = client.put_up() # 上にブロックをおく
        elif value[3] == 1:
            value = client.put_left()
        elif value[5] == 1:
            value = client.put_right()
        elif value[7] == 1:
            value = client.put_down()

        if value[0] == 1 and value[7] != 2: # 左上に敵がいるかつ下がブロックではないなら
            value = client.walk_down() #　下に行く
        elif value[0] == 1 and value[5] != 2: # 左上に敵があるかつ右がブロックではないなら
            value = client.walk_right() #  右に行く
        elif value[0] == 1 and value[5]== 2 and value[7] == 2: # 左上に敵があるかつ右がブロックではないなら
            value = client.look_up()     
        elif value[2] == 1 and value[3] != 2: # 右上に敵があるかつ左がブロックではないなら
            value = client.walk_left()    
        elif value[2] == 1 and value[7] != 2: # 左上に敵があるかつ右がブロックではないなら
            value = client.walk_down()   
        elif value[6] == 1 and value[1] != 2: # 左下に敵がいるかつ上がブロックではないなら
            value = client.walk_up() #　上に行く
        elif value[6] == 1 and value[5] != 2: # 左下に敵があるかつ右がブロックではないなら
            value = client.walk_right() #  左に行く 
        elif value[8] == 1 and value[1] != 2: # 右下に敵があるかつ左がブロックではないなら
            value = client.walk_left()    
        elif value[8] == 1 and value[3] != 2: # 右下に敵があるかつ左がブロックではないなら
            value = client.walk_left()                     

        elif value[1] == 3: # もし上がアイテムなら
            value = client.walk_up() # 上に行く
        elif value[3] == 3:
            value = client.walk_left()
        elif value[5] == 3:
            value = client.walk_right()
        elif value[7] == 3:
            value = client.walk_down()
        elif value[0] == 3 and value[1] != 2: # 左上にアイテムがあるかつ上がブロックではないなら
            value = client.walk_up() #　上に行く
        elif value[0] == 3 and value[3] != 2: # 左上にアイテムがあるかつ左がブロックではないなら
            value = client.walk_left() #  左に行く
        elif value[2] == 3 and value[1] != 2: # 右上にアイテムがあるかつ上がブロックではないなら
            value = client.walk_up() #　上に行く
        elif value[2] == 3 and value[5] != 2: # 右上にアイテムがあるかつ右がブロックではないなら
            value = client.walk_right() #  右に行く
        elif value[6] == 3 and value[7] != 2: # 左下にアイテムがあるかつ下がブロックではないなら
            value = client.walk_down() #　上に行く
        elif value[6] == 3 and value[3] != 2: # 左下にアイテムがあるかつ左がブロックではないなら
            value = client.walk_left() #  左に行く        
        elif value[8] == 3 and value[7] != 2: # 左上にアイテムがあるかつ上がブロックではないなら
            value = client.walk_down() #　上に行く
        elif value[8] == 3 and value[5] != 2: # 左上にアイテムがあるかつ左がブロックではないなら
            value = client.walk_right() #  左に行く
                   
              
    

                       
        else: # 上も下も右もひだりもアイテムではないなら

            rand = random.randint(0,3)

            if turn == 5: # もしturnが10なら
                turn = 0
                if rand == 0: #　もしrandが0なら上にいく
                    if value[1] != 2:
                        value = client.walk_up()
                        muki = "up"
                    elif value[5] != 2:
                        value = client.walk_right()
                        muki = "right"
                    elif value[3] != 2:
                        value = client.walk_left()
                        muki = "left"
                    elif value[7] != 2:
                        value = client.walk_down()   
                        muki ="down" 
                elif rand == 1: #　もしrandが1なら右にいく
                    if value[5] != 2:
                        value = client.walk_right()
                        muki = "right"
                    elif value[1] != 2:
                        value = client.walk_up()
                        muki = "up"
                    elif value[3] != 2:
                        value = client.walk_left()    
                        muki = "left"    
                    elif value[7] != 2:
                        value = client.walk_down()
                        muki = "down"
                elif rand == 2: # もしrandが１なら下に行く
                    if value[7] != 2:
                        value = client.walk_down()
                        muki = "down"
                    elif value[1] != 2:
                        value = client.walk_up()
                        muki = "up"
                    elif value[5] != 2:
                        value = client.walk_right()
                        muki = "right"
                    elif value[3] != 2:
                        value = client.walk_left()
                        muki = "left"           
                elif rand == 3: # もしrandが3なら下に行く
                    if value[3] != 2:
                        value = client.walk_left()
                        muki = "left"
                    elif value[7] != 2:
                        value = client.walk_down()
                        muki = "down"
                    elif value[5] != 2:
                        value = client.walk_right()
                        muki = "right"
                    elif value[1] != 2:
                        value = client.walk_up()
                        muki = "up"

            elif muki == "down": # もしmukiがdownなら
                turn += 1 
                if value[7] != 2: # もし自分の下がブロックではないなら またはアイテムなら
                    value = client.walk_down() # 下に行く   
                elif value[3] != 2: # もし自分の下がブロックで左がブロックではないなら
                    value = client.walk_left()
                    muki = "left"
                elif value[5] != 2: # もし左と下がブロックで右がブロックでないなら右に行く
                    value = client.walk_right() # 右に行く  
                    muki = "right" 
                else: # もし右と左と下がブロックなら上にいく
                    value = client.walk_up() # 上に行く
                    muki = "up"  

            elif muki == "up": # もしmukiがupなら
                turn += 1 
                if value[1] != 2: # もし自分の上がブロックではないなら    
                    value = client.walk_up() # 上に行く     
                elif value[5] != 2: # もし上がブロックで右がブロックでないなら     
                    value = client.walk_right() # 右に行く    
                    muki = "right"
                elif value[3] != 2 : # もし上と右がブロックで左がブロックではないなら左に行く
                    value = client.walk_left()
                    muki = "left"
                else: # もし上も左も右もブロックなら下に行く
                    value = client.walk_down()
                    muki = "down"

            elif muki == "right": # もしmukiがrightなら
                turn += 1 
                if value[5] != 2: # もし自分の右がブロックではないなら 
                    value = client.walk_right() # 右に行く 
                elif value[7] != 2 : # 右がブロックで下がブロックでないなら
                    value = client.walk_down() # 下に行く
                    muki = "down"
                elif value[1] != 2: # 右と下がブロックで上がブロックでないなら
                    value = client.walk_up()
                    muki = "up"
                else: # 右も上も下もブロックなら
                    value = client.walk_left()
                    muki = "left"

            elif muki == "left": # もしmukiがleftなら
                turn += 1 
                if value[3] != 2: # もし自分の左がブロックではないなら 
                    value = client.walk_left() # 左に行く   
                elif value[1] != 2: # 左がブロックで上がブロックでないなら
                    value = client.walk_up() # 上に行く 
                    muki = "up"
                elif value[7] != 2: #左も上もブロックで下がブロックでないなら
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