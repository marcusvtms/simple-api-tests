from behave import given, when, then, step
from datetime import datetime
import json
import requests

API_URL = 'https://1e8aa271-e499-4226-8f49-2d7927b42e33.mock.pstmn.io'

@given('the order has an id of "8ccdb422-b259-42f6-8bf4-8829381d7ed4"')
def step_impl(context):
    context.order_id = '8ccdb422-b259-42f6-8bf4-8829381d7ed4'

@step('the HEADER param request content type is "application/json"')
def step_impl(context):
    context.header = {"Content-type" : "application/json"}

@when('the user sends a GET HTTP request to /order enpoint')
def step_impl(context):
    url = API_URL+'/order/'+context.order_id
    response = requests.get(url=url, headers=context.header)
    context.response_body = response.json()
    context.status_code = response.status_code

@then('you should receive a "200" status code')
def step_impl(context):
    assert context.status_code == 200

@step('the external id should not be null')
def step_impl(context):
    assert context.response_body["ExternalId"] != ""

@step('the list of items should not be empty')
def step_impl(context):
    assert len(context.response_body["Items"]) > 0

@step('the order status should be "paid"')
def step_impl(context):
    assert context.response_body["Status"] == "paid"

@step('the total order should be the sum of the list of orders prices')
def step_impl(context):
    total_price = 0
    for item in context.response_body["Items"]:
        total_price += item["Price"]
    assert total_price == context.response_body["TotalOrder"]

@step('the last update time should be greater than or the same time of creation')
def step_impl(context):
    create_at = datetime.strptime(context.response_body["CreateAt"], '%a, %d %b %Y %H:%M:%S %Z')
    last_update = datetime.strptime(context.response_body["LastUpdate"], '%a, %d %b %Y %H:%M:%S %Z')
    assert last_update >= create_at

@step('the wallet should not be empty')
def step_impl(context):
    assert context.response_body["Wallet"] != ""

