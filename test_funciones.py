from funciones import sumar, es_primo

def test_sumar():
    assert sumar(2,3)==5
    assert sumar(2,2)==4
    assert sumar(1,2)==3
    
def test_es_primo():
    assert es_primo(53541265487) is False
    assert es_primo(7) is True
    assert es_primo(20) is False