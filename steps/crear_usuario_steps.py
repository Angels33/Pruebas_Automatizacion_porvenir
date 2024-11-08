from behave import given, when, then
import requests

@given('que tengo los datos para crear un nuevo usuario')
def step_impl(context):
    context.user_data = {"name": "Juan", "job": "QA"}

@when('realizo una solicitud POST al endpoint "/api/users" con los datos del usuario')
def step_impl(context):
    context.url = "https://reqres.in/api/users"
    context.response = requests.post(context.url, json=context.user_data)

@then('la respuesta debe indicar que el usuario fue creado exitosamente')
def step_impl(context):
    assert context.response.status_code == 201

@then('la respuesta debe contener el ID del usuario creado')
def step_impl(context):
    response_json = context.response.json()
    assert "id" in response_json

