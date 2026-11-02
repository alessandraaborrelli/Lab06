from database import DB_connect
from database.DB_connect import get_connection
from model.strumento import Strumento
from model.prestito import Prestito

'''
    MODELLO:
    - Rappresenta la struttura dati
    - Si occupa di gestire lo stato dell'applicazione
    - Interagisce con il database
'''

class DepositoStrumenti:
    def __init__(self, nome, responsabile):
        self._nome = nome
        self._responsabile = responsabile

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def responsabile(self):
        return self._responsabile

    @responsabile.setter
    def responsabile(self, responsabile):
        self._responsabile = responsabile

    def get_strumenti(self) -> list[Strumento] | None:
        """
            Funzione che legge tutti gli strumenti nel database
            :return: una lista con tutti gli strumenti presenti oppure None
        """
        # TODO
        connessione = get_connection()
        if connessione is None:
            return

        cursore = connessione.cursor(dictionary=True)
        query = "SELECT * FROM strumento"
        cursore.execute(query)

        lista_strumenti = []
        for riga in cursore:
            s = Strumento(
                codice = riga["codice"],
                tipo = riga["tipo"],
                marca = riga["marca"],
                anno_acquisto =riga["anno_acquisto"],
                valore =riga["valore"],
                disponibile =riga["disponibile"]
            )
            lista_strumenti.append(s)
        cursore.close()
        connessione.close()
        return lista_strumenti


    def cerca_strumenti_per_tipo(self, tipo) -> list[Strumento] | None:
        """
            Funzione che recupera una lista con tutti gli strumenti presenti nel database di un certo tipo
            :param tipo: il tipo dello strumento (es. "Chitarra")
            :return: una lista con tutti gli strumenti del tipo indicato oppure None
        """
        # TODO
        connessione = get_connection()
        if connessione is None:
            return

        cursore = connessione.cursor(dictionary=True)
        query = "SELECT * FROM strumento WHERE tipo = %s"
        cursore.execute(query, (tipo,))

        lista_strumenti_trovati = []
        for riga in cursore:
            s = Strumento(
                codice=riga["codice"],
                tipo=riga["tipo"],
                marca=riga["marca"],
                anno_acquisto=riga["anno_acquisto"],
                valore=riga["valore"],
                disponibile=riga["disponibile"]
            )
            lista_strumenti_trovati.append(s)
        cursore.close()
        connessione.close()
        return lista_strumenti_trovati
