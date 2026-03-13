import allure
import pytest
import requests


@allure.feature('Test Booking')
@allure.story('Test Created booking')
def test_create_booking(api_client, mocker):
    payload = {
    "firstname" : "Jim",
    "lastname" : "Brown",
    "totalprice" : 111,
    "depositpaid" : True,
    "bookingdates" : {
        "checkin" : "2018-01-01",
        "checkout" : "2019-01-01"
    },
    "additionalneeds" : "Breakfast"
}
    response = api_client.create_booking(payload)
    assert "bookingid" in response
    assert "booking" in response


    booking = response["booking"]
    assert booking["firstname"] == payload["firstname"], 'firstname не совпадает с ожидаемым'
    assert booking["lastname"] == payload["lastname"], 'lastname не совпадает с ожидаемым'
    assert booking["totalprice"] == payload["totalprice"], 'totalprice не совпадает с ожидаемым'
    assert booking["depositpaid"] == payload["depositpaid"], 'depositpaid не совпадает с ожидаемым'
    assert booking["bookingdates"]["checkin"] == payload["bookingdates"]["checkin"], 'checkin не совпадает с ожидаемым'
    assert booking["bookingdates"]["checkout"] == payload["bookingdates"]["checkout"], 'checkout не совпадает с ожидаемым'
    assert booking["additionalneeds"] == payload["additionalneeds"], 'additionalneeds не совпадает с ожидаемым'
