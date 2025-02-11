Feature: Evitar duplicidade de corrida

  Scenario: Um pedido não pode ser aceito por dois entregadores
    Given que o restaurante "Sabor Caseiro" enviou um pedido
    When o entregador "João" aceita a entrega
    And o entregador "Carlos" tenta aceitar o mesmo pedido
    Then o sistema deve impedir a duplicidade e manter apenas um entregador designado