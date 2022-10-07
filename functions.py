from types import NoneType

def novo_print(mensagem: str, *args, **kwargs) -> NoneType:
    print(f"Novo Print: {mensagem}", *args, **kwargs)