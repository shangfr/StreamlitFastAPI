# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 15:11:08 2023

@author: shangfr
"""

import json
import requests
import streamlit as st

st.title("FollowAI's Home")


tab1, tab2, tab3 = st.tabs(["Web", "Apps", "Demo"])

with tab1:
    st.subheader(":orange[Web-Apps]")
    st.markdown("- 🛎 [Home](https://shangfr.site/)")
    st.markdown("- 🛎 [Apps](https://app.shangfr.site/)")
    st.markdown("- 🛎 [Portainer](https://portainer.shangfr.site/)")

with tab2:
    st.subheader(":orange[Streamlit-Apps]")
    st.markdown("- 🛎 [Data-Follower](https://shangfr-data-follower-app-mokm7x.streamlit.app/)")
    st.markdown("- 🛎 [Py-Depgraph](https://shangfr-pydepgraph-app-gh2ivs.streamlit.app/)")
    st.markdown("- 🛎 [TTS](https://shangfr-streamlittts-app-xvews2.streamlit.app/)")


with tab3:
    st.subheader(":orange[Demo]")
    with st.expander("Interact with FastAPI endpoint"):
        API_HOST = 'backend'
        API_PORT = 8500
        backend = f'http://{API_HOST}:{API_PORT}'


        st.caption("计算器")

        option = st.selectbox('请选择计算类型：',
                              ('加', '减', '乘', '除'))
        st.write("")
        st.write("选择数值：")
        x = st.slider("X", 0, 100, 20)
        y = st.slider("Y", 0, 130, 10)
        # converting the inputs into a json format
        inputs = {"operation": option, "x": x, "y": y}
        # when the user clicks on button it will fetch the API
        if st.button('计算'):
            res = requests.post(url=f"{backend}/calculate", data=json.dumps(inputs))
            st.subheader(f"算法API返回值： `{res.json()}`")
