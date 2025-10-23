#Виктория Д., 36 когорта, финальный проект
import sender_stand_request
import data 


def test_get_order_by_track():
    create_order_response = sender_stand_request.create_new_order(data.order_body, data.headers)
    get_order_response = sender_stand_request.get_order(create_order_response.json()["track"])
    assert get_order_response.status_code == 200, f"Ожидался код 200, но получен {get_order_response.status_code}"


