import random

def calculate_check_digit(digits: list[int]) -> int:
    """Calcula o dígito verificador de um CPF a partir de uma lista de dígitos."""
    weight = len(digits) + 1
    total = sum(d * (weight - i) for i, d in enumerate(digits))
    rest = (total * 10) % 11
    return 0 if rest > 9 else rest


def generate_cpf(formatted: bool = False) -> str:
    """
    Gera um número de CPF válido aleatório.

    :param formatted: se True, retorna no formato XXX.XXX.XXX-XX
    :return: CPF como string
    """
    # Gera os nove primeiros dígitos
    base = [random.randint(0, 9) for _ in range(9)]

    # Calcula os dois dígitos verificadores
    first = calculate_check_digit(base)
    second = calculate_check_digit(base + [first])

    cpf = base + [first, second]
    cpf_str = ''.join(map(str, cpf))

    if formatted:
        return f"{cpf_str[:3]}.{cpf_str[3:6]}.{cpf_str[6:9]}-{cpf_str[9:]}"
    return cpf_str


if __name__ == "__main__":
    print("CPF gerado:", generate_cpf())
    # Para obter com formatação: generate_cpf(formatted=True)