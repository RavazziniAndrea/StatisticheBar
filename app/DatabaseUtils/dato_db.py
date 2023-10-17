class DatoDB:

    def __init__(self, qta, tipo, data, ora):
        self.qta=qta
        self.tipo=tipo
        self.data=data
        self.ora=ora


    def get_qta(self):
        return self.qta
    
    def set_qta(self, qta):
        self.qta=qta
        
    def get_tipo(self):
        return self.tipo
    
    def set_tipo(self, tipo):
        self.tipo=tipo
        
    def get_data(self):
        return self.data
    
    def set_data(self, data):
        self.data=data
        
    def get_ora(self):
        return self.ora
    
    def set_ora(self, ora):
        self.ora=ora
        