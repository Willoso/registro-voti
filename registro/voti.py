def media(voti):
    if not voti:
        raise ValueError("La lista dei voti non può essere vuota")
    return round(sum(voti) / len(voti), 2)


def voto_valido(v):
    return 1 <= v <= 10