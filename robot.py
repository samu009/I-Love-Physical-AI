class Robot
    def __init__(self, codice: str, modello: str, applicazione: str, peso_massimo_componenti_kg: float, stato: str) -> None
        self.codice = codice
        self.modello = modello
        self.applicazione = applicazione
        self.peso_massimo_componenti_kg = peso_massimo_componenti_kg
        self.stato = stato
        self.componenti = componenti [Componente]
        
        
    def aggiungi_componente(self, componente: Componente) -> None
        if (self.comoponente.codice == codice){
            ValueError
        }else if(self.comoponente.peso_kg > peso_massimo_componenti_kg){
             ValueError
        }componeti.append(componente)
        
    def peso_componenti(self) -> float
        self.somma = 0.0
        for(componenti in componenti[]){
            somma = somma + componenti.peso_kg}
        return somma
    
    def cerca_componente(self, codice :str)
        for(componenti in componenti[]){
            if(componeti.codice == self.codice){
                return componeti
            }
        }
        
    def rimuovi_componente(self, codice :str)
        self.componete_trovato : Componete
        for(componenti in componenti[]){
            if(componeti.codice == self.codice){
                self.componete_trovato=componenti
                componeti.remove(componenti)
                return self.componete_trovato
            }
        }
        
    def componenti_sotto_peso(self, peso_massimo: float)-> list[Componete]
        self.lista_componenti : list[Componete]
        for(componenti in componenti[]){
            if(componeti.peso_kg < self.peso_massimo){
                self.lista_componenti.append(componenti)
            }
        }
        return self.lista_componenti
            
        