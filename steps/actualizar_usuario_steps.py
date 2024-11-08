from behave import given, when, then
import requests

@given('que tengo un ID de usuario para actualizar')
def step_impl(context):
    context.user_id = 1  # ID de usuario
    context.url = f"https://reqres.in/api/users/{context.user_id}"

@when('realizo una solicitud PUT al endpoint con los siguientes datos actualizados')
def step_impl(context):
    context.updated_data = {"name": "Juan", "job": "Desarrollador"}
    context.response = requests.put(context.url, json=context.updated_data)

@then('la respuesta debe indicar que el usuario fue actualizado exitosamente')
def step_impl(context):
    assert context.response.status_code == 200

