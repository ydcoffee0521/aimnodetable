import json

node_data = {}

for i in range(1, 47):
    node_data[str(i)] = {
        "status": "Available",
        "occupiedBy": "",
        "occupiedTime": ""
    }

json_data = json.dumps(node_data)

# 파일에 JSON 데이터 저장
with open('hpc11_node_data.json', 'w') as file:
    file.write(json_data)

print("JSON 데이터가 파일에 저장되었습니다.")
