"""Regras de negocio relacionadas ao calculo de pedidos."""


def validar_item(item: dict) -> None:
    """Valida preco e quantidade de um item.

    Raises:
        ValueError: se o preco ou a quantidade nao forem positivos.
    """
    if item["preco"] <= 0:
        raise ValueError("O preco deve ser positivo.")

    if item["quantidade"] <= 0:
        raise ValueError("A quantidade deve ser positiva.")


def calcular_total(itens: list[dict]) -> float:
    """Calcula o total do pedido.

    Uma lista vazia resulta em total igual a zero.
    """
    total = 0

    for item in itens:
        validar_item(item)
        total += item["preco"] * item["quantidade"]

    return total


# EXERCICIO:
# Implemente com TDD a funcao descrita abaixo.
#
# def calcular_total_com_desconto(itens, percentual_desconto):
#     """Calcula o total e aplica desconto entre 0 e 30 por cento.
#
#     Regras:
#     - desconto menor que 0 ou maior que 30 deve gerar ValueError;
#     - lista vazia deve resultar em zero;
#     - os testes existentes devem continuar aprovados.
#     """
#     pass
