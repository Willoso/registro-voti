import os
import pytest
from registro.voti import media, voto_valido, esito, voto_massimo, voto_minimo


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


# --- Test per esito(voti) ---
def test_esito_promosso_sopra_sei():
    assert esito([7, 8, 9]) == "Promosso"


def test_esito_promosso_limite_sei():
    assert esito([5, 6, 7]) == "Promosso"


def test_esito_insufficiente():
    assert esito([4, 5, 5]) == "Insufficiente"


def test_esito_lista_vuota():
    with pytest.raises(ValueError):
        esito([])


# --- Test per voto_massimo(voti) ---
def test_voto_massimo_normale():
    assert voto_massimo([5, 9, 7, 6]) == 9


def test_voto_massimo_decimali():
    assert voto_massimo([6.5, 7.25, 7.0]) == 7.25


def test_voto_massimo_singolo():
    assert voto_massimo([4]) == 4


def test_voto_massimo_lista_vuota():
    with pytest.raises(ValueError):
        voto_massimo([])


# --- Test per voto_minimo(voti) ---
def test_voto_minimo_normale():
    assert voto_minimo([5, 9, 7, 6]) == 5


def test_voto_minimo_decimali():
    assert voto_minimo([6.5, 5.75, 7.0]) == 5.75


def test_voto_minimo_singolo():
    assert voto_minimo([8]) == 8


def test_voto_minimo_lista_vuota():
    with pytest.raises(ValueError):
        voto_minimo([])


# --- Test che fallisce solo su Windows ---
def test_percorso_fisso_unix():
    assert os.path.join("registro", "voti.py") == "registro/voti.py"