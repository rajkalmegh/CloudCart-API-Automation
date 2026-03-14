
def test_create_order(api_client):

    data = {
        "product_id":"123",
        "quantity":2
    }

    response = api_client.post("/orders", data)

    assert response.status_code == 200
