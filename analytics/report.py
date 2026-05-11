class Report:
    def __init__(self, analyser_node): # АССОЦИАЦИЯ (Report использует Analyser)
        self.analyser = analyser_node

    def print_report(self):
        print(f"\n--- REPORT: {self.analyser} ---")
        results = self.analyser.result if self.analyser.result else self.analyser.analyse()
        for i, s in enumerate(results, 1):
            print(f"{i}. {s['student_id']} | Score: {s['final_exam_score']}")