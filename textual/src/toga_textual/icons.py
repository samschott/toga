class Icon:
    EXTENSIONS = [".png"]
    SIZES = None

    def __init__(self, interface, path, mask):
        super().__init__()
        self.interface = interface
        self.path = path
