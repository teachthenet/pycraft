# Lezione 4

#### Obiettivo
Crea un edificio programmaticamente

#### Nuovi Concetti

Le variabili possono fare riferimento ad altre variabili, come si fa in algebra
```python
x = 10
x2 = x + 5
```
*x2* adesso vale 15

```python
mc.setBlocks(x, y, z, x2, y2, z2, block_id)
```

- E' disponibile una nuova funzione che possiamo usare chiamata *setBlocks*.
- La funzione *setBlocks* prende in input le coordinate x/y/z dei due angoli opposti di un edificio. 
- Per esempio, se tu pensassi di guardare casa tua dalla strada, la funzione prenderebbe in input l'angolo anteriore in basso a destra della tua casa E quello posteriore in alto a sinistra.
- La funzione quindi imposta ogni blocco all'interno del cuboide che hai definito usando il *block_id* passato

#### Codice
Apri script.py in un editor di codice. Cancella tutto il contenuto del file, partiremo da zero!

```python
import mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create(address="199.96.85.3", name="mancho")
```
Le prime 2 righe sono simili alla lezione precedente. Assicurati di sostituire "mancho" con il tuo nome!

```python
#Otteniamo la posizione corrente del giocatore cosi' vi possiamo costruire la piramide
pos = mc.player.getPos()
x = pos.x
y = pos.y
z = pos.z
```

Questa posizione corrisponde all'angolo anteriore in basso a destra del nostro edificio - mettiamolo dov'e' posizionato il nostro utente in modo da poterlo trovare facilmente!

```python
x2 = x + 10
y2 = y + 5
z2 = z + 8
```

- Questa posizione corrisponde all'angolo posteriore in alto a sinistra del nostro edificio.
- Nota che la stiamo definendo relativamente alla x/y/z (angolo anteriore in basso a destra) dell'edificio.
- Cioè: il valore di x dell'angolo posteriore in alto a sinistra e' uguale al valore di x dell'angolo anteriore in basso a destra + 10.

```python
block_id = 4
```
Questo e' l'id del blocco di tipo ciottolo. Cambialo, se preferisci, con un ID di blocco diverso scegliendolo [qui](http://minecraft-ids.grahamedgecombe.com/).

```python
mc.setBlocks(x, y, z, x2, y2, z2, block_id)
```
Il risultato di quanto sopra dovrebbe essere un edificio che misura 10 blocchi per 5 blocchi per 8 blocchi.

#### Terminale

Esegui lo script con il comando:
```shell
python script.py
```

# SFIDE

- Modifica lo script per cambiare il blocco usato per costruire l'edificio.
- Rendi l'edificio alto il doppio.
- Aggiungi il codice seguente al fondo del tuo script (non cancellare niente, aggiungilo solo) e deduci cosa fa.
```python
mystery_block_id = 0
mc.setBlocks(x+1, y+1, z+1, x2-1, y2-1, z2-1, mystery_block_id)
```
