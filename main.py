import os, csv, json

class FileManager:
    def __init__(self, file): self.file = file

    def check_file(self):
        if not os.path.exists(self.file):
            print("File missing!"); return False
        return True

    def create_output_folder(self, folder="output"):
        if not os.path.exists(folder): os.makedirs(folder)

class DataLoader:
    def __init__(self, file):
        self.file = file
        self.students = []

    def load(self):
        try:
            with open(self.file, encoding='utf-8') as f:
                for row in csv.DictReader(f):
                    try:
                        row['final_exam_score'] = float(row['final_exam_score'])
                        self.students.append(row)
                    except ValueError: continue
            print(f"Loaded {len(self.students)} students")
        except Exception as e: print(f"Error: {e}")

    def preview(self):
        for s in self.students[:5]: print(f"{s['student_id']} | GPA: {s.get('GPA')}")

class DataAnalyser:
    def __init__(self, students):
        self.students = students
        self.result = []

    def analyse(self):
        # Lambda и Filter (требование Practice 5)
        valid = list(filter(lambda x: x['final_exam_score'] > 0, self.students))
        # Сортировка по Варианту D
        self.result = sorted(valid, key=lambda x: x['final_exam_score'], reverse=True)[:10]

    def print_results(self):
        for i, s in enumerate(self.result, 1):
            print(f"{i}. {s['student_id']}: {s['final_exam_score']}")

class ResultSaver:
    def __init__(self, data, path):
        self.data, self.path = data, path

    def save_json(self):
        try:
            with open(self.path, 'w') as f:
                json.dump(self.data, f, indent=4)
            print("Saved to JSON")
        except Exception as e: print(e)

if __name__ == "__main__":
    CSV_FILE = 'global_university_students_performance_habits_10000.csv'

    fm = FileManager(CSV_FILE)
    if fm.check_file():
        fm.create_output_folder()

        dl = DataLoader(CSV_FILE)
        dl.load()

        analyser = DataAnalyser(dl.students)
        analyser.analyse()

        saver = ResultSaver(analyser.result, 'output/result.json')
        saver.save_json()