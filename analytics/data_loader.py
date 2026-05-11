import csv

class DataLoader:
    def __init__(self, file_path):
        self.file_path = file_path
        self.students = []

    def load(self):
        with open(self.file_path, encoding='utf-8-sig') as f:
            reader = csv.DictReader(f)
            for row in reader:
                try:
                    # Чистим данные: переводим баллы в числа сразу
                    row['final_exam_score'] = float(row['final_exam_score'])
                    self.students.append(row)
                except (ValueError, KeyError):
                    continue
        print(f"Loaded {len(self.students)} records.")

    def preview(self):
        print("First 2 records:", self.students[:2])