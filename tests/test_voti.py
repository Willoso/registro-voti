import pytest
from registro.voti import media, voto_valido


# --- Test per media(voti) ---
def test_media_voti_interi():
    assert media([6, 7, 8]) == 7.0


def test_media_arrotondamento():
    assert media([6, 7, 7]) == 6.67


def test_media_singolo_voto():
    assert media([8.5]) == 8.5


def test_media_lista_vuota():
    with pytest.raises(ValueError):
        media([])


# --- Test per voto_valido(v) ---
def test_voto_valido_normale():
    assert voto_valido(7) is True


def test_voto_valido_estremi():
    assert voto_valido(1) is True
    assert voto_valido(10) is True


def test_voto_non_valido_troppo_basso():
    assert voto_valido(0) is False
    assert voto_valido(-2) is False


def test_voto_non_valido_troppo_alto():
    assert voto_valido(11) is False