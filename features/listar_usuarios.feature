Feature: Listar usuarios

  Scenario: Obtener lista de usuarios en la página 2
    Given que accedo al servicio de listar usuarios de ReqRes
    When realizo una solicitud GET al endpoint "/api/users?page=2"
    Then la respuesta debe contener una lista de usuarios en la página 2
    And el estado de la respuesta debe ser 200

