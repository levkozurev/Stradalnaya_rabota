class Object:
    def __init__(self, car_brand, model):
        self.car_brand = car_brand
        self.model = model

mazda= Object('Mazda',CX5)
bently = Object('Bently',Continental_GT)

print(mazda.model)
print(bently.model)
