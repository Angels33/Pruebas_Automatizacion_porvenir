Feature: Eliminar un usuario existente

  Scenario: Eliminar un usuario con un ID válido
    Given que tengo un ID de usuario para eliminar
    When realizo una solicitud DELETE al endpoint de eliminación de usuario
    Then la respuesta debe indicar que el usuario fue eliminado exitosamente
    And el estado de la respuesta debe ser 204
