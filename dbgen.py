import json

node_data = {}
hpc8_disabled = [1,4,6,7,8,9,10,12,17,18,19,20,21,22,23,24,29,30,31,33,34,35,36,39,40,43,45,46,47]
hpc9_disabled = [1,3,7,9,10,11,12,14,15,16,17,19,20,21,22,23,24,26,27,30,31,33,34,36,38,39,40,41,42,43,44,45,46,47]
hpc10_disabled = [1,2,3,4,5,6,7,8,9,10,11,12,14,15,16,17,18,20,22,23,25,26,28,29,31,32,33,34,35,36,37,39,40,45,46,49,51,52,53,54,58,60,61,63,64,69,70,71,74,77,78,81,82,83,86,88,91,92,94]
hpc11_disabled = [33, 34, 35, 40, 41]
for i in range(1, 96):
    if i in (hpc10_disabled):
        node_data[str(i)] = {
            "status": "Available",
            "occupiedBy": "",
            "occupiedTime": ""
        }

    else:
        node_data[str(i)] = {
            "status": "Available",
            "occupiedBy": "",
            "occupiedTime": ""
        }

json_data = json.dumps(node_data)

# 파일에 JSON 데이터 저장
with open('hpc10_node_data.json', 'w') as file:
    file.write(json_data)

print("JSON 데이터가 파일에 저장되었습니다.")
