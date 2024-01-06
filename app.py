from modelos.restaurante import Restaurante

restaurante_praca = Restaurante("praça", "gourmet")
restaurante_praca.receber_avaliacao("Monica", 10)
restaurante_praca.receber_avaliacao("João", 8)
restaurante_praca.receber_avaliacao("Paloma", 5)


def main():
    Restaurante.listar_restaurantes()


if __name__ == "__main__":
    main()
