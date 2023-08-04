import streamlit as st
import json
import pandas as pd
from datetime import datetime
def local_css(file_name):
    with open(file_name) as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

def centered_table(dataframe):
    # 데이터프레임 복사
    df_centered = dataframe.copy()
    # 특정 열의 스타일 수정
    df_centered.style.set_properties(subset=['Name'], **{'text-align': 'center'})
    
    # Streamlit에 HTML 표시
    st.write(df_centered.to_html(escape=False), unsafe_allow_html=True)

# JSON 데이터 로드
def load_json(file_path):
    with open(file_path, 'r') as file:
        json_data = file.read()
        return json_data

# JSON 데이터 초기화
def initialize_node_data(file_path):
    json_data = load_json(file_path)
    node_data = json.loads(json_data)
    return node_data

# 서버 노드 정보 풀기
def expand_server_nodes(server_nodes):
    nodes = []
    for node in server_nodes.split(','):
        if '-' in node:
            start, end = node.split('-')
            nodes.extend(range(int(start), int(end) + 1))
        else:
            nodes.append(int(node))
    return nodes

def update_node_status_hpc(node_data, hpcnum):
    st.markdown("<h1 style='text-align: center; color: grey;'>HPC"+str(hpcnum)+"</h1>", unsafe_allow_html=True)
    if (hpcnum==8):
        num_nodes = 47
    elif (hpcnum==9):
        num_nodes = 47
    elif (hpcnum==10):
        num_nodes = 95
    else:
        num_nodes = 46
    
    # Create columns for the node grid
    columns_hpc11 = st.columns(10)

    for i in range(num_nodes // 10):
        node_row = columns_hpc11
        for node_number, column in enumerate(node_row):
            node_index = i * 10 + node_number + 1
            node_info = node_data.get(str(node_index), {})
            status = node_info.get("status", 'Available')
            node_color = '#00ff00' if status == 'Available' else '#ff0000'
            node_fontc = '#000000' if status == 'Available' else '#000000'

            # Display node status in the corresponding column
            if status == "Occupied":
                occupying_person = node_info.get('occupiedBy', '')
                occupied_time_diff = (datetime.now()-datetime.strptime(node_info.get('occupiedTime', ''),'%Y-%m-%d %H:%M:%S')).total_seconds()
                occupied_time = f'{int(occupied_time_diff // 3600):02d}:{int((occupied_time_diff % 3600) // 60):02d}'
                column.markdown(
                    f'<div class="node" style="background-color: {node_color}; color: {node_fontc};">{node_index}<br>{occupying_person}<br>{occupied_time}</div>',
                    unsafe_allow_html=True
                )
            elif status == "Available":
                column.markdown(
                    f'<div class="node" style="background-color: {node_color}; color: {node_fontc};">{node_index}<br>Available</div>',
                    unsafe_allow_html=True
                )
            else:
                column.markdown(
                    f'<div class="node" style="background-color: gray; color: #000000;">{node_index}<br>Disabled</div>',
                    unsafe_allow_html=True
                )


    last_row_nodes = (num_nodes % 10)
    node_row = columns_hpc11[:last_row_nodes]

    for node_number, column in enumerate(node_row):
        node_index = (num_nodes // 10) * 10 + node_number + 1
        node_info = node_data.get(str(node_index), {})
        status = node_info.get("status", 'Available')
        node_color = '#00ff00' if status == 'Available' else '#ff0000'
        node_fontc = '#000000' if status == 'Available' else '#000000'

        # Display node status in the corresponding column
        if status == "Occupied":
            occupying_person = node_info.get('occupiedBy', '')
            occupied_time_diff = (datetime.now()-datetime.strptime(node_info.get('occupiedTime', ''),'%Y-%m-%d %H:%M:%S')).total_seconds()
            occupied_time = f'{int(occupied_time_diff // 3600):02d}:{int((occupied_time_diff % 3600) // 60):02d}'
            column.markdown(
                f'<div class="node" style="background-color: {node_color}; color: {node_fontc};">{node_index}<br>{occupying_person}<br>{occupied_time}</div>',
                unsafe_allow_html=True
            )
        elif status == "Available":
            column.markdown(
                f'<div class="node" style="background-color: {node_color}; color: {node_fontc};">{node_index}<br>Available</div>',
                unsafe_allow_html=True
            )
        else:
            column.markdown(
                f'<div class="node" style="background-color: gray; color: #000000;">{node_index}<br>Disabled</div>',
                unsafe_allow_html=True
            )

    # Update node data and save it to JSON file
    with open('hpc'+str(hpcnum)+'_node_data.json', 'w') as file:
        file.write(json.dumps(node_data))
        
def update_node_status_hpc11(node_data):
    st.markdown("<h1 style='text-align: center; color: grey;'>HPC11</h1>", unsafe_allow_html=True)

    # Create columns for the node grid
    columns_hpc11 = st.columns(10)

    for i in range(46 // 10):
        node_row = columns_hpc11
        for node_number, column in enumerate(node_row):
            node_index = i * 10 + node_number + 1
            node_info = node_data.get(str(node_index), {})
            status = node_info.get("status", 'Available')
            node_color = '#00ff00' if status == 'Available' else '#ff0000'
            node_fontc = '#000000' if status == 'Available' else '#000000'

            # Display node status in the corresponding column
            if status == "Occupied":
                occupying_person = node_info.get('occupiedBy', '')
                occupied_time_diff = (datetime.now()-datetime.strptime(node_info.get('occupiedTime', ''),'%Y-%m-%d %H:%M:%S')).total_seconds()
                occupied_time = f'{int(occupied_time_diff // 3600):02d}:{int((occupied_time_diff % 3600) // 60):02d}'
                column.markdown(
                    f'<div class="node" style="background-color: {node_color}; color: {node_fontc};">{node_index}<br>{occupying_person}<br>{occupied_time}</div>',
                    unsafe_allow_html=True
                )
            elif status == "Available":
                column.markdown(
                    f'<div class="node" style="background-color: {node_color}; color: {node_fontc};">{node_index}<br>Available</div>',
                    unsafe_allow_html=True
                )
            else:
                column.markdown(
                    f'<div class="node" style="background-color: gray; color: #000000;">{node_index}<br>Disabled</div>',
                    unsafe_allow_html=True
                )


    last_row_nodes = (46 % 10)
    node_row = columns_hpc11[:last_row_nodes]

    for node_number, column in enumerate(node_row):
        node_index = (46 // 10) * 10 + node_number + 1
        node_info = node_data.get(str(node_index), {})
        status = node_info.get("status", 'Available')
        node_color = '#00ff00' if status == 'Available' else '#ff0000'
        node_fontc = '#000000' if status == 'Available' else '#000000'

        # Display node status in the corresponding column
        if status == "Occupied":
            occupying_person = node_info.get('occupiedBy', '')
            occupied_time_diff = (datetime.now()-datetime.strptime(node_info.get('occupiedTime', ''),'%Y-%m-%d %H:%M:%S')).total_seconds()
            occupied_time = f'{int(occupied_time_diff // 3600):02d}:{int((occupied_time_diff % 3600) // 60):02d}'
            column.markdown(
                f'<div class="node" style="background-color: {node_color}; color: {node_fontc};">{node_index}<br>{occupying_person}<br>{occupied_time}</div>',
                unsafe_allow_html=True
            )
        elif status == "Available":
            column.markdown(
                f'<div class="node" style="background-color: {node_color}; color: {node_fontc};">{node_index}<br>Available</div>',
                unsafe_allow_html=True
            )
        else:
            column.markdown(
                f'<div class="node" style="background-color: gray; color: #000000;">{node_index}<br>Disabled</div>',
                unsafe_allow_html=True
            )

    # Update node data and save it to JSON file
    with open('hpc11_node_data.json', 'w') as file:
        file.write(json.dumps(node_data))


def update_node_status_aimc01(node_data):
    st.markdown("<h1 style='text-align: center; color: grey;'>aimc01</h1>", unsafe_allow_html=True)


    # Create columns for the node grid
    margin = 0
    columns_aimc01 = st.columns(10)
    columns_c01but = st.columns(10)
    table_c = st.container()
    for i in range(10 // 10):
        node_row = columns_aimc01
        for node_number, column in enumerate(node_row):
            node_index = i * 10 + node_number + 1
            node_info = node_data.get(str(node_index), {})
            status = node_info.get("status", 'Available')
            node_color = '#00ff00' if status == 'Available' else '#ff0000'
            node_fontc = '#000000' if status == 'Available' else '#000000'
            cnt = 0
            for t in range(len(node_info["users"])):
                cnt = cnt + int(node_info["users"][t]["occupiedNode"])
            # Display node status in the corresponding column
            if status == "Occupied":
                column.markdown(
                    f'<div class="node" style="background-color: {node_color}; color: {node_fontc};">{node_index}<br>Occupied<br>{cnt}/64</div>',
                    unsafe_allow_html=True
                )
            elif status == "Available":
                column.markdown(
                    f'<div class="node" style="background-color: {node_color}; color: {node_fontc};">{node_index}<br>Available<br>{cnt}/64</div>',
                    unsafe_allow_html=True
                )
            else:
                column.markdown(
                    f'<div class="node" style="background-color: gray; color: #000000;">{node_index}<br>Disabled</div>',
                    unsafe_allow_html=True
                )

    # Update node data and save it to JSON file
    with open('aimc01_node_data_adv.json', 'w') as file:
        file.write(json.dumps(node_data))
    if columns_c01but[0].button('node01'):
        nn = 1
        node_info = node_data.get(str(nn), {})
        ln = len(node_info["users"])
        if (ln!=0):
            namel = []
            corel = []
            percl = []
            timel = []
            elapl = []
            for g in range(ln):
                temps = (datetime.now()-datetime.strptime(node_info["users"][g]["occupiedTime"],'%Y-%m-%d %H:%M:%S')).total_seconds()
                namel.append(node_info["users"][g]["name"])
                corel.append(node_info["users"][g]["occupiedNode"])
                tempc = int(node_info["users"][g]["occupiedNode"])
                percl.append(f"{100*tempc/64:.2f}")
                timel.append(node_info["users"][g]["occupiedTime"])
                elapl.append(f"{int(temps//3600):d}:{int((temps%3600)//60):02d}")
            df = pd.DataFrame({"ID":namel,
                            "numcore":corel,
                            "percent":percl,
                            "input time":timel,
                            "elapsed time":elapl})

            table_c.dataframe(df,use_container_width=True )
        else:
            namel = ["empty"]
            corel = ["empty"]
            percl = ["empty"]
            timel = ["empty"]
            elapl = ["empty"]
            df = pd.DataFrame({"ID":namel,
                            "numcore":corel,
                            "percent":percl,
                            "input time":timel,
                            "elapsed time":elapl})
            table_c.dataframe(df,use_container_width=True )
    if columns_c01but[1].button('node02'): 
        nn = 2
        node_info = node_data.get(str(nn), {})
        ln = len(node_info["users"])
        if (ln!=0):
            namel = []
            corel = []
            percl = []
            timel = []
            elapl = []
            for g in range(ln):
                temps = (datetime.now()-datetime.strptime(node_info["users"][g]["occupiedTime"],'%Y-%m-%d %H:%M:%S')).total_seconds()
                namel.append(node_info["users"][g]["name"])
                corel.append(node_info["users"][g]["occupiedNode"])
                tempc = int(node_info["users"][g]["occupiedNode"])
                percl.append(f"{100*tempc/64:.2f}")
                timel.append(node_info["users"][g]["occupiedTime"])
                elapl.append(f"{int(temps//3600):d}:{int((temps%3600)//60):02d}")
            df = pd.DataFrame({"ID":namel,
                            "numcore":corel,
                            "percent":percl,
                            "input time":timel,
                            "elapsed time":elapl})
            table_c.dataframe(df,use_container_width=True )
        else:
            namel = ["empty"]
            corel = ["empty"]
            percl = ["empty"]
            timel = ["empty"]
            elapl = ["empty"]
            df = pd.DataFrame({"ID":namel,
                            "numcore":corel,
                            "percent":percl,
                            "input time":timel,
                            "elapsed time":elapl})
            table_c.dataframe(df,use_container_width=True )
    if columns_c01but[2].button('node03'): 
        nn = 3
        node_info = node_data.get(str(nn), {})
        ln = len(node_info["users"])
        if (ln!=0):
            namel = []
            corel = []
            percl = []
            timel = []
            elapl = []
            for g in range(ln):
                temps = (datetime.now()-datetime.strptime(node_info["users"][g]["occupiedTime"],'%Y-%m-%d %H:%M:%S')).total_seconds()
                namel.append(node_info["users"][g]["name"])
                corel.append(node_info["users"][g]["occupiedNode"])
                tempc = int(node_info["users"][g]["occupiedNode"])
                percl.append(f"{100*tempc/64:.2f}")
                timel.append(node_info["users"][g]["occupiedTime"])
                elapl.append(f"{int(temps//3600):d}:{int((temps%3600)//60):02d}")
            df = pd.DataFrame({"ID":namel,
                            "numcore":corel,
                            "percent":percl,
                            "input time":timel,
                            "elapsed time":elapl})
            table_c.dataframe(df,use_container_width=True )
        else:
            namel = ["empty"]
            corel = ["empty"]
            percl = ["empty"]
            timel = ["empty"]
            elapl = ["empty"]
            df = pd.DataFrame({"ID":namel,
                            "numcore":corel,
                            "percent":percl,
                            "input time":timel,
                            "elapsed time":elapl})
            table_c.dataframe(df,use_container_width=True )
    if columns_c01but[3].button('node04'): 
        nn = 4
        node_info = node_data.get(str(nn), {})
        ln = len(node_info["users"])
        if (ln!=0):
            namel = []
            corel = []
            percl = []
            timel = []
            elapl = []
            for g in range(ln):
                temps = (datetime.now()-datetime.strptime(node_info["users"][g]["occupiedTime"],'%Y-%m-%d %H:%M:%S')).total_seconds()
                namel.append(node_info["users"][g]["name"])
                corel.append(node_info["users"][g]["occupiedNode"])
                tempc = int(node_info["users"][g]["occupiedNode"])
                percl.append(f"{100*tempc/64:.2f}")
                timel.append(node_info["users"][g]["occupiedTime"])
                elapl.append(f"{int(temps//3600):d}:{int((temps%3600)//60):02d}")
            df = pd.DataFrame({"ID":namel,
                            "numcore":corel,
                            "percent":percl,
                            "input time":timel,
                            "elapsed time":elapl})
            table_c.dataframe(df,use_container_width=True )
        else:
            namel = ["empty"]
            corel = ["empty"]
            percl = ["empty"]
            timel = ["empty"]
            elapl = ["empty"]
            df = pd.DataFrame({"ID":namel,
                            "numcore":corel,
                            "percent":percl,
                            "input time":timel,
                            "elapsed time":elapl})
            table_c.dataframe(df,use_container_width=True )
    if columns_c01but[4].button('node05'): 
        nn = 5
        node_info = node_data.get(str(nn), {})
        ln = len(node_info["users"])
        if (ln!=0):
            namel = []
            corel = []
            percl = []
            timel = []
            elapl = []
            for g in range(ln):
                temps = (datetime.now()-datetime.strptime(node_info["users"][g]["occupiedTime"],'%Y-%m-%d %H:%M:%S')).total_seconds()
                namel.append(node_info["users"][g]["name"])
                corel.append(node_info["users"][g]["occupiedNode"])
                tempc = int(node_info["users"][g]["occupiedNode"])
                percl.append(f"{100*tempc/64:.2f}")
                timel.append(node_info["users"][g]["occupiedTime"])
                elapl.append(f"{int(temps//3600):d}:{int((temps%3600)//60):02d}")
            df = pd.DataFrame({"ID":namel,
                            "numcore":corel,
                            "percent":percl,
                            "input time":timel,
                            "elapsed time":elapl})
            table_c.dataframe(df,use_container_width=True )
        else:
            namel = ["empty"]
            corel = ["empty"]
            percl = ["empty"]
            timel = ["empty"]
            elapl = ["empty"]
            df = pd.DataFrame({"ID":namel,
                            "numcore":corel,
                            "percent":percl,
                            "input time":timel,
                            "elapsed time":elapl})
            table_c.dataframe(df,use_container_width=True )
    if columns_c01but[5].button('node06'): 
        nn = 6
        node_info = node_data.get(str(nn), {})
        ln = len(node_info["users"])
        if (ln!=0):
            namel = []
            corel = []
            percl = []
            timel = []
            elapl = []
            for g in range(ln):
                temps = (datetime.now()-datetime.strptime(node_info["users"][g]["occupiedTime"],'%Y-%m-%d %H:%M:%S')).total_seconds()
                namel.append(node_info["users"][g]["name"])
                corel.append(node_info["users"][g]["occupiedNode"])
                tempc = int(node_info["users"][g]["occupiedNode"])
                percl.append(f"{100*tempc/64:.2f}")
                timel.append(node_info["users"][g]["occupiedTime"])
                elapl.append(f"{int(temps//3600):d}:{int((temps%3600)//60):02d}")
            df = pd.DataFrame({"ID":namel,
                            "numcore":corel,
                            "percent":percl,
                            "input time":timel,
                            "elapsed time":elapl})
            table_c.dataframe(df,use_container_width=True )
        else:
            namel = ["empty"]
            corel = ["empty"]
            percl = ["empty"]
            timel = ["empty"]
            elapl = ["empty"]
            df = pd.DataFrame({"ID":namel,
                            "numcore":corel,
                            "percent":percl,
                            "input time":timel,
                            "elapsed time":elapl})
            table_c.dataframe(df,use_container_width=True )
    if columns_c01but[6].button('node07'): 
        nn = 7
        node_info = node_data.get(str(nn), {})
        ln = len(node_info["users"])
        if (ln!=0):
            namel = []
            corel = []
            percl = []
            timel = []
            elapl = []
            for g in range(ln):
                temps = (datetime.now()-datetime.strptime(node_info["users"][g]["occupiedTime"],'%Y-%m-%d %H:%M:%S')).total_seconds()
                namel.append(node_info["users"][g]["name"])
                corel.append(node_info["users"][g]["occupiedNode"])
                tempc = int(node_info["users"][g]["occupiedNode"])
                percl.append(f"{100*tempc/64:.2f}")
                timel.append(node_info["users"][g]["occupiedTime"])
                elapl.append(f"{int(temps//3600):d}:{int((temps%3600)//60):02d}")
            df = pd.DataFrame({"ID":namel,
                            "numcore":corel,
                            "percent":percl,
                            "input time":timel,
                            "elapsed time":elapl})
            table_c.dataframe(df,use_container_width=True )
        else:
            namel = ["empty"]
            corel = ["empty"]
            percl = ["empty"]
            timel = ["empty"]
            elapl = ["empty"]
            df = pd.DataFrame({"ID":namel,
                            "numcore":corel,
                            "percent":percl,
                            "input time":timel,
                            "elapsed time":elapl})
            table_c.dataframe(df,use_container_width=True )
    if columns_c01but[7].button('node08'): 
        nn = 8
        node_info = node_data.get(str(nn), {})
        ln = len(node_info["users"])
        if (ln!=0):
            namel = []
            corel = []
            percl = []
            timel = []
            elapl = []
            for g in range(ln):
                temps = (datetime.now()-datetime.strptime(node_info["users"][g]["occupiedTime"],'%Y-%m-%d %H:%M:%S')).total_seconds()
                namel.append(node_info["users"][g]["name"])
                corel.append(node_info["users"][g]["occupiedNode"])
                tempc = int(node_info["users"][g]["occupiedNode"])
                percl.append(f"{100*tempc/64:.2f}")
                timel.append(node_info["users"][g]["occupiedTime"])
                elapl.append(f"{int(temps//3600):d}:{int((temps%3600)//60):02d}")
            df = pd.DataFrame({"ID":namel,
                            "numcore":corel,
                            "percent":percl,
                            "input time":timel,
                            "elapsed time":elapl})
            table_c.dataframe(df,use_container_width=True )
        else:
            namel = ["empty"]
            corel = ["empty"]
            percl = ["empty"]
            timel = ["empty"]
            elapl = ["empty"]
            df = pd.DataFrame({"ID":namel,
                            "numcore":corel,
                            "percent":percl,
                            "input time":timel,
                            "elapsed time":elapl})
            table_c.dataframe(df,use_container_width=True )
    if columns_c01but[8].button('node09'): 
        nn = 9
        node_info = node_data.get(str(nn), {})
        ln = len(node_info["users"])
        if (ln!=0):
            namel = []
            corel = []
            percl = []
            timel = []
            elapl = []
            for g in range(ln):
                temps = (datetime.now()-datetime.strptime(node_info["users"][g]["occupiedTime"],'%Y-%m-%d %H:%M:%S')).total_seconds()
                namel.append(node_info["users"][g]["name"])
                corel.append(node_info["users"][g]["occupiedNode"])
                tempc = int(node_info["users"][g]["occupiedNode"])
                percl.append(f"{100*tempc/64:.2f}")
                timel.append(node_info["users"][g]["occupiedTime"])
                elapl.append(f"{int(temps//3600):d}:{int((temps%3600)//60):02d}")
            df = pd.DataFrame({"ID":namel,
                            "numcore":corel,
                            "percent":percl,
                            "input time":timel,
                            "elapsed time":elapl})
            table_c.dataframe(df,use_container_width=True )
        else:
            namel = ["empty"]
            corel = ["empty"]
            percl = ["empty"]
            timel = ["empty"]
            elapl = ["empty"]
            df = pd.DataFrame({"ID":namel,
                            "numcore":corel,
                            "percent":percl,
                            "input time":timel,
                            "elapsed time":elapl})
            table_c.dataframe(df,use_container_width=True )
    if columns_c01but[9].button('node10'): 
        nn = 10
        node_info = node_data.get(str(nn), {})
        ln = len(node_info["users"])
        if (ln!=0):
            namel = []
            corel = []
            percl = []
            timel = []
            elapl = []
            for g in range(ln):
                temps = (datetime.now()-datetime.strptime(node_info["users"][g]["occupiedTime"],'%Y-%m-%d %H:%M:%S')).total_seconds()
                namel.append(node_info["users"][g]["name"])
                corel.append(node_info["users"][g]["occupiedNode"])
                tempc = int(node_info["users"][g]["occupiedNode"])
                percl.append(f"{100*tempc/64:.2f}")
                timel.append(node_info["users"][g]["occupiedTime"])
                elapl.append(f"{int(temps//3600):d}:{int((temps%3600)//60):02d}")
            df = pd.DataFrame({"ID":namel,
                            "numcore":corel,
                            "percent":percl,
                            "input time":timel,
                            "elapsed time":elapl})
            table_c.dataframe(df,use_container_width=True )
        else:
            namel = ["empty"]
            corel = ["empty"]
            percl = ["empty"]
            timel = ["empty"]
            elapl = ["empty"]
            df = pd.DataFrame({"ID":namel,
                            "numcore":corel,
                            "percent":percl,
                            "input time":timel,
                            "elapsed time":elapl})
            table_c.dataframe(df,use_container_width=True )

def update_node_status_aimc02(node_data):
    st.markdown("<h1 style='text-align: center; color: grey;'>aimc02</h1>", unsafe_allow_html=True)


    # Create columns for the node grid
    columns_aimc02 = st.columns(10)
    columns_c02but = st.columns(10)
    table_c2 = st.container()

    for i in range(10 // 10):
        node_row = columns_aimc02
        for node_number, column in enumerate(node_row):
            node_index = i * 10 + node_number + 1
            node_info = node_data.get(str(node_index), {})
            status = node_info.get("status", 'Available')
            node_color = '#00ff00' if status == 'Available' else '#ff0000'
            node_fontc = '#000000' if status == 'Available' else '#000000'
            cnt = 0
            for t in range(len(node_info["users"])):
                cnt = cnt + int(node_info["users"][t]["occupiedNode"])
            # Display node status in the corresponding column
            if status == "Occupied":
                column.markdown(
                    f'<div class="node" style="background-color: {node_color}; color: {node_fontc};">{node_index}<br>Occupied<br>{cnt}/48</div>',
                    unsafe_allow_html=True
                )
            elif status == "Available":
                column.markdown(
                    f'<div class="node" style="background-color: {node_color}; color: {node_fontc};">{node_index}<br>Available<br>{cnt}/48</div>',
                    unsafe_allow_html=True
                )
            else:
                column.markdown(
                    f'<div class="node" style="background-color: gray; color: #000000;">{node_index}<br>Disabled</div>',
                    unsafe_allow_html=True
                )

    # Update node data and save it to JSON file
    with open('aimc02_node_data_adv.json', 'w') as file:
        file.write(json.dumps(node_data))
    if columns_c02but[0].button(key="nana01", label='node01'):
        nn = 1
        node_info = node_data.get(str(nn), {})
        ln = len(node_info["users"])
        if (ln!=0):
            namel = []
            corel = []
            percl = []
            timel = []
            elapl = []
            for g in range(ln):
                temps = (datetime.now()-datetime.strptime(node_info["users"][g]["occupiedTime"],'%Y-%m-%d %H:%M:%S')).total_seconds()
                namel.append(node_info["users"][g]["name"])
                corel.append(node_info["users"][g]["occupiedNode"])
                tempc = int(node_info["users"][g]["occupiedNode"])
                percl.append(f"{100*tempc/48:.2f}")
                timel.append(node_info["users"][g]["occupiedTime"])
                elapl.append(f"{int(temps//3600):d}:{int((temps%3600)//60):02d}")
            df = pd.DataFrame({"ID":namel,
                            "numcore":corel,
                            "percent":percl,
                            "input time":timel,
                            "elapsed time":elapl})
            table_c2.dataframe(df,use_container_width=True )
        else:
            namel = ["empty"]
            corel = ["empty"]
            percl = ["empty"]
            timel = ["empty"]
            elapl = ["empty"]
            df = pd.DataFrame({"ID":namel,
                            "numcore":corel,
                            "percent":percl,
                            "input time":timel,
                            "elapsed time":elapl})
            table_c2.dataframe(df,use_container_width=True )
    if columns_c02but[1].button(key="nana02", label='node02'): 
        nn = 2
        node_info = node_data.get(str(nn), {})
        ln = len(node_info["users"])
        if (ln!=0):
            namel = []
            corel = []
            percl = []
            timel = []
            elapl = []
            for g in range(ln):
                temps = (datetime.now()-datetime.strptime(node_info["users"][g]["occupiedTime"],'%Y-%m-%d %H:%M:%S')).total_seconds()
                namel.append(node_info["users"][g]["name"])
                corel.append(node_info["users"][g]["occupiedNode"])
                tempc = int(node_info["users"][g]["occupiedNode"])
                percl.append(f"{100*tempc/48:.2f}")
                timel.append(node_info["users"][g]["occupiedTime"])
                elapl.append(f"{int(temps//3600):d}:{int((temps%3600)//60):02d}")
            df = pd.DataFrame({"ID":namel,
                            "numcore":corel,
                            "percent":percl,
                            "input time":timel,
                            "elapsed time":elapl})
            table_c2.dataframe(df,use_container_width=True )
        else:
            namel = ["empty"]
            corel = ["empty"]
            percl = ["empty"]
            timel = ["empty"]
            elapl = ["empty"]
            df = pd.DataFrame({"ID":namel,
                            "numcore":corel,
                            "percent":percl,
                            "input time":timel,
                            "elapsed time":elapl})
            table_c2.dataframe(df,use_container_width=True )
    if columns_c02but[2].button(key="nana03", label='node03'): 
        nn = 3
        node_info = node_data.get(str(nn), {})
        ln = len(node_info["users"])
        if (ln!=0):
            namel = []
            corel = []
            percl = []
            timel = []
            elapl = []
            for g in range(ln):
                temps = (datetime.now()-datetime.strptime(node_info["users"][g]["occupiedTime"],'%Y-%m-%d %H:%M:%S')).total_seconds()
                namel.append(node_info["users"][g]["name"])
                corel.append(node_info["users"][g]["occupiedNode"])
                tempc = int(node_info["users"][g]["occupiedNode"])
                percl.append(f"{100*tempc/48:.2f}")
                timel.append(node_info["users"][g]["occupiedTime"])
                elapl.append(f"{int(temps//3600):d}:{int((temps%3600)//60):02d}")
            df = pd.DataFrame({"ID":namel,
                            "numcore":corel,
                            "percent":percl,
                            "input time":timel,
                            "elapsed time":elapl})
            table_c2.dataframe(df,use_container_width=True )
        else:
            namel = ["empty"]
            corel = ["empty"]
            percl = ["empty"]
            timel = ["empty"]
            elapl = ["empty"]
            df = pd.DataFrame({"ID":namel,
                            "numcore":corel,
                            "percent":percl,
                            "input time":timel,
                            "elapsed time":elapl})
            table_c2.dataframe(df,use_container_width=True )
    if columns_c02but[3].button(key="nana04", label='node04'): 
        nn = 4
        node_info = node_data.get(str(nn), {})
        ln = len(node_info["users"])
        if (ln!=0):
            namel = []
            corel = []
            percl = []
            timel = []
            elapl = []
            for g in range(ln):
                temps = (datetime.now()-datetime.strptime(node_info["users"][g]["occupiedTime"],'%Y-%m-%d %H:%M:%S')).total_seconds()
                namel.append(node_info["users"][g]["name"])
                corel.append(node_info["users"][g]["occupiedNode"])
                tempc = int(node_info["users"][g]["occupiedNode"])
                percl.append(f"{100*tempc/48:.2f}")
                timel.append(node_info["users"][g]["occupiedTime"])
                elapl.append(f"{int(temps//3600):d}:{int((temps%3600)//60):02d}")
            df = pd.DataFrame({"ID":namel,
                            "numcore":corel,
                            "percent":percl,
                            "input time":timel,
                            "elapsed time":elapl})
            table_c2.dataframe(df,use_container_width=True )
        else:
            namel = ["empty"]
            corel = ["empty"]
            percl = ["empty"]
            timel = ["empty"]
            elapl = ["empty"]
            df = pd.DataFrame({"ID":namel,
                            "numcore":corel,
                            "percent":percl,
                            "input time":timel,
                            "elapsed time":elapl})
            table_c2.dataframe(df,use_container_width=True )
    if columns_c02but[4].button(key="nana05", label='node05'): 
        nn = 5
        node_info = node_data.get(str(nn), {})
        ln = len(node_info["users"])
        if (ln!=0):
            namel = []
            corel = []
            percl = []
            timel = []
            elapl = []
            for g in range(ln):
                temps = (datetime.now()-datetime.strptime(node_info["users"][g]["occupiedTime"],'%Y-%m-%d %H:%M:%S')).total_seconds()
                namel.append(node_info["users"][g]["name"])
                corel.append(node_info["users"][g]["occupiedNode"])
                tempc = int(node_info["users"][g]["occupiedNode"])
                percl.append(f"{100*tempc/48:.2f}")
                timel.append(node_info["users"][g]["occupiedTime"])
                elapl.append(f"{int(temps//3600):d}:{int((temps%3600)//60):02d}")
            df = pd.DataFrame({"ID":namel,
                            "numcore":corel,
                            "percent":percl,
                            "input time":timel,
                            "elapsed time":elapl})
            table_c2.dataframe(df,use_container_width=True )
        else:
            namel = ["empty"]
            corel = ["empty"]
            percl = ["empty"]
            timel = ["empty"]
            elapl = ["empty"]
            df = pd.DataFrame({"ID":namel,
                            "numcore":corel,
                            "percent":percl,
                            "input time":timel,
                            "elapsed time":elapl})
            table_c2.dataframe(df,use_container_width=True )
    if columns_c02but[5].button(key="nana06", label='node06'): 
        nn = 6
        node_info = node_data.get(str(nn), {})
        ln = len(node_info["users"])
        if (ln!=0):
            namel = []
            corel = []
            percl = []
            timel = []
            elapl = []
            for g in range(ln):
                temps = (datetime.now()-datetime.strptime(node_info["users"][g]["occupiedTime"],'%Y-%m-%d %H:%M:%S')).total_seconds()
                namel.append(node_info["users"][g]["name"])
                corel.append(node_info["users"][g]["occupiedNode"])
                tempc = int(node_info["users"][g]["occupiedNode"])
                percl.append(f"{100*tempc/48:.2f}")
                timel.append(node_info["users"][g]["occupiedTime"])
                elapl.append(f"{int(temps//3600):d}:{int((temps%3600)//60):02d}")
            df = pd.DataFrame({"ID":namel,
                            "numcore":corel,
                            "percent":percl,
                            "input time":timel,
                            "elapsed time":elapl})
            table_c2.dataframe(df,use_container_width=True )
        else:
            namel = ["empty"]
            corel = ["empty"]
            percl = ["empty"]
            timel = ["empty"]
            elapl = ["empty"]
            df = pd.DataFrame({"ID":namel,
                            "numcore":corel,
                            "percent":percl,
                            "input time":timel,
                            "elapsed time":elapl})
            table_c2.dataframe(df,use_container_width=True )
    if columns_c02but[6].button(key="nana07", label='node07'): 
        nn = 7
        node_info = node_data.get(str(nn), {})
        ln = len(node_info["users"])
        if (ln!=0):
            namel = []
            corel = []
            percl = []
            timel = []
            elapl = []
            for g in range(ln):
                temps = (datetime.now()-datetime.strptime(node_info["users"][g]["occupiedTime"],'%Y-%m-%d %H:%M:%S')).total_seconds()
                namel.append(node_info["users"][g]["name"])
                corel.append(node_info["users"][g]["occupiedNode"])
                tempc = int(node_info["users"][g]["occupiedNode"])
                percl.append(f"{100*tempc/48:.2f}")
                timel.append(node_info["users"][g]["occupiedTime"])
                elapl.append(f"{int(temps//3600):d}:{int((temps%3600)//60):02d}")
            df = pd.DataFrame({"ID":namel,
                            "numcore":corel,
                            "percent":percl,
                            "input time":timel,
                            "elapsed time":elapl})
            table_c2.dataframe(df,use_container_width=True )
        else:
            namel = ["empty"]
            corel = ["empty"]
            percl = ["empty"]
            timel = ["empty"]
            elapl = ["empty"]
            df = pd.DataFrame({"ID":namel,
                            "numcore":corel,
                            "percent":percl,
                            "input time":timel,
                            "elapsed time":elapl})
            table_c2.dataframe(df,use_container_width=True )
    if columns_c02but[7].button(key="nana08", label='node08'): 
        nn = 8
        node_info = node_data.get(str(nn), {})
        ln = len(node_info["users"])
        if (ln!=0):
            namel = []
            corel = []
            percl = []
            timel = []
            elapl = []
            for g in range(ln):
                temps = (datetime.now()-datetime.strptime(node_info["users"][g]["occupiedTime"],'%Y-%m-%d %H:%M:%S')).total_seconds()
                namel.append(node_info["users"][g]["name"])
                corel.append(node_info["users"][g]["occupiedNode"])
                tempc = int(node_info["users"][g]["occupiedNode"])
                percl.append(f"{100*tempc/48:.2f}")
                timel.append(node_info["users"][g]["occupiedTime"])
                elapl.append(f"{int(temps//3600):d}:{int((temps%3600)//60):02d}")
            df = pd.DataFrame({"ID":namel,
                            "numcore":corel,
                            "percent":percl,
                            "input time":timel,
                            "elapsed time":elapl})
            table_c2.dataframe(df,use_container_width=True )
        else:
            namel = ["empty"]
            corel = ["empty"]
            percl = ["empty"]
            timel = ["empty"]
            elapl = ["empty"]
            df = pd.DataFrame({"ID":namel,
                            "numcore":corel,
                            "percent":percl,
                            "input time":timel,
                            "elapsed time":elapl})
            table_c2.dataframe(df,use_container_width=True )
    if columns_c02but[8].button(key="nana09", label='node09'): 
        nn = 9
        node_info = node_data.get(str(nn), {})
        ln = len(node_info["users"])
        if (ln!=0):
            namel = []
            corel = []
            percl = []
            timel = []
            elapl = []
            for g in range(ln):
                temps = (datetime.now()-datetime.strptime(node_info["users"][g]["occupiedTime"],'%Y-%m-%d %H:%M:%S')).total_seconds()
                namel.append(node_info["users"][g]["name"])
                corel.append(node_info["users"][g]["occupiedNode"])
                tempc = int(node_info["users"][g]["occupiedNode"])
                percl.append(f"{100*tempc/48:.2f}")
                timel.append(node_info["users"][g]["occupiedTime"])
                elapl.append(f"{int(temps//3600):d}:{int((temps%3600)//60):02d}")
            df = pd.DataFrame({"ID":namel,
                            "numcore":corel,
                            "percent":percl,
                            "input time":timel,
                            "elapsed time":elapl})
            table_c2.dataframe(df,use_container_width=True )
        else:
            namel = ["empty"]
            corel = ["empty"]
            percl = ["empty"]
            timel = ["empty"]
            elapl = ["empty"]
            df = pd.DataFrame({"ID":namel,
                            "numcore":corel,
                            "percent":percl,
                            "input time":timel,
                            "elapsed time":elapl})
            table_c2.dataframe(df,use_container_width=True )
    if columns_c02but[9].button(key="nana10", label='node10'): 
        nn = 10
        node_info = node_data.get(str(nn), {})
        ln = len(node_info["users"])
        if (ln!=0):
            namel = []
            corel = []
            percl = []
            timel = []
            elapl = []
            for g in range(ln):
                temps = (datetime.now()-datetime.strptime(node_info["users"][g]["occupiedTime"],'%Y-%m-%d %H:%M:%S')).total_seconds()
                namel.append(node_info["users"][g]["name"])
                corel.append(node_info["users"][g]["occupiedNode"])
                tempc = int(node_info["users"][g]["occupiedNode"])
                percl.append(f"{100*tempc/48:.2f}")
                timel.append(node_info["users"][g]["occupiedTime"])
                elapl.append(f"{int(temps//3600):d}:{int((temps%3600)//60):02d}")
            df = pd.DataFrame({"ID":namel,
                            "numcore":corel,
                            "percent":percl,
                            "input time":timel,
                            "elapsed time":elapl})
            table_c2.dataframe(df,use_container_width=True )
        else:
            namel = ["empty"]
            corel = ["empty"]
            percl = ["empty"]
            timel = ["empty"]
            elapl = ["empty"]
            df = pd.DataFrame({"ID":namel,
                            "numcore":corel,
                            "percent":percl,
                            "input time":timel,
                            "elapsed time":elapl})
            table_c2.dataframe(df,use_container_width=True )
# 메인 애플리케이션 실행
def main():
    st.set_page_config(layout="centered")  # 페이지를 wide로 설정

    local_css("style.css")
    backgroundColor="#50bcdf"
    st.title('Node Status Update')
    # 폼 입력 처리
    server_selection = st.selectbox('Server name', ['aimc01', 'aimc02', 'hpc8', 'hpc9', 'hpc10','hpc11'])
    server_node_input = st.text_input('Target node')
    target_status = st.selectbox('Target Status', ["alloc","free","enable","disable"])  
    if ((server_selection=="aimc01" or server_selection=="aimc02") and target_status=="alloc"):
        server_core_input = st.text_input('Target core')      
    occupying_person = st.selectbox('User',['helen','yujoo', 'yun', 'jb', 'yisehak', 'dam', 'dhlee','slee'])
    
    # aimc01_disabled = []
    # aimc02_disabled = []
    # hpc8_disabled = [1,4,6,7,8,9,10,12,17,18,19,20,21,22,23,24,29,30,31,33,34,35,36,39,40,43,45,46,47]
    # hpc9_disabled = [1,3,7,9,10,11,12,14,15,16,17,19,20,21,22,23,24,26,27,30,31,33,34,36,38,39,40,41,42,43,44,45,46,47]
    # hpc10_disabled = [1,2,3,4,5,6,7,8,9,10,11,12,14,15,16,17,18,20,22,23,25,26,28,29,31,32,33,34,35,36,37,39,40,45,46,49,51,52,53,54,58,60,61,63,64,69,70,71,74,77,78,81,82,83,86,88,91,92,94]
    # hpc11_disabled = [33, 34, 35, 40, 41]


    # JSON 데이터 초기화
    hpc8_node_data = initialize_node_data("hpc8_node_data.json")
    hpc9_node_data = initialize_node_data("hpc9_node_data.json")
    hpc10_node_data = initialize_node_data("hpc10_node_data.json")
    hpc11_node_data = initialize_node_data("hpc11_node_data.json")
    aimc01_node_data = initialize_node_data("aimc01_node_data_adv.json")
    aimc02_node_data = initialize_node_data("aimc02_node_data_adv.json")
    but_col = st.columns([1,1,8])

    # for node in hpc8_disabled:
    #     node_info = hpc8_node_data.get(str(node), {})
    #     node_info["status"] = 'Disabled'
    #     node_info.pop('occupiedBy', None)  # Remove 'occupiedBy' key from the dictionary
    #     node_info.pop('occupiedTime',None)

    # for node in hpc9_disabled:
    #     node_info = hpc9_node_data.get(str(node), {})
    #     node_info["status"] = 'Disabled'
    #     node_info.pop('occupiedBy', None)  # Remove 'occupiedBy' key from the dictionary
    #     node_info.pop('occupiedTime',None)

    # for node in hpc10_disabled:
    #     node_info = hpc10_node_data.get(str(node), {})
    #     node_info["status"] = 'Disabled'
    #     node_info.pop('occupiedBy', None)  # Remove 'occupiedBy' key from the dictionary
    #     node_info.pop('occupiedTime',None)

    # for node in hpc11_disabled:
    #     node_info = hpc11_node_data.get(str(node), {})
    #     node_info["status"] = 'Disabled'
    #     node_info.pop('occupiedBy', None)  # Remove 'occupiedBy' key from the dictionary
    #     node_info.pop('occupiedTime',None)

    # for node in aimc01_disabled:
    #     node_info = aimc01_node_data.get(str(node), {})
    #     node_info["status"] = 'Disabled'
    #     node_info["users"] = {}

    # for node in aimc02_disabled:
    #     node_info = aimc02_node_data.get(str(node), {})
    #     node_info["status"] = 'Disabled'
    #     node_info["users"] = {}


    if but_col[0].button('update'): 
        try:
            # 서버 노드 정보 풀기
            server_nodes = expand_server_nodes(server_node_input)
            if ((server_selection=="aimc01" or server_selection=="aimc02") and target_status=="alloc"):
                server_cores = expand_server_nodes(server_core_input)
            else:
                server_cores = []
                for g in range(len(server_nodes)):
                    server_cores.append(0)
            if (len(server_nodes)!=len(server_cores)):
                st.error("Invalid request. The number of nodes being used should match the number of input numbers.")
            else:
                validation1 = False
                validation2 = False
                minnode = min(server_nodes)
                maxnode = max(server_nodes)
                if (server_selection=="hpc8" and (maxnode > 47 or minnode < 1) or
                    server_selection=="hpc9" and (maxnode > 47 or minnode < 1) or
                    server_selection=="hpc10" and (maxnode > 95 or minnode < 1) or
                    server_selection=="hpc11" and (maxnode > 46 or minnode < 1) or
                    server_selection=="aimc01" and (maxnode > 10 or minnode < 1) or
                    server_selection=="aimc02" and (maxnode > 10 or minnode < 1)):
                    st.error("Invalid node request. Out of node range.")
                else:
                    if (server_selection=="hpc8"):
                        for node in server_nodes:
                            node_info = hpc8_node_data.get(str(node), {})
                            if (node_info["status"]=='Occupied' or node_info["status"]=="Disabled"):
                                validation1=True
                    elif (server_selection=="hpc9"):
                        for node in server_nodes:
                            node_info = hpc9_node_data.get(str(node), {})
                            if (node_info["status"]=='Occupied' or node_info["status"]=="Disabled"):
                                validation1=True 
                    elif (server_selection=="hpc10"):
                        for node in server_nodes:
                            node_info = hpc10_node_data.get(str(node), {})
                            if (node_info["status"]=='Occupied' or node_info["status"]=="Disabled"):
                                validation1=True 
                    elif (server_selection=="hpc11"):
                        for node in server_nodes:
                            node_info = hpc11_node_data.get(str(node), {})
                            if (node_info["status"]=='Occupied' or node_info["status"]=="Disabled"):
                                validation1=True 
                    elif (server_selection=="aimc01"):
                        for n, node in enumerate(server_nodes):
                            node_info = aimc01_node_data.get(str(node), {})
                            if (node_info["status"]=='Occupied' or node_info["status"]=="Disabled"):
                                validation1=True
                            cnt = server_cores[n]
                            for t in range(len(node_info["users"])):
                                cnt = cnt + int(node_info["users"][t]["occupiedNode"])
                            if (cnt > 64):
                                validation2=True         
                    elif (server_selection=="aimc02"):
                        for n, node in enumerate(server_nodes):
                            node_info = aimc02_node_data.get(str(node), {})
                            if (node_info["status"]=='Occupied' or node_info["status"]=="Disabled"):
                                validation1=True
                            cnt = server_cores[n]
                            for t in range(len(node_info["users"])):
                                cnt = cnt + int(node_info["users"][t]["occupiedNode"])
                            if (cnt > 48):
                                validation2=True   
                    if (target_status == "alloc" and validation1):
                        st.error("Invalid node request. Access to occupied/disabled node.")
                    elif (target_status == "alloc" and validation2):
                        st.error("Invalid node request. Not enough node left")
                    else:
                        if (server_selection=="hpc8"):
                            # Update the node_data dictionary
                            for node in server_nodes:
                                node_info = hpc8_node_data.get(str(node), {})
                                #print(node_info)
                                if (target_status == "free" and node_info["status"]!="Disabled"):
                                    # Change the status to "Available" if the occupying person is "free"
                                    node_info["status"] = 'Available'
                                    node_info.pop('occupiedBy', None)  # Remove 'occupiedBy' key from the dictionary
                                    node_info.pop('occupiedTime',None)
                                elif (target_status == "free" and node_info["status"]=="Disabled"):
                                    # Change the status to "Available" if the occupying person is "free"
                                    continue
                                elif (target_status == "disable"):
                                    node_info["status"] = 'Disabled'
                                    node_info.pop('occupiedBy', None)  # Remove 'occupiedBy' key from the dictionary
                                    node_info.pop('occupiedTime',None)
                                elif (target_status == "enable" and node_info["status"]!="Disabled"):
                                    continue
                                elif (target_status == "enable" and node_info["status"]=="Disabled"):
                                    node_info["status"] = 'Available'
                                    node_info.pop('occupiedBy', None)  # Remove 'occupiedBy' key from the dictionary
                                    node_info.pop('occupiedTime',None)
                                else:
                                    node_info["status"] = 'Occupied'
                                    node_info['occupiedBy'] = occupying_person
                                    node_info['occupiedTime'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

                                # Update the node_data dictionary with the updated node information
                                hpc8_node_data[str(node)] = node_info
                        
                        elif (server_selection=="hpc9"):
                            # Update the node_data dictionary
                            for node in server_nodes:
                                node_info = hpc9_node_data.get(str(node), {})
                                if (target_status== "free" and node_info["status"]!="Disabled"):
                                    # Change the status to "Available" if the occupying person is "free"
                                    node_info["status"] = 'Available'
                                    node_info.pop('occupiedBy', None)  # Remove 'occupiedBy' key from the dictionary
                                    node_info.pop('occupiedTime',None)
                                elif (target_status == "free" and node_info["status"]=="Disabled"):
                                    # Change the status to "Available" if the occupying person is "free"
                                    continue
                                elif (target_status == "disable"):
                                    node_info["status"] = 'Disabled'
                                    node_info.pop('occupiedBy', None)  # Remove 'occupiedBy' key from the dictionary
                                    node_info.pop('occupiedTime',None)
                                elif (target_status == "enable" and node_info["status"]!="Disabled"):
                                    continue
                                elif (target_status == "enable" and node_info["status"]=="Disabled"):
                                    node_info["status"] = 'Available'
                                    node_info.pop('occupiedBy', None)  # Remove 'occupiedBy' key from the dictionary
                                    node_info.pop('occupiedTime',None)
                                else:
                                    node_info["status"] = 'Occupied'
                                    node_info['occupiedBy'] = occupying_person
                                    node_info['occupiedTime'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

                                # Update the node_data dictionary with the updated node information
                                hpc9_node_data[str(node)] = node_info
                        
                        elif (server_selection=="hpc10"):
                            # Update the node_data dictionary
                            for node in server_nodes:
                                node_info = hpc10_node_data.get(str(node), {})
                                if (target_status == "free" and node_info["status"]!="Disabled"):
                                    # Change the status to "Available" if the occupying person is "free"
                                    node_info["status"] = 'Available'
                                    node_info.pop('occupiedBy', None)  # Remove 'occupiedBy' key from the dictionary
                                    node_info.pop('occupiedTime',None)
                                elif (target_status == "free" and node_info["status"]=="Disabled"):
                                    # Change the status to "Available" if the occupying person is "free"
                                    continue
                                elif (target_status == "disable"):
                                    node_info["status"] = 'Disabled'
                                    node_info.pop('occupiedBy', None)  # Remove 'occupiedBy' key from the dictionary
                                    node_info.pop('occupiedTime',None)
                                elif (target_status == "enable" and node_info["status"]!="Disabled"):
                                    continue
                                elif (target_status == "enable" and node_info["status"]=="Disabled"):
                                    node_info["status"] = 'Available'
                                    node_info.pop('occupiedBy', None)  # Remove 'occupiedBy' key from the dictionary
                                    node_info.pop('occupiedTime',None)
                                else:
                                    node_info["status"] = 'Occupied'
                                    node_info['occupiedBy'] = occupying_person
                                    node_info['occupiedTime'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

                                # Update the node_data dictionary with the updated node information
                                hpc10_node_data[str(node)] = node_info
                        
                        elif (server_selection=="hpc11"):
                            # Update the node_data dictionary
                            for node in server_nodes:
                                node_info = hpc11_node_data.get(str(node), {})
                                if (target_status == "free" and node_info["status"]!="Disabled"):
                                    # Change the status to "Available" if the occupying person is "free"
                                    node_info["status"] = 'Available'
                                    node_info.pop('occupiedBy', None)  # Remove 'occupiedBy' key from the dictionary
                                    node_info.pop('occupiedTime',None)
                                elif (target_status == "free" and node_info["status"]=="Disabled"):
                                    # Change the status to "Available" if the occupying person is "free"
                                    continue
                                elif (target_status == "disable"):
                                    node_info["status"] = 'Disabled'
                                    node_info.pop('occupiedBy', None)  # Remove 'occupiedBy' key from the dictionary
                                    node_info.pop('occupiedTime',None)
                                elif (target_status == "enable" and node_info["status"]!="Disabled"):
                                    continue
                                elif (target_status == "enable" and node_info["status"]=="Disabled"):
                                    node_info["status"] = 'Available'
                                    node_info.pop('occupiedBy', None)  # Remove 'occupiedBy' key from the dictionary
                                    node_info.pop('occupiedTime',None)
                                else:
                                    node_info["status"] = 'Occupied'
                                    node_info['occupiedBy'] = occupying_person
                                    node_info['occupiedTime'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

                                # Update the node_data dictionary with the updated node information
                                hpc11_node_data[str(node)] = node_info

                        elif (server_selection=="aimc01"):
                            # Update the node_data dictionary
                            for n, node in enumerate(server_nodes):
                                node_info = aimc01_node_data.get(str(node), {})
                                cnt = server_cores[n]
                                for t in range(len(node_info["users"])):
                                    cnt = cnt + int(node_info["users"][t]["occupiedNode"])
                                if (target_status == "free" and node_info["status"]!="Disabled"):
                                    # Change the status to "Available" if the occupying person is "free"
                                    node_info["status"] = 'Available'
                                    templist = []
                                    for g in range(len(node_info["users"])):
                                        if (node_info["users"][g]["name"] != occupying_person):
                                            templist.append(node_info["users"][g])
                                    node_info["users"] = templist
                                elif (target_status == "free" and node_info["status"]=="Disabled"):
                                    # Change the status to "Available" if the occupying person is "free"
                                    continue
                                elif (target_status == "disable"):
                                    node_info["status"] = 'Disabled'
                                    node_info["users"] = []
                                elif (target_status == "enable" and node_info["status"]!="Disabled"):
                                    continue
                                elif (target_status == "enable" and node_info["status"]=="Disabled"):
                                    node_info["status"] = 'Available'
                                    node_info["users"] = []
                                else:
                                    if (cnt==64):
                                        node_info["status"] = 'Occupied'
                                    else:
                                        node_info["status"] = 'Available'
                                    node_info["users"].append(
                                        {
                                            "name": occupying_person,
                                            "occupiedNode": server_cores[n],
                                            "occupiedTime": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                                        }
                                    )

                                # Update the node_data dictionary with the updated node information
                                aimc01_node_data[str(node)] = node_info

                        elif (server_selection=="aimc02"):
                            # Update the node_data dictionary
                            for n, node in enumerate(server_nodes):
                                node_info = aimc02_node_data.get(str(node), {})
                                cnt = server_cores[n]
                                for t in range(len(node_info["users"])):
                                    cnt = cnt + int(node_info["users"][t]["occupiedNode"])
                                if (target_status == "free" and node_info["status"]!="Disabled"):
                                    # Change the status to "Available" if the occupying person is "free"
                                    node_info["status"] = 'Available'
                                    templist = []
                                    for g in range(len(node_info["users"])):
                                        if (node_info["users"][g]["name"] != occupying_person):
                                            templist.append(node_info["users"][g])
                                    node_info["users"] = templist
                                elif (target_status == "free" and node_info["status"]=="Disabled"):
                                    # Change the status to "Available" if the occupying person is "free"
                                    continue
                                elif (target_status == "disable"):
                                    node_info["status"] = 'Disabled'
                                    node_info["users"] = []
                                elif (target_status == "enable" and node_info["status"]!="Disabled"):
                                    continue
                                elif (target_status == "enable" and node_info["status"]=="Disabled"):
                                    node_info["status"] = 'Available'
                                    node_info["users"] = []
                                else:
                                    if (cnt==48):
                                        node_info["status"] = 'Occupied'
                                    else:
                                        node_info["status"] = 'Available'
                                    node_info["users"].append(
                                        {
                                            "name": occupying_person,
                                            "occupiedNode": server_cores[n],
                                            "occupiedTime": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                                        }
                                    )

                                # Update the node_data dictionary with the updated node information
                                aimc02_node_data[str(node)] = node_info
        except:
            st.error("Invalid node number input.")
    # 노드 상태 정보 업데이트
    
    if but_col[1].button("renew"):
        dummy = 1
    update_node_status_aimc01(aimc01_node_data)
    update_node_status_aimc02(aimc02_node_data)
    update_node_status_hpc(hpc8_node_data, 8)
    update_node_status_hpc(hpc9_node_data, 9)
    update_node_status_hpc(hpc10_node_data, 10)
    update_node_status_hpc(hpc11_node_data, 11)




# 애플리케이션 실행
if __name__ == '__main__':
    main()
