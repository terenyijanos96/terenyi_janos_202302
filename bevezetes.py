def jatekos_krealas():
    print(f"I/A:")
    jatekos_neve = input("\tJátékos neve: ")
    jatekos_szerepkore = input("\tszerepkör: ")

    match jatekos_szerepkore:
        case "varázsló": eletero = 2
        case "harcos": eletero = 10
        case _: eletero = 8

    print(f"I/B:\n\tÜdvözlünk {jatekos_neve}, {eletero} életed van!")
