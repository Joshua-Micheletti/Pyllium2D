class Structure:
    def __init__(self, path):
        self.cells = []
        self.width = 0
        self.height = 0
        self.path = path

        self.parse_structure(self.path)

    def parse_structure(self, path):
        file = open(path)

        line_count = 0

        for line in file:
            elements = line.strip().split('\t')
            self.width = len(elements)

            self.cells.append([])

            for element in elements:
                self.cells[len(self.cells) - 1].append(int(element))

            line_count += 1

        self.height = line_count
        self.cells.reverse()

    def get_tile(self, x, y):
        return(self.cells[x][y])
