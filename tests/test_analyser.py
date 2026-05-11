import unittest
from analytics.analyser import TopStudentsAnalyser

class TestAnalyser(unittest.TestCase):
    def setUp(self):
        self.mock_data = [
            {'student_id': 'S1', 'final_exam_score': 50.0},
            {'student_id': 'S2', 'final_exam_score': 90.0}
        ]
        self.analyser = TopStudentsAnalyser(self.mock_data)

    def test_sorting(self):
        res = self.analyser.analyse()
        self.assertEqual(res[0]['student_id'], 'S2') # S2 должен быть первым

if __name__ == '__main__':
    unittest.main()