from classes.immobile import Immobile


class Menu:

    __immobili = []

    def __init__(self) -> None:

        for i in range(3):
            print(f"Inserisci i valori per l'immmobile numero {i + 1}")
            codice = int(input(f"Inserisci il codice dell'immobile {i + 1}: "))
            estensione = float(
                input(
                    f"Inserisci l'estensione in metri quadri dell'immobile numero {i + 1}: "
                )
            )
            costo_m2 = float(
                input(
                    f"Inserisci il costo per metro quadro per l'immobile numero {i + 1}: "
                )
            )
            percetuale_tasse = int(
                input(
                    f"Inserisci la percetuale di tasse per l'immobile numero {i + 1}: "
                )
            )

            Menu.__immobili.append(
                Immobile(codice, estensione, costo_m2, percetuale_tasse)
            )

    @staticmethod
    def __stampa_menu():
        print(
            "1. Stampa dati dell'immobile dato il codice\n2. Stampa i dati degli immobili il cui valore è compreso in un range\n3. Stampa dati dell'immobile con maggiore estensione\n4. Stampa tassa media\n5. Stampa costo totale comprese tasse e l'estensione\n6. Esci"
        )

    @staticmethod
    def segli_opzione():
        Menu.__stampa_menu()
        opzione = int(input("Inserisci il numero dell'opzione che vuoi eseguire"))
        while opzione < 1 or opzione > 6:
            opzione = int(input("Inserisci un'opzione valida"))

        exit = False
        while not exit:
            if opzione == 1:
                Menu.__stampa_immobile_per_id()
            elif opzione == 2:
                Menu.__stampa_immobili_per_range_valore()
            elif opzione == 3:
                Menu.__stampa_immobile_maggiore_estensione()
            elif opzione == 4:
                Menu.__stampa_tassa_media()
            elif opzione == 5:
                Menu.__stampa_informazioni_immobile()
            else:
                exit = True
                print("👋👋👋")

    @staticmethod
    def __stampa_immobile_per_id():
        id = input("Inserisci l'id dell'immobile")
        for immobile in Menu.__immobili:
            if immobile.get_codice() == id:
                print("---------------------------")
                print(immobile)
                print("---------------------------")
                return

        print("Nessun immobile è stato trovato con questo codice")

    @staticmethod
    def __stampa_immobili_per_range_valore():
        prezzo_inizio = input("Inserisci un valore d'inizio")
        prezzo_fine = input("Inserisci un valore di fine")
        immobile_trovato = False
        for immobile in Menu.__immobili:
            if (
                immobile.calcola_valore() >= prezzo_inizio
                and immobile.calcola_valore() <= prezzo_fine
            ):
                print("---------------------------")
                print(immobile)
                print("---------------------------")

                immobile_trovato = True

        if not immobile_trovato:
            print(
                f"Nessun immobile è stato trovato nel range {prezzo_inizio} - {prezzo_fine}"
            )

    @staticmethod
    def __stampa_immobile_maggiore_estensione():
        immobile_maggiore_estensione = None
        max_estensione = None
        for immobile in Menu.__immobili:
            if max_estensione == None:
                immobile_maggiore_estensione = immobile
                max_estensione = immobile.get_estensione()
            else:
                if immobile.get_estensione() > max_estensione:
                    immobile_maggiore_estensione = immobile
                    max_estensione = immobile.get_estensione()

        print(immobile_maggiore_estensione)

    @staticmethod
    def __stampa_tassa_media():
        n_immobili = len(Menu.__immobili)
        tassa_media = (
            sum([immobile.get_percentuale_tasse() for immobile in Menu.__immobili])
            / n_immobili
        )

        print(tassa_media)

    @staticmethod
    def __stampa_informazioni_immobile():
        id = input("Inserisci il codice dell'immobile")
        immobile = None
        immobile_trovato = False

        for _immobile in Menu.__immobili:
            if _immobile.get_codice == id:
                immobile = _immobile
                immobile_trovato = True

        if not immobile_trovato:
            print("Nessun immobile è stato trovato con questo codice")
        else:
            costo_totale = immobile.calcola_valore() + immobile.calcola_tasse()

            print(f"Costo totale (tasse incluse): f{costo_totale}")
            print(f"Estensione: {immobile.get_estensione()}")


Menu()
Menu.segli_opzione()
