#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter as tk
from PIL import Image, ImageTk
import threading
import json
import os

START_W = 300
START_H = 180
DEFAULT_INTERVAL = 180   # secondi tra un blink e l'altro
DEFAULT_BLINK = 0.08     # durata chiusura occhio
SETTINGS_FILE = "ocio_settings.json"


class OcioApp:
    def __init__(self):
        # --- variabili ---
        self.interval = DEFAULT_INTERVAL
        self.blink_close_time = DEFAULT_BLINK
        self.running = True
        self.timer = None
        self.eye_open = True  # stato dell'occhio

        self.load_settings()

        # --- finestra ---
        self.root = tk.Tk()
        self.root.title("OCIO")
        self.root.attributes("-topmost", True)
        self.root.geometry(f"{START_W}x{START_H}")
        self.root.resizable(True, True)
        self.root.configure(bg="black")
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

        # trasparenza
        self.root.attributes("-alpha", 0.9)

        # immagini
        self.img_open_orig = Image.open("eye_open.png")
        self.img_closed_orig = Image.open("eye_closed.png")

        self.label = tk.Label(self.root, bg="black")
        self.label.pack(expand=True, fill="both")

        self.update_image(self.eye_open)

        # resize handler
        self.root.bind("<Configure>", self.on_resize)

        # menu tasto destro
        self.menu = tk.Menu(self.root, tearoff=0)
        self.menu.add_command(label="Blink più rapido", command=self.blink_faster)
        self.menu.add_command(label="Blink più lento", command=self.blink_slower)
        self.menu.add_separator()
        self.menu.add_command(label="Centro in alto", command=lambda: self.position_window("center_top"))
        self.menu.add_command(label="Destra", command=lambda: self.position_window("right_center"))

        self.menu.add_separator()
        self.menu.add_command(label="Cambia intervallo", command=self.change_interval)
        self.menu.add_command(label="Esci", command=self.on_close)
        self.label.bind("<Button-3>", self.show_menu)

        # --- posiziona finestra ---
        self.root.update_idletasks()
        self.position_window("center_top")

        # --- avvia timer ---
        self.start_timer()

        self.root.mainloop()

    # ------------------------
    # gestione immagine
    def update_image(self, open_eye=True):
        img = self.img_open_orig if open_eye else self.img_closed_orig
        w = max(50, self.root.winfo_width())
        h = max(30, self.root.winfo_height())
        resized = img.resize((w, h), Image.LANCZOS)
        self.tk_img = ImageTk.PhotoImage(resized)
        self.label.config(image=self.tk_img)

    # ------------------------
    # blink
    def blink(self):
        if not self.running:
            return
        self.eye_open = False
        self.update_image(False)
        self.timer = threading.Timer(self.blink_close_time, self.reset)
        self.timer.start()

    def reset(self):
        self.eye_open = True
        self.update_image(True)
        self.start_timer()

    def start_timer(self):
        if self.running:
            self.timer = threading.Timer(self.interval, self.blink)
            self.timer.start()

    # ------------------------
    # resize
    def on_resize(self, event):
        self.update_image(self.eye_open)

    # ------------------------
    # menu
    def show_menu(self, event):
        self.menu.tk_popup(event.x_root, event.y_root)

    def blink_faster(self):
        self.blink_close_time = max(0.04, self.blink_close_time - 0.02)

    def blink_slower(self):
        self.blink_close_time = min(0.3, self.blink_close_time + 0.02)

    def change_interval(self):
        top = tk.Toplevel(self.root)
        top.title("Intervallo blink")
        top.attributes("-topmost", True)

        tk.Label(top, text="Secondi (30–300 consigliato):").pack(padx=10, pady=5)
        entry = tk.Entry(top)
        entry.insert(0, str(self.interval))
        entry.pack(padx=10, pady=5)

        def save():
            try:
                self.interval = int(entry.get())
                self.save_settings()
                if self.timer:
                    self.timer.cancel()
                self.start_timer()
                top.destroy()
            except ValueError:
                pass

        tk.Button(top, text="OK", command=save).pack(pady=10)

    # ------------------------
    # posizionamento finestra
    def position_window(self, mode="center_top"):
        self.root.update_idletasks()
        sw = self.root.winfo_screenwidth()
        sh = self.root.winfo_screenheight()
        w = self.root.winfo_width()
        h = self.root.winfo_height()

        if mode == "center_top":
            x = (sw - w) // 2
            y = 20
        elif mode == "right_center":
            x = sw - w - 20
            y = (sh - h) // 2
        else:
            return

        self.root.geometry(f"+{x}+{y}")

    # ------------------------
    # chiusura
    def on_close(self):
        self.running = False
        if self.timer:
            self.timer.cancel()
        self.save_settings()
        self.root.destroy()

    # ------------------------
    # salvataggio impostazioni
    def load_settings(self):
        if os.path.exists(SETTINGS_FILE):
            with open(SETTINGS_FILE, "r") as f:
                data = json.load(f)
                self.interval = data.get("interval", DEFAULT_INTERVAL)
                self.blink_close_time = data.get("blink_close_time", DEFAULT_BLINK)

    def save_settings(self):
        with open(SETTINGS_FILE, "w") as f:
            json.dump({
                "interval": self.interval,
                "blink_close_time": self.blink_close_time
            }, f)


if __name__ == "__main__":
    OcioApp()
