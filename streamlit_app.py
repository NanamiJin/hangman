from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

"""
# 三国志真戦名将ガチャシミュレーター仕様_ver.1.0について

・5.6%の確率で星5武将を獲得する

・36%の確率で星4武将を獲得する

・58.4%の確率で星4武将を獲得する

・5回登用するたびに、星4武将または星5武将を必ず獲得する

・登用すると30回以内に必ず星5武将を獲得できる。星5武将を獲得すると回数のカウントはリセットされ、そこからまた更に30以内に星5武将を獲得できる
　各種登用の確定枠は、別々に統計している

・シリーズ2までの各武将の登用出率が公式サイトに従い、設定されている

・リセットボタンを押すと、今までのガチャデータをリセットする（もう一回登用ボタンを押す、画面に反映される）
　ガチャシミュレーター終了後に獲得した星5武将のcsvデータが./outputに出力される

・メインアプリプログラム`/streamlit_app.py` は以下のように示す。
"""

with st.echo(code_location='below'):
    total_points = st.slider("Number of points in spiral", 1, 8000, 2000)
    num_turns = st.slider("Number of turns in spiral", 1, 100, 9)

    Point = namedtuple('Point', 'x y')
    data = []

    points_per_turn = total_points / num_turns

    for curr_point_num in range(total_points):
        curr_turn, i = divmod(curr_point_num, points_per_turn)
        angle = (curr_turn + 1) * 2 * math.pi * i / points_per_turn
        radius = curr_point_num / total_points
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        data.append(Point(x, y))

    st.altair_chart(alt.Chart(pd.DataFrame(data), height=500, width=500)
        .mark_circle(color='#0068c9', opacity=0.5)
        .encode(x='x:Q', y='y:Q'))
