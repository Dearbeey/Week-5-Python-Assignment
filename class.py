class Phone:
    def __init__(self, brand, model, battery):
        self.brand = brand
        self.model = model
        self.battery = battery

    def call(self, number):
        print(f"{self.brand} {self.model} is calling {number}")

    def charge(self, percentage):
        print(f"{self.brand} {self.model} is charging {percentage}%")

class Smartphone(Phone):
    def __init__(self, brand, model, ram, battery, camera):
        super().__init__(brand, model, battery)
        self.ram = ram
        self.camera = camera

    def install_app(self, app_name):
        print(f"{self.brand} {self.model} is installing {app_name}")

    def call(self, number):
        super().call(number)
        print(f"{self.brand} {self.model} is using VoIP to call {number}")    

#  instances
basic_phone = Phone("Samsung", "Duos", 1000)
smart_phone = Smartphone("Samsung", "S25", 12, 4000, 50)

#  methods
basic_phone.call("0746520413")
basic_phone.charge(50)  
smart_phone.call("0745201413")
smart_phone.install_app("WhatsApp")
smart_phone.charge(80)  
            