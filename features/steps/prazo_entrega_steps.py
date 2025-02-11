from behave import given, when, then

class Pedidos:
    def __init__(self, historico):
        self.historico = historico

    def calcular_pedidos_atrasados(self):
        atrasados = [p for p in self.historico if p["atrasado"]]
        return (len(atrasados) / len(self.historico)) * 100

@given(u'um histórico de pedidos com prazos de entrega variados')
def step_given_historico_pedidos(context):
    context.pedidos = Pedidos([
        {"id": 1, "atrasado": False},
        {"id": 2, "atrasado": False},
        {"id": 3, "atrasado": False},
        {"id": 4, "atrasado": True},
    ])


@when("calculamos a taxa de pedidos atrasados")
def step_when_calcular_atrasados(context):
    context.resultado = context.pedidos.calcular_pedidos_atrasados()

@when(u'o sistema calcula a taxa de pedidos que excederam o tempo limite')
def step_when_calcula_taxa_atrasos(context):
    # Agora usando o método da classe Pedidos para calcular os atrasos
    context.taxa_atrasos = context.pedidos.calcular_pedidos_atrasados()

@then(u'a porcentagem deve ser exibida e comparada com o limite aceitável')
def step_then_compara_taxa_atrasos(context):
    limite_aceitavel = 30  # Exemplo de limite aceitável (10%)
    assert context.taxa_atrasos <= limite_aceitavel, f"Taxa de atrasos {context.taxa_atrasos}% é maior que o limite aceitável de {limite_aceitavel}%"
