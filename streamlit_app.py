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
    one_time_gacha_button = st.button('1回登用')
    five_times_gacha_button = st.button('5回登用')


    st.altair_chart(alt.Chart(pd.DataFrame(data), height=500, width=500)
        .mark_circle(color='#0068c9', opacity=0.5)
        .encode(x='x:Q', y='y:Q'))
