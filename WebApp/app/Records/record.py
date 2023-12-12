
class Record:

    def __init__(self, qty, typ, date, time):
        self.qty = qty
        self.typ = typ
        self.date = date
        self.time = str(time).split('.')[0]

    
    def fromMessage(message):
        dati = str(message).split('#')
        if dati.__len__() < 5: 
            return None
        return Record(dati[1],dati[2],dati[3],dati[4])
    

    def toStr(self):
        return f"qty: {self.qty} - typ: {self.typ} - date: {self.date} - time: {self.time}"