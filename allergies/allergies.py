ITEMS = {"cats": 128, "pollen": 64, "chocolate": 32, "tomatoes": 16, "strawberries": 8, "shellfish": 4, "peanuts": 2,
         "eggs": 1}
SCORES = list(ITEMS.values())
NAMES = list(ITEMS.keys())


class Allergies:
    def __init__(self, score):
        if score > 1024:
            score -= 1024
        if score > 512:
            score -= 512
        if score > 256:
            score -= 256
        self.score = score
        self.allergy_list = []
        self.item = ''

    def allergic_to(self, item):
        self.item = item
        for ind, sc in enumerate(SCORES):
            if self.score >= sc:
                self.score -= sc
                self.allergy_list.append(NAMES[ind])
        self.allergy_list.reverse()
        if self.item in self.allergy_list:
            return True
        return False

    @property
    def lst(self):
        self.allergic_to(self)
        return self.allergy_list
