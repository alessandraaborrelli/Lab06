import flet as ft
from UI.view import View
from model.model import DepositoStrumenti

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view: View, model: DepositoStrumenti):
        self._model = model
        self._view = view

    def get_nome(self):
        return self._model.nome

    def get_responsabile(self):
        return self._model.responsabile

    def set_responsabile(self, responsabile):
        self._model.responsabile = responsabile

    def conferma_responsabile(self, e):
        self._model.responsabile = self._view.input_responsabile.value
        self._view.txt_responsabile.value = f"Responsabile: {self._model.responsabile}"
        self._view.update()

    # Altre Funzioni Event Handler
    # TODO
    # definizione della funzione collegata al bottone "Mostra"
    def mostra_strumenti(self, e):
        strumenti = self._model.get_all_strumenti() # recupera la lista degli strumenti dal modello
        self._view.lista_strumenti.controls.clear() # pulisce la ListView per non accumulare dati vecchi

        # controlla se la lista è vuota
        if not strumenti:
            self._view.lista_strumenti.controls.append(ft.Text("Nessuno strumento presente nel database"))
        else:
            for s in strumenti:
                testo = f"{s.codice} - {s.tipo} {s.marca} ({s.anno_acquisto}) - Valore: {s.valore}€ - Disponibile: {s.disponibile}"
                self._view.lista_strumenti.controls.append(ft.Text(testo))
        # aggiorna la vista
        self._view.update()

    # definizione della funzione collegata al bottone "Cerca"
    def cerca_strumenti(self, e):
        # prende il valore inserito nella casella di testo
        tipo = self._view.input_tipo_strumento.value

        # se l'utente non ha scritto nulla, mostra l'alert
        if not tipo or tipo.strip() == "":
            self._view.show_alert("Inserisci un tipo di strumento da cercare!")
            return

        # cerca nel model
        risultati = self._model.cerca_strumenti_per_tipo(tipo.strip())
        # pulisce la ListView per non accumulare dati vecchi
        self._view.lista_strumenti_ricerca.controls.clear()

        if not risultati:
            self._view.lista_strumenti_ricerca.controls.append(ft.Text(f"Nessuno strumento trovato di tipo '{tipo.strip()}'."))
        else:
            for s in risultati:
                testo = f"{s.codice} - {s.tipo} - {s.marca} ({s.anno_acquisto})"
                self._view.lista_strumenti_ricerca.controls.append(ft.Text(testo))

        # aggiorna la vista
        self._view.update()