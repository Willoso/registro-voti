def media(voti):
    if not voti:
        raise ValueError("La lista dei voti non può essere vuota")
    return round(sum(voti) / len(voti), 2)


def voto_valido(v):
    return 1 <= v <= 10


def esito(voti):
    if media(voti) >= 6:
        return "Promosso"
    return "Insufficiente"


def voto_massimo(voti):
    if not voti:
        raise ValueError("La lista dei voti non può essere vuota")
    return max(voti)


def voto_minimo(voti):
    if not voti:
        raise ValueError("La lista dei voti non può essere vuota")
    return min(voti)