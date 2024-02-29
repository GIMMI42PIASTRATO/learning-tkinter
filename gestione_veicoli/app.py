from classes.autocarro import Autocarro
from classes.autoveicolo import Autoveicolo

autocarro = Autocarro("3487857", "Tesla", "Cybertruck", 5, 50000, 4)
print(autocarro.get_prezzo())
print(autocarro.get_marca())
print(autocarro.get_max_carico())
print(autocarro.get_modello())
print(autocarro.get_numero_posti())

autoveicolo = Autoveicolo("3433434", "Tesla", "Model S", 5, 15000, 5)
print(autoveicolo.get_prezzo())
print(autoveicolo.get_marca())
print(autoveicolo.get_numero_porte())
print(autoveicolo.get_modello())
print(autoveicolo.get_numero_posti())
