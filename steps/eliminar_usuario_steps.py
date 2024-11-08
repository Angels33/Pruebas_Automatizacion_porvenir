from behave import given, when, then
import requests

@given('que tengo un ID de usuario para eliminar')
def step_impl(context):
    context.user_id = 1  # Definir un ID de usuario que exista
    context.url = f"https://reqres.in/api/users/{context.user_id}"

@when('realizo una solicitud DELETE al endpoint de eliminación de usuario')
def step_impl(context):
    context.response = requests.delete(context.url)

@then('la respuesta debe indicar que el usuario fue eliminado exitosamente')
def step_impl(context):
    assert context.response.status_code == 204

@then('el estado de la respuesta debe ser 204')
def step_impl(context):
    assert context.response.status_code == 204
