import json
from api_server import app


def test_optical_nodes_data():
    with open("optical_data.json", "r") as file:
        data = json.load(file)

    assert "optical_nodes" in data
    assert len(data["optical_nodes"]) > 0

    for node in data["optical_nodes"]:
        assert "name" in node
        assert "status" in node


def test_optical_nodes_api():
    client = app.test_client()

    response = client.get("/api/optical-nodes")

    assert response.status_code == 200

    data = response.get_json()
    assert "optical_nodes" in data
    assert len(data["optical_nodes"]) == 3
