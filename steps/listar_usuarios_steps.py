from behave import given, when, then
import requests

@given('que accedo al servicio de listar usuarios de ReqRes')
def step_impl(context):
    context.url = "https://reqres.in/api/users?page=2"

@when('realizo una solicitud GET al endpoint "/api/users?page=2"')
def step_impl(context):
    context.response = requests.get(context.url)

@then('la respuesta debe contener una lista de usuarios en la página 2')
def step_impl(context):
    response_json = context.response.json()
    assert "data" in response_json
    assert isinstance(response_json["data"], list)  # Verifica que sea una lista

@then('el estado de la respuesta debe ser 200')
def step_impl(context):
    assert context.response.status_code == 200
