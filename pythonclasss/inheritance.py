class car :
    def fuel(self):
        return "i run on petrol"
    
    class BMW(car):
        def speed(self):
            return "i am fast"
        
        bmw = BMW()
        print(bmw.fuel())
        print(bmw.speed()) 