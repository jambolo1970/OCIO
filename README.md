# OCIO
OCIO è una piccola utility, un promemoria visivo per ricordarti di sbattere le palpebre e prevenire secchezza oculare, in modo visivo.
una volta c'erano dei simpatici occhi che mettevi sopra lo schermo che indurre a sbattere le palpebre, e visto che non si trovano più, per chi ha la necessità di lavorare molto al PC come nel mio caso, mi sono fatto questa piccola utility.

## Caratteristiche

- Finestra sempre in primo piano
- Blink (apertura/chiusura occhio) automatico e manuale cliccando sull’occhio
- Drag te lo posizioni dove vuoi e lo allarghi o stringi come vuoi
- Snap ai bordi dello schermo
- Blink (apertura/chiusura occhio) rapido regolabile
- Intervallo regolabile

## Installazione

1. Clona il repository:
```bash
git clone https://github.com/jambolo1970/OCIO.git
cd OCIO
```
## Installa le dipendenze

```bash
pip install -r requirements.txt
```

## Avvia l’applicazione 

```bash
python OCIO.py
```
### Oppure installa come pacchetto e avviala con:

```bash
pip install .  # dalla cartella del progetto
ocio           # e parte il programma

```
## Il lanciatore

Salvando in ```~/.local/share/applications/OCIO.desktop``` comparirà tra le applicazioni e potrà essere avviato con un click.
oppure copialo sulla scrivania e dai i persmessi ```chmod +x OCIO.desktop``` per lanciarlo direttamente dalla tua scrivania.

### Struttura dell'utility
OCIO/

├── OCIO.desktop             # lanciatore da copiare e dare i permessi

├── OCIO.py                  # il tuo script principale

├── eye_open.png             # immagine occhio aperto

├── eye_closed.png           # immagine occhio chiuso

├── ocio_settings.json       # generata automaticamente sul proprio PC

├── README.md                # istruzioni di installazione e varie

├── LICENSE                  # Licenza d'uso GPL 3 generata da github

├── requirements.txt         # le dipendenze python

└── setup.py                 # per installazione con pip
