from behave import given, when, then

class Pedido:
    def __init__(self):
        self.entregador_aceitou = None

    def aceitar_pedido(self, entregador):
        if self.entregador_aceitou is None:
            self.entregador_aceitou = entregador
            return True
        return False  # Retorna False se outro entregador tentar aceitar

pedido = Pedido()

@given(u'que o restaurante "Sabor Caseiro" enviou um pedido')
def step_given_pedido_enviado(context):
    context.pedido = Pedido()  # Criamos um novo pedido no contexto

@when(u'o entregador "João" aceita a entrega')
def step_when_entregador_joao_aceita(context):
    context.resultado_joao = context.pedido.aceitar_pedido("João")

@when(u'o entregador "Carlos" tenta aceitar o mesmo pedido')
def step_when_entregador_carlos_tenta_aceitar(context):
    context.resultado_carlos = context.pedido.aceitar_pedido("Carlos")

@then(u'o sistema deve impedir a duplicidade e manter apenas um entregador designado')
def step_then_impedir_duplicidade(context):
    assert context.resultado_joao is True, "Erro: João deveria conseguir aceitar!"
    assert context.resultado_carlos is False, "Erro: Carlos conseguiu aceitar, mas não deveria!"
