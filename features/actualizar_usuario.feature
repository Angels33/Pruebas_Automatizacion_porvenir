Feature: Actualizar un usuario existente

  @actualizar_usuario
  Scenario: Actualizar un usuario con datos válidos
    Given que tengo un ID de usuario para actualizar
    When realizo una solicitud PUT al endpoint con los siguientes datos actualizados
      | name   | job             |
      | "Juan" | "Desarrollador" |
    Then la respuesta debe indicar que el usuario fue actualizado exitosamente





