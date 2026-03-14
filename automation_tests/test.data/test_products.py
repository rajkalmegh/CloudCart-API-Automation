
def test_create_product(api_client):

    data = {
        "name":"Phone",
        "price":20000
    }

    response = api_client.post("/products", data)

    assert response.status_code == 200


def test_get_products(api_client):

    response = api_client.get("/products")

    assert response.status_code == 200
