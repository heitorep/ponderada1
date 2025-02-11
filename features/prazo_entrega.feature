Feature: Monitoramento de pedidos atrasados

  Scenario: Calcular % de pedidos que ultrapassam o prazo
    Given um histórico de pedidos com prazos de entrega variados
    When o sistema calcula a taxa de pedidos que excederam o tempo limite
    Then a porcentagem deve ser exibida e comparada com o limite aceitável