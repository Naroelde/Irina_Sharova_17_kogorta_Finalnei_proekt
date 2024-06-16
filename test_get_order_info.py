import data
import sender_stand_request

def test_get_order_info_by_track_number():
    # Cоздан заказ и ответ от сервера сохранен в переменную track
    track = sender_stand_request.create_order(data.order_body)
    # В переменной track остался только номер трека
    track = track.json()["track"]
    # Отправлен запрос на получение данных заказа по трек номеру
    order_info = sender_stand_request.get_order_info_by_track(str(track))
    # Проверка, что пришел ответ 200
    assert order_info.status_code == 200
