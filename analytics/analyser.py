class DataAnalyser: # БАЗОВЫЙ КЛАСС
    def __init__(self, data):
        self.data = data
        self.result = []

    def analyse(self): # Метод будет переопределен (Полиморфизм)
        pass

    def __str__(self): # Красивый вывод объекта
        return f"{self.__class__.__name__} (Rows: {len(self.data)})"

class TopStudentsAnalyser(DataAnalyser): # НАСЛЕДОВАНИЕ
    def analyse(self): # ПЕРЕОПРЕДЕЛЕНИЕ
        # Вариант D: Топ-10 по экзамену
        self.result = sorted(self.data, key=lambda x: x['final_exam_score'], reverse=True)[:10]
        return self.result