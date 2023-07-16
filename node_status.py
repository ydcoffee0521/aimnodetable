import streamlit as st
import json
from datetime import datetime
def local_css(file_name):
    with open(file_name) as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

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
                    f'<div class="node" style="background-color: gray; color: #000000;">{node_index}<br>Disable</div>',
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
                    f'<div class="node" style="background-color: gray; color: #000000;">{node_index}<br>Disable</div>',
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

    for i in range(10 // 10):
        node_row = columns_aimc01
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

    # Update node data and save it to JSON file
    with open('aimc01_node_data.json', 'w') as file:
        file.write(json.dumps(node_data))

def update_node_status_aimc02(node_data):
    st.markdown("<h1 style='text-align: center; color: grey;'>aimc02</h1>", unsafe_allow_html=True)


    # Create columns for the node grid
    columns_aimc02 = st.columns(10)

    for i in range(10 // 10):
        node_row = columns_aimc02
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

    # Update node data and save it to JSON file
    with open('aimc02_node_data.json', 'w') as file:
        file.write(json.dumps(node_data))
        
# 메인 애플리케이션 실행
def main():
    st.set_page_config(layout="centered")  # 페이지를 wide로 설정
    local_css("style.css")
    backgroundColor="#50bcdf"
    st.title('Node Status Update')
    # 폼 입력 처리
    server_selection = st.selectbox('Server name:', ['aimc01', 'aimc02', 'hpc8', 'hpc9', 'hpc10','hpc11'])
    server_node_input = st.text_input('Target node:')
    occupying_person = st.selectbox('User:',['helen','yujoo', 'yun', 'jb', 'yisehak', 'dam', 'dhlee','slee', 'free'])
    
    aimc01_disabled = []
    aimc02_disabled = []
    hpc8_disabled = []
    hpc9_disabled = []
    hpc10_disabled = [1,2,3,4,5,6,7,8,9,10,11,12,14,15,16,17,18,20,22,23,25,26,28,29,31,32,33,34,35,36,37,39,40,45,46,49,51,52,53,54,58,60,61,63,64,69,70,71,74,77,78,81,82,83,86,88,91,92,94]
    for i in range(1,48):
        hpc9_disabled.append(i)
        if (i==21 or i==38 or i==44):
            continue
        else:
            hpc8_disabled.append(i)
        
    hpc11_disabled = [33, 34, 35, 40, 41]


    # JSON 데이터 초기화
    hpc8_node_data = initialize_node_data("hpc8_node_data.json")
    hpc9_node_data = initialize_node_data("hpc9_node_data.json")
    hpc10_node_data = initialize_node_data("hpc10_node_data.json")
    hpc11_node_data = initialize_node_data("hpc11_node_data.json")
    aimc01_node_data = initialize_node_data("aimc01_node_data.json")
    aimc02_node_data = initialize_node_data("aimc02_node_data.json")
    but_col = st.columns([1,1,4])

    for node in hpc8_disabled:
        node_info = hpc8_node_data.get(str(node), {})
        node_info["status"] = 'Disabled'
        node_info.pop('occupiedBy', None)  # Remove 'occupiedBy' key from the dictionary
        node_info.pop('occupiedTime',None)

    for node in hpc9_disabled:
        node_info = hpc9_node_data.get(str(node), {})
        node_info["status"] = 'Disabled'
        node_info.pop('occupiedBy', None)  # Remove 'occupiedBy' key from the dictionary
        node_info.pop('occupiedTime',None)

    for node in hpc10_disabled:
        node_info = hpc10_node_data.get(str(node), {})
        node_info["status"] = 'Disabled'
        node_info.pop('occupiedBy', None)  # Remove 'occupiedBy' key from the dictionary
        node_info.pop('occupiedTime',None)

    for node in hpc11_disabled:
        node_info = hpc11_node_data.get(str(node), {})
        node_info["status"] = 'Disabled'
        node_info.pop('occupiedBy', None)  # Remove 'occupiedBy' key from the dictionary
        node_info.pop('occupiedTime',None)

    for node in aimc01_disabled:
        node_info = aimc01_node_data.get(str(node), {})
        node_info["status"] = 'Disabled'
        node_info.pop('occupiedBy', None)  # Remove 'occupiedBy' key from the dictionary
        node_info.pop('occupiedTime',None)

    for node in aimc02_disabled:
        node_info = aimc02_node_data.get(str(node), {})
        node_info["status"] = 'Disabled'
        node_info.pop('occupiedBy', None)  # Remove 'occupiedBy' key from the dictionary
        node_info.pop('occupiedTime',None)

    if but_col[0].button('update'): 
        # try:
        # 서버 노드 정보 풀기
        server_nodes = expand_server_nodes(server_node_input)

        validation1 = False
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
                for node in server_nodes:
                    node_info = aimc01_node_data.get(str(node), {})
                    if (node_info["status"]=='Occupied' or node_info["status"]=="Disabled"):
                        validation1=True
            elif (server_selection=="aimc02"):
                for node in server_nodes:
                    node_info = aimc02_node_data.get(str(node), {})
                    if (node_info["status"]=='Occupied' or node_info["status"]=="Disabled"):
                        validation1=True
            if (occupying_person.lower() != "free" and validation1):
                st.error("Invalid node request. Access to occupied/disabled node.")
            else:
                if (server_selection=="hpc8"):
                    # Update the node_data dictionary
                    for node in server_nodes:
                        node_info = hpc8_node_data.get(str(node), {})
                        print(node_info)
                        if (occupying_person.lower() == "free" and node_info["status"]!="Disabled"):
                            # Change the status to "Available" if the occupying person is "free"
                            node_info["status"] = 'Available'
                            node_info.pop('occupiedBy', None)  # Remove 'occupiedBy' key from the dictionary
                            node_info.pop('occupiedTime',None)
                        elif (occupying_person.lower() == "free" and node_info["status"]=="Disabled"):
                            # Change the status to "Available" if the occupying person is "free"
                            continue
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
                        if (occupying_person.lower() == "free" and node_info["status"]!="Disabled"):
                            # Change the status to "Available" if the occupying person is "free"
                            node_info["status"] = 'Available'
                            node_info.pop('occupiedBy', None)  # Remove 'occupiedBy' key from the dictionary
                            node_info.pop('occupiedTime',None)
                        elif (occupying_person.lower() == "free" and node_info["status"]=="Disabled"):
                            # Change the status to "Available" if the occupying person is "free"
                            continue
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
                        if (occupying_person.lower() == "free" and node_info["status"]!="Disabled"):
                            # Change the status to "Available" if the occupying person is "free"
                            node_info["status"] = 'Available'
                            node_info.pop('occupiedBy', None)  # Remove 'occupiedBy' key from the dictionary
                            node_info.pop('occupiedTime',None)
                        elif (occupying_person.lower() == "free" and node_info["status"]=="Disabled"):
                            # Change the status to "Available" if the occupying person is "free"
                            continue
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
                        if (occupying_person.lower() == "free" and node_info["status"]!="Disabled"):
                            # Change the status to "Available" if the occupying person is "free"
                            node_info["status"] = 'Available'
                            node_info.pop('occupiedBy', None)  # Remove 'occupiedBy' key from the dictionary
                            node_info.pop('occupiedTime',None)
                        elif (occupying_person.lower() == "free" and node_info["status"]=="Disabled"):
                            # Change the status to "Available" if the occupying person is "free"
                            continue
                        else:
                            node_info["status"] = 'Occupied'
                            node_info['occupiedBy'] = occupying_person
                            node_info['occupiedTime'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

                        # Update the node_data dictionary with the updated node information
                        hpc11_node_data[str(node)] = node_info

                elif (server_selection=="aimc01"):
                    # Update the node_data dictionary
                    for node in server_nodes:
                        node_info = aimc01_node_data.get(str(node), {})
                        if (occupying_person.lower() == "free" and node_info["status"]!="Disabled"):
                            # Change the status to "Available" if the occupying person is "free"
                            node_info["status"] = 'Available'
                            node_info.pop('occupiedBy', None)  # Remove 'occupiedBy' key from the dictionary
                            node_info.pop('occupiedTime',None)
                        elif (occupying_person.lower() == "free" and node_info["status"]=="Disabled"):
                            # Change the status to "Available" if the occupying person is "free"
                            continue
                        else:
                            node_info["status"] = 'Occupied'
                            node_info['occupiedBy'] = occupying_person
                            node_info['occupiedTime'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

                        # Update the node_data dictionary with the updated node information
                        aimc01_node_data[str(node)] = node_info

                elif (server_selection=="aimc02"):
                    # Update the node_data dictionary
                    for node in server_nodes:
                        node_info = aimc02_node_data.get(str(node), {})
                        if (occupying_person.lower() == "free" and node_info["status"]!="Disabled"):
                            # Change the status to "Available" if the occupying person is "free"
                            node_info["status"] = 'Available'
                            node_info.pop('occupiedBy', None)  # Remove 'occupiedBy' key from the dictionary
                            node_info.pop('occupiedTime',None)
                        elif (occupying_person.lower() == "free" and node_info["status"]=="Disabled"):
                            # Change the status to "Available" if the occupying person is "free"
                            continue
                        else:
                            node_info["status"] = 'Occupied'
                            node_info['occupiedBy'] = occupying_person
                            node_info['occupiedTime'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

                        # Update the node_data dictionary with the updated node information
                        aimc02_node_data[str(node)] = node_info 
        # except:
            # st.error("Invalid node number input.")
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
