#!/bin/bash

#
#    Nome programma: Crea Lanciatore OCIO
#    Autore: Gianluca Bolognesi
#    Versione: Aprile 2026
#    Descrizione: programma bash per creare un lanciatore in KDE ed installarlo nel menu.
#

# --- DEFINIZIONE COLORI ---
ROSSO='\033[0;31m'
VERDE='\033[0;32m'
NC='\033[0m' # No Color

# 1. Ottiene il percorso assoluto della cartella dove si trova lo script
DIR_ATTUALE="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

# 2. Crea il file .desktop
# Nota: Assicurati che il file python si chiami esattamente OCIO.py (case sensitive)
echo "[Desktop Entry]
Name=OCIO
Comment=Ricordati di sbattere le palpebre
Exec=python3 $DIR_ATTUALE/OCIO.py
Path=$DIR_ATTUALE
Icon=view-visible
Terminal=false
Type=Application
StartupNotify=true
Categories=Utility;" > OCIO.desktop

# 3. Rende il file eseguibile
chmod +x OCIO.desktop

# 4. Lo copia nella cartella delle applicazioni dell'utente
mkdir -p ~/.local/share/applications/
cp OCIO.desktop ~/.local/share/applications/

# --- CONTROLLO FINALE ---
if [ -f ~/.local/share/applications/OCIO.desktop ]; then
    echo -e "${VERDE}[OK]${NC} Installazione completata! OCIO è ora nel tuo menu applicazioni."
else
    echo -e "${ROSSO}[ERRORE]${NC} Qualcosa è andato storto nell'installazione!"
    exit 1
fi
