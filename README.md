# OCIO 👁️
OCIO è una piccola utility, un promemoria visivo per ricordarti di sbattere le palpebre e prevenire secchezza oculare, in modo visivo.
Una volta c'erano dei simpatici occhi che mettevi sopra lo schermo per indurre a sbattere le palpebre, visto che non si trovano più, per chi ha la necessità di lavorare molte ore al PC come nel mio caso, mi sono fatto questa piccola utility, ricordatevi comunque che almeno ogni 50 minuti va fatta una pausa almeno di 10 minuti.

## ℹ️ Informazioni

L'applicazione è stata creata per OpenSuse, nulla vieta di utilizzare su altri sistemi operativi (vedi Windows, Apple) o altre distribuzioni Linux, serve solo python e le dipendenze sotto elencate.

## Caratteristiche

- Finestra sempre in primo piano
- Blink (apertura/chiusura occhio) automatico e manuale cliccando sull’occhio
- Drag te lo posizioni dove vuoi e lo allarghi o stringi come vuoi
- Snap ai bordi dello schermo
- Blink (apertura/chiusura occhio) rapido regolabile
- Intervallo regolabile

## ⚙️ Installazione

1. **Clona il repository:** e estrai lo zip.
```bash
git clone https://github.com/jambolo1970/OCIO.git
cd OCIO
```
## Installa le dipendenze

2. **Installa le dipendenze di sistema** (Necessario su Linux per il supporto immagini in Tkinter):
   - *Ubuntu/Debian:* `sudo apt install python3-pil.imagetk`
   - *Fedora :* `sudo dnf install python313-Pillow-tk` 
   - *OpenSUSE:* `sudo zypper in python313-Pillow-tk ` 
   
3. **Installa i requisiti Python**:
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
## 🚀 Il lanciatore

Salvando in ```~/.local/share/applications/OCIO.desktop``` comparirà tra le applicazioni e potrà essere avviato con un click.
oppure copialo sulla scrivania e dai i persmessi ```chmod +x OCIO.desktop``` per lanciarlo direttamente dalla tua scrivania.

Ho aggiunto il programma ```crea-lanciatore.sh``` che esegue in automatico la parte sopra installando l'utility direttamente nella directory per poi ritrovarsi l'applicazione nel menù.

### 🫚 Struttura dell'utility
OCIO/

├── OCIO.desktop             # lanciatore da copiare e dare i permessi

├── OCIO.py                  # è lo script principale in python

├── eye_open.png             # immagine occhio aperto

├── eye_closed.png           # immagine occhio chiuso

├── ocio_settings.json       # generato automaticamente sul proprio PC

├── README.md                # istruzioni di installazione e varie

├── LICENSE                  # Licenza d'uso GPL 3 generata da github - l'utility serve per la propria saltue

├── requirements.txt         # le dipendenze python da installare

├── crea-lanciatore.sh       # crea il file OCIO.descktop inserendolo direttamente anche nel menu di sistema

└── setup.py                 # per installazione con pip

## 🤝 Contribuire

I contributi sono benvenuti! Sentitevi liberi di inviare una richiesta o di aprire un problema per suggerire miglioramenti o segnalare bug, sarò ben lieto di modificare e migliorare questo programmino python.
