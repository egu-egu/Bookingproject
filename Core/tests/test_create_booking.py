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
    assert booking["firstname"] == "Jim"
    assert booking["lastname"] == "Brown"
    assert booking["totalprice"] == 111
    assert booking["depositpaid"] == True
    assert booking["bookingdates"]["checkin"] == "2018-01-01"
    assert booking["bookingdates"]["checkout"] == "2019-01-01"
    assert booking["additionalneeds"] == "Breakfast"
