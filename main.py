from types import NoneType

def novo_print(mensagem: str, *args, **kwargs) -> NoneType:
    print(f"Novo Print: {mensagem}", *args, **kwargs)



if __name__ == "__main__":
    novo_print("Ola Mundo!")