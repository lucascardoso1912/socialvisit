from ia_prompt import PROMPT_RELATORIO

def gerar_descricao_tecnica(anotacoes_brutas):
    """
    Função placeholder para IA assistiva.
    No MVP, pode ser conectada a uma API de IA.
    """

    texto = anotacoes_brutas.strip()

    if not texto.endswith("."):
        texto += "."

    return (
        "Durante a visita domiciliar, "
        + texto[0].lower()
        + texto[1:]
    )
