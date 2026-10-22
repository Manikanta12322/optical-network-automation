import json

with open("optical_data.json", "r") as file:
    data = json.load(file)

print("Optical Network Status Report")
print("-----------------------------")

for node in data["optical_nodes"]:
    name = node["name"]
    status = node["status"]

    print(f"{name}: {status}")

    if status == "DOWN":
        print(f"ALERT: {name} requires investigation!")
