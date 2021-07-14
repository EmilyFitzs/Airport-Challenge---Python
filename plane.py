class Plane:
    def __init__(self, flying=True) -> object:
        self.flying = flying

    def take_off(self):
        if self.flying:
            raise Exception('Plane already flying!')

    def land(self):
        if not self.flying:
            raise Exception('Plane is in the air!')