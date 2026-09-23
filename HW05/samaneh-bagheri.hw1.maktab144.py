from abc import ABC,abstractmethod
class Home_appliances(ABC) :

    def __init__(self,id,name):
        self.id = id
        self.name = name
        self.status = False
    @abstractmethod
    def turn_on(self):
        pass
       
    @abstractmethod
    def turn_off(self):
        pass

class Lamp(Home_appliances):
        def init(self,id,name,wifi,log):
            super().__init__(id,name)
            self.wifi = wifi
            self.log = log
class Wifi():
        def init(self):
            self.connected = False
        def connect(self):
            self.connected=True
        def disconnect(self):
            self.connected= False
           
class Log():
        def init(self):
            self.logs=[]
        def add_log(self,event):
            self.logs.append(event)

Wifi1 = wifi()
lamp1=Lamp(12,'bedroom',True,wifi1,log1)