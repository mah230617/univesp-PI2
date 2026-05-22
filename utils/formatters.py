def formatar_cpf_cnpj(valor):
    if not valor: return ""

    valor = str(valor)

    if len(valor) == 11:
        return (
            f"{valor[:3]}."
            f"{valor[3:6]}."
            f"{valor[6:9]}-"
            f"{valor[9:]}"
        )

    if len(valor) == 14:
        return (
            f"{valor[:2]}."
            f"{valor[2:5]}."
            f"{valor[5:8]}/"
            f"{valor[8:12]}-"
            f"{valor[12:]}"
        )

    return valor


def formatar_telefone(valor):
    if not valor:
        return ""

    valor = str(valor)

    # Celular
    if len(valor) == 11:
        return (f"({valor[:2]}) "f"{valor[2:7]}-"f"{valor[7:]}")

    # Fixo
    if len(valor) == 10:
        return (f"({valor[:2]}) "f"{valor[2:6]}-"f"{valor[6:]}")

    return valor


def formatar_cep(valor):
    if not valor:
        return ""

    valor = str(valor)

    if len(valor) == 8:
        return (f"{valor[:5]}-"f"{valor[5:]}")

    return valor


def formatar_data(valor):
    if not valor: return ""

    return valor.strftime("%d/%m/%Y")