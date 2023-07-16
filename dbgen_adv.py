import json

node_data = {}

for i in range(1, 11):
    node_data[str(i)] = {
        "status" : "Available",
        "users": [],
    }

json_data = json.dumps(node_data)

# 파일에 JSON 데이터 저장
with open('aimc02_node_data_adv.json', 'w') as file:
    file.write(json_data)

print("JSON 데이터가 파일에 저장되었습니다.")

'''
users = [
    {
        "name": "John",
        "occupiedNode": "1",
        "occupiedTime": "2023-07-16 10:00:00",
    },
    {
        "name": "Emily",
        "occupiedNode": "3",
        "occupiedTime": "2023-07-16 11:30:00",
    },
    {
        "name": "Michael",
        "occupiedNode": "7",
        "occupiedTime": "2023-07-16 12:45:00",
    }
]
'''
