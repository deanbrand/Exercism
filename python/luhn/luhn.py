class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num.replace(" ", "")

    def valid(self):
        if len(self.card_num) < 2:
            return False
        for char in self.card_num:
            if not char.isdigit():
                return False

        first_dig = []
        second_dig = []

        for ind, num in enumerate(self.card_num[::-1]):
            if ind % 2 == 0:
                first_dig.append(int(num))
            else:
                second_dig.append(int(num) * 2)
        for ind, num in enumerate(second_dig):
            if num > 9:
                second_dig[ind] -= 9
        if (sum(second_dig) + sum(first_dig)) % 10 == 0:
            return True
        return False
