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
    muki = "left" # mukiをdownにする
    turn = 100
    print(turn)

    def look_walk_up():
        rand = random.randint(1,3) # 1から3の乱数を作る
        if rand == 1: # もし乱数が1なら
            value = client.look_up() # 上の3×3マスを調べる
            if value[4] != 1: # もし2つ上が敵でなければ
                value = client.get_ready()
                value = client.walk_up()    
            else: # もし2つ上が敵なら
                value = client.get_ready()
                value = client.put_up()
        else: # 乱数が2か3なら
            value = client.walk_up() # 上に行く
    
    def look_walk_down():
        rand = random.randint(1,3) # 1から3の乱数を作る
        if rand == 1: # もし乱数が1なら
            value = client.look_down() # 下の3×3マスを調べる
            if value[4] != 1: # もし2つ下が敵でなければ
                value = client.get_ready()
                value = client.walk_down()
            else: # もし2つ下が敵なら
                value = client.get_ready()
                value = client.put_down()
        else: # 乱数が2か3なら
            value = client.walk_down() # 下に行く 

    def look_walk_right():
        rand = random.randint(1,3) # 1から3の乱数を作る
        if rand == 1: # もし乱数が1なら
            value = client.look_right() # 右の3×3マスを調べる
            if value[4] != 1: # もし2つ右が敵でなければ
                value = client.get_ready()
                value = client.walk_right()
            else: # もし2つ右が敵なら
                value = client.get_ready()
                value = client.put_right()
        else: # 乱数が2か3なら
            value = client.walk_right() # 右に行く

    def look_walk_left():
        rand = random.randint(1,3) # 1から3の乱数を作る
        if rand == 1: # もし乱数が1なら
            value = client.look_left() # 左の3×3マスを調べる
            if value[4] != 1: # もし2つ左が敵でなければ
                value = client.get_ready()
                value = client.walk_left()
            else: # もし2つ左が敵なら
                value = client.get_ready()
                value = client.put_left()
        else: # 乱数が2か3なら
            value = client.walk_left() # 左に行く
                      
    while(True):
        value = client.get_ready() # 行動する前には必ず get_ready() する
        turn = turn - 1  # get_readyをしたらturnを1減らす

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
        elif value[0] == 1 and value[5]== 2 and value[7] == 2: # 左上に敵があるかつ右がブロックで下もブロックなら
            value = client.look_up()     
        elif value[2] == 1 and value[3] != 2: # 右上に敵があるかつ左がブロックではないなら
            value = client.walk_left()    
        elif value[2] == 1 and value[7] != 2: # 右上に敵があるかつ右がブロックではないなら
            value = client.walk_down()
        elif value[2] == 1 and value[3]== 2 and value[7] == 2: # 左上に敵があるかつ左がブロックで下もブロックなら
            value = client.look_up()       
        elif value[6] == 1 and value[1] != 2: # 左下に敵がいるかつ上がブロックではないなら
            value = client.walk_up() #　上に行く
        elif value[6] == 1 and value[5] != 2: # 左下に敵があるかつ右がブロックではないなら
            value = client.walk_right()
        elif value[6] == 1 and value[5]== 2 and value[1] == 2: # 左上に敵があるかつ右がブロックで上もブロックならいなら
            value = client.look_up()    
        elif value[8] == 1 and value[1] != 2: # 右下に敵があるかつ上がブロックではないなら
            value = client.walk_up()    
        elif value[8] == 1 and value[3] != 2: # 右下に敵があるかつ左がブロックではないなら
            value = client.walk_left()
        elif value[8] == 1 and value[3]== 2 and value[1] == 2: # 右下に敵があるかつ左がブロックで上もブロックなら
            value = client.look_up()                         

        elif value[1] == 3: # もし上がアイテムなら
            if value[0] == 2 and value[2] == 2: # 左上がブロックかつ右上もブロックなら
                value = client.put_up() # 上にブロックを置く
            else: # でなければ
                look_walk_up() # 関数look_walk_upを呼び出す
            
        elif value[5] == 3: # もし右がアイテムなら
            if value[2] == 2 and value[8] == 2:
                value = client.put_right()
            else:         
                look_walk_right()

        elif value[3] == 3: # もし左がアイテムなら
            if value[0] == 2 and value[6] == 2:
                value = client.put_left()
            else:    
                look_walk_left() 

        elif value[7] == 3: # もし下がアイテムなら
            if value[6] == 2 and value[8] == 2:
                value = client.put_down()
            else: 
                look_walk_down()                
        
        elif value[0] == 3 and value[1] != 2: # 左上にアイテムがあるかつ上がブロックではないなら
            look_walk_up() # 関数walk_walk_upをよびだす        
        elif value[0] == 3 and value[3] != 2: # 左上にアイテムがあるかつ左がブロックではないなら
            look_walk_left() #  左に行く
        elif value[2] == 3 and value[1] != 2:
            look_walk_up() # 上に行く
        elif value[2] == 3 and value[5] != 2: # 右上にアイテムがあるかつ右がブロックではないなら
            look_walk_right() #  右に行く    
        elif value[6] == 3 and value[7] != 2: # 左下にアイテムがあるかつ下がブロックではないなら
            look_walk_down() #　下に行く
        elif value[6] == 3 and value[3] != 2: # 左下にアイテムがあるかつ左がブロックではないなら
            look_walk_left() #  左に行く        
        elif value[8] == 3 and value[7] != 2: # 上にアイテムがあるかつ上がブロックではないなら
            look_walk_down() #　下に行く
        elif value[8] == 3 and value[5] != 2: # 左上にアイテムがあるかつ左がブロックではないなら
            look_walk_right() #  右に行く       
                                       
        else: # 上も下も右もひだりもアイテムではないなら

            rand = random.randint(0,4) # 0から4までの乱数を作る
            if rand == 0: # randが0なら（5回に1回くらいサーチをする）
                rand2 = random.randint(0,3) # rand2を作り
                if rand2 == 0: # rand2が0なら
                    value = client.search_up() # 上９マスを調べる
                    for i in range(9):  # 9回繰り返す(iは0から8まで1ずつ増える)
                        if value[i] == 3: # もしi番目がアイテムなら
                            muki = "up" # 向きをupに変える
                    value = client.get_ready()
                elif rand2 == 1: # rand2が1なら
                    value = client.search_down() # 下９マスを調べる
                    for i in range(9):  # 9回繰り返す(iは0から8まで1ずつ増える)
                        if value[i] == 3: # もしi番目がアイテムなら
                            muki = "down" # 向きをdownに変える
                    value = client.get_ready()   
                elif rand2 == 2: # rand2が2なら
                    value = client.search_right() # 下９マスを調べる
                    for i in range(9):  # 9回繰り返す(iは0から8まで1ずつ増える)
                        if value[i] == 3: # もしi番目がアイテムなら
                            muki = "right" # 向きをrightに変える
                    value = client.get_ready()
                elif rand2 == 3: # rand2が3なら
                    value = client.search_left() # 下９マスを調べる
                    for i in range(9):  # 9回繰り返す(iは0から8まで1ずつ増える)
                        if value[i] == 3: # もしi番目がアイテムなら
                            muki = "left" # 向きをdownに変える
                    value = client.get_ready()             

            rand = random.randint(0,14) # 0から14までの乱数を作る
            if rand == 0: # randが0なら（15回に1回くらいランダムに向きを変える）
                rand = random.randint(0,3)
                if rand == 0: #　もしrandが0ならmukiをupに変える
                    muki = "up"
                elif rand == 1: #　もしrandが0ならmukiをupに変える
                    muki = "down"
                elif rand == 2: 
                    muki = "left"
                elif rand == 3:
                    muki = "right"          
            

            if muki == "down": # もしmukiがdownなら
                if value[7] != 2: # もし自分の下がブロックではないなら またはアイテムなら
                    look_walk_down() # 下に行く   
                elif value[3] != 2: # もし自分の下がブロックで左がブロックではないなら
                    look_walk_left()
                    muki = "left"
                elif value[5] != 2: # もし左と下がブロックで右がブロックでないなら右に行く
                    look_walk_right() # 右に行く  
                    muki = "right" 
                else: # もし右と左と下がブロックなら上にいく
                    look_walk_up() # 上に行く
                    muki = "up"  

            elif muki == "up": # もしmukiがupなら
                if value[1] != 2: # もし自分の上がブロックではないなら    
                    look_walk_up() # 上に行く     
                elif value[5] != 2: # もし上がブロックで右がブロックでないなら     
                    look_walk_right() # 右に行く    
                    muki = "right"
                elif value[3] != 2 : # もし上と右がブロックで左がブロックではないなら左に行く
                    look_walk_left()
                    muki = "left"
                else: # もし上も左も右もブロックなら下に行く
                    look_walk_down()
                    muki = "down"

            elif muki == "right": # もしmukiがrightなら
                if value[5] != 2: # もし自分の右がブロックではないなら 
                    look_walk_right() # 右に行く 
                elif value[7] != 2 : # 右がブロックで下がブロックでないなら
                    look_walk_down() # 下に行く
                    muki = "down"
                elif value[1] != 2: # 右と下がブロックで上がブロックでないなら
                    look_walk_up()
                    muki = "up"
                else: # 右も上も下もブロックなら
                    look_walk_left()
                    muki = "left"

            elif muki == "left": # もしmukiがleftなら
                if value[3] != 2: # もし自分の左がブロックではないなら 
                    look_walk_left() # 左に行く   
                elif value[1] != 2: # 左がブロックで上がブロックでないなら
                    look_walk_up() # 上に行く 
                    muki = "up"
                elif value[7] != 2: #左も上もブロックで下がブロックでないなら
                    look_walk_down() # 下に行く 
                    muki = "down"
                else: # 左も上も下もブロックなら
                    look_walk_right() # 右に行く
                    muki = "right"
"""
python sample.py のようにこのファイルを直接実行すると，
__name__ は "__main__" となる．これを利用して main() を実行する．
"""
if __name__ == "__main__":
    main()