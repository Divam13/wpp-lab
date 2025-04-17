class Converter:
    def __init__(self, length, unit):
        self.length = length
        self.unit = unit.lower()
        self.unit_to_meters = {
            'inches': 0.0254,
            'feet': 0.3048,
            'yards': 0.9144,
            'miles': 1609.34,
            'kilometers': 1000,
            'meters': 1,
            'centimeters': 0.01,
            'millimeters': 0.001
        }

    def convert_to_meters(self):
        return self.length * self.unit_to_meters[self.unit]

    def inches(self):
        return self.convert_to_meters() / 0.0254

    def feet(self):
        return self.convert_to_meters() / 0.3048

    def yards(self):
        return self.convert_to_meters() / 0.9144

    def miles(self):
        return self.convert_to_meters() / 1609.34

    def kilometers(self):
        return self.convert_to_meters() / 1000

    def meters(self):
        return self.convert_to_meters()

    def centimeters(self):
        return self.convert_to_meters() / 0.01

    def millimeters(self):
        return self.convert_to_meters() / 0.001

def main():
    while True:
        try:
            length = float(input("Enter the length: "))
            unit = input("Enter the unit (inches, feet, yards, miles, kilometers, meters, centimeters, millimeters): ").lower()
            if unit not in ['inches', 'feet', 'yards', 'miles', 'kilometers', 'meters', 'centimeters', 'millimeters']:
                raise ValueError("Invalid unit entered. Please enter a valid unit.")
            break
        except ValueError as e:
            print(e)

    converter = Converter(length, unit)

    print(f"{length} {unit} in inches: {converter.inches()}")
    print(f"{length} {unit} in feet: {converter.feet()}")
    print(f"{length} {unit} in yards: {converter.yards()}")
    print(f"{length} {unit} in miles: {converter.miles()}")
    print(f"{length} {unit} in kilometers: {converter.kilometers()}")
    print(f"{length} {unit} in meters: {converter.meters()}")
    print(f"{length} {unit} in centimeters: {converter.centimeters()}")
    print(f"{length} {unit} in millimeters: {converter.millimeters()}")

if __name__ == "__main__":
    main()
