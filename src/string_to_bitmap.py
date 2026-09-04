from chars_dict import CHARACTER_DICT as characters

class bitmap():
    def __init__(self, input: str):
        self.message = input.upper()
        self.grid = self.string_to_bitmap()

    def __str__(self) -> str:
        rows = ''
        for item in self.grid:
            row = ''
            for char in item:
                if char:
                    row += "o"
                else:
                    row += " "
            rows += row + "\n"
        return rows

    def string_to_bitmap(self) -> list[list[bool]]:
        result = [[] for _ in range(7)]
        for char in self.message:
            char_matrix = characters.get(char)
            for i in range(7):
                result[i].extend(char_matrix[i])
                result[i].append(False)
        return result
