# このコードは、Processingの中にあるPythonモードで実行してください。

# =====================================================================
#     * Project Name     : Self-Avoiding-Walk
#     * Description      : スケッチに自己回避ランダムウォークを描きます。
#     * Author           : Shunta Nakamura
#     * Creation Data    : 04-08-2023
#     * LICENSE is MIT (see https://github.com/NAVYSHUNTA/Self-Avoiding-Walk/blob/main/LICENSE)
#     * Original is here : https://github.com/NAVYSHUNTA/Self-Avoiding-Walk
# =====================================================================

import random


# 初期処理
def setup():
    frameRate(10) # 描画の速度
    size(800, 800) # スケッチのサイズ
    background(0, 0, 0) # 背景色

# 自己回避ランダムウォーククラス
class SelfAvoidingWalk:
    # コンストラクタ(線を引く回数の上限値、1本の線の長さ)
    def __init__(self, times_max_pull_line = 500, unit_length = 20):
        self.times_max_pull_line = times_max_pull_line
        self.x = 0
        self.y = 0

        # 左右上下のどれかにランダム移動するための計算で使うもの
        self.attached_list = [[0, unit_length], [0, -unit_length], [unit_length, 0], [-unit_length, 0]]

        # 重複の有無を確認するために辿った座標を記録する
        self.draw_points_set = set()

        # 連続で重複した回数を数える
        self.stop_cnt = 0

    # 描画処理
    def draw_random_walk(self):
        # 辿った点を記録する
        self.draw_points_set.add((self.x, self.y))

        tmp_x = self.x
        tmp_y = self.y

        while True:
            attached_xy = random.choice(self.attached_list)
            # 既にある線分と重複していないか確認する
            if (self.x + attached_xy[0], self.y + attached_xy[1]) in self.draw_points_set:
                self.stop_cnt += 1
                if self.stop_cnt > 100:
                    break
            else:
                self.stop_cnt = 0
                self.times_max_pull_line -= 1
                self.x += attached_xy[0]
                self.y += attached_xy[1]
                stroke(0, 255, 0) # 線分の色
                strokeWeight(5) # 線分の太さ
                line(tmp_x, tmp_y, self.x, self.y) # 線を引く
                break

if __name__ == "__main__":
    # 自己回避ランダムウォーククラスのインスタンスを生成し、sawに代入する
    saw = SelfAvoidingWalk()

    # 繰り返し処理
    def draw():
        global saw
        translate(400, 400) # 中央に描くために座標を変更する
        saw.draw_random_walk()

        # 描画の中断(中断条件：描けなくなるか、線分の長さがある程度の長さになったか、画面からはみ出たか)
        if saw.stop_cnt > 100 or saw.times_max_pull_line < 0 or max(abs(saw.x), abs(saw.y)) > 450:
            background(0, 0, 0) # スケッチをリセットする
            saw = SelfAvoidingWalk()
