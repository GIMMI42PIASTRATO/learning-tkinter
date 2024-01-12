# Calcolatrice
**Problema:** Si vuole implementare una calcolatrice elettronica con i tasti standard di base utilizzando la grafica della libreria Tkinter di Python.
Il layout standard deve comprendere:

- il display, 
- la tastiera con le cifre, 
- i tasti delle operazioni aritmetiche, 
- il tasto di uguale,
- il tasto di cancellazione ultimo comando.

La calcolatrice risponde con un messaggio di errore se il comando non e’ fornito secondo la sintassi corretta.
p.e. 3++5, al secondo + l’applicazione fa nascere un messaggio di errore.
Il risultato grafico dovrà essere all’incirca come quello indicato in figura 1

## I Facoltativo
Implementare le funzionalita’ di memoria mediante i seguenti tasti:

- MEM (richiama il numero contenuto nella memoria)
- STO (Memorizza il risultato dell’ultima operazione o   del numero presente sul display)
- M+ (somma il risultato dell’ultima operazione o del numero presente sul display al contenuto della memoria) Es. se in M è contenuto 5 e sul display è visualizzato 10 se premo M+ nella memoria deve essere memorizzato 15.

Visualizzare sopra il display una M quando è presente un numero in memoria diverso da zero.

## II Facoltativo
Implementare le funzionalita’ di calcolatrice scientifica oltre a quella di base. La calcolatrice scientifica deve calcolare le seguenti operazioni:
- Funzioni trigonometriche 
- elevamento al quadrato
- radice quadrata
- elevamento a esponente n
- radice ennesima
- fattoriale di n (n! = n(n-1)(n-2)...2*1 ; 0! = 1)  es: 4! = 4*3*2= 24
- reciproco di n ( 1/n )

