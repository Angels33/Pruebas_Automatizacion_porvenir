Feature: Crear un usuario nuevo

  @crear_usuario
  Scenario: Crear un usuario con datos válidos
    Given que tengo los datos para crear un nuevo usuario
    When realizo una solicitud POST al endpoint "/api/users" con los datos del usuario
    Then la respuesta debe indicar que el usuario fue creado exitosamente
    And la respuesta debe contener el ID del usuario creado

