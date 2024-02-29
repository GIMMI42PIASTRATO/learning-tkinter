from classes.autocarro import Autocarro

autocarro = Autocarro("3487857", "Tesla", "Cybertruck", 5, 50000, 4)
print(autocarro.get_prezzo())
print(autocarro.get_marca())
print(autocarro.get_max_carico())
print(autocarro.get_modello())
print(autocarro.get_numero_posti())
