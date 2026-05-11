import unittest
from analytics.analyser import TopStudentsAnalyser

class TestAnalyser(unittest.TestCase):
    def setUp(self):
        # Создаем тестовые данные (мини-датасет)
        self.sample_data = [
            {'student_id': 'S1', 'final_exam_score': 50.0},
            {'student_id': 'S2', 'final_exam_score': 95.5},
            {'student_id': 'S3', 'final_exam_score': 88.0},
            {'student_id': 'S4', 'final_exam_score': 40.0}
        ]
        self.analyser = TopStudentsAnalyser(self.sample_data)

    # Тест 1: Проверка, что результат не пустой
    def test_result_is_not_empty(self):
        res = self.analyser.analyse()
        self.assertTrue(len(res) > 0, "Результат не должен быть пустым")

    # Тест 2: Проверка логики ТОП-1 (сортировка)
    def test_top_student_logic(self):
        res = self.analyser.analyse()
        # Самый высокий балл 95.5 у студента S2
        self.assertEqual(res[0]['student_id'], 'S2', "Первым должен быть студент с самым высоким баллом")

    # Тест 3: Проверка лимита (не больше 10)
    def test_limit_top_n(self):
        # Создадим список из 15 студентов, чтобы проверить срез [:10]
        big_data = [{'student_id': f'S{i}', 'final_exam_score': 90.0} for i in range(15)]
        big_analyser = TopStudentsAnalyser(big_data)
        res = big_analyser.analyse()
        self.assertEqual(len(res), 10, "Анализатор должен возвращать ровно 10 студентов")

    # Тест 4: Проверка структуры данных (наличие ключей)
    def test_result_keys(self):
        res = self.analyser.analyse()
        # Проверяем, что в словаре первого студента есть нужные ключи
        self.assertIn('student_id', res[0])
        self.assertIn('final_exam_score', res[0])

if __name__ == '__main__':
    unittest.main()