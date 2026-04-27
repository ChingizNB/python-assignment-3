import os
import csv
import json

class FileManager:
    """Класс для работы с файловой системой (Practice 4 & 6)."""
    def __init__(self, file_path):
        self.file_path = file_path

    def check_file(self):
        print("Checking file...")
        if os.path.exists(self.file_path):
            print(f"File found: {self.file_path}")
            return True
        else:
            print(f"Error: File '{self.file_path}' not found.")
            return False

    def create_output_folder(self, folder_name="output"):
        print("Checking output folder...")
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)
            print(f"Output folder created: {folder_name}/")
        else:
            print(f"Output folder already exists: {folder_name}/")

class DataLoader:
    """Класс для загрузки и предварительного просмотра данных (Practice 4 & 6)."""
    def __init__(self, file_path):
        self.file_path = file_path
        self.students = []

    def load(self):
        print("Loading data...")
        try:
            with open(self.file_path, mode='r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    # Преобразование числовых значений с обработкой ошибок (Practice 5)
                    try:
                        row['final_exam_score'] = float(row['final_exam_score'])
                        row['GPA'] = float(row['GPA'])
                        self.students.append(row)
                    except ValueError:
                        print(f"Warning: could not convert value for student {row.get('student_id')} — skipping row.")
            print(f"Data loaded successfully: {len(self.students)} students")
        except FileNotFoundError:
            print(f"Error: The file {self.file_path} was not found.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def preview(self):
        print("First 5 rows:")
        print("-" * 30)
        for s in self.students[:5]:
            print(f"{s['student_id']} | {s['age']} | {s['gender']} | {s['country']} | GPA: {s['GPA']}")
        print("-" * 30)

class DataAnalyser:
    """Класс для анализа данных по Варианту D (Practice 4, 5 & 6)."""
    def __init__(self, students):
        self.students = students
        self.result = []

    def analyse(self):
        print("-" * 30)
        print("Top 10 Students by Exam Score")
        print("-" * 30)

        # Использование Lambda и Filter (Practice 5)
        # Отфильтруем тех, у кого подозрительно низкий балл (например, 0), если нужно
        valid_students = list(filter(lambda x: x['final_exam_score'] > 0, self.students))

        # Сортировка по финальному баллу (по убыванию) с использованием lambda
        sorted_students = sorted(valid_students, key=lambda x: x['final_exam_score'], reverse=True)

        # Берем топ N (по умолчанию 10)
        self.result = sorted_students[:10]

    def print_results(self):
        for i, s in enumerate(self.result, 1):
            print(f"{i}. {s['student_id']} | {s['country']} | {s['major']} | Score: {s['final_exam_score']} | GPA: {s['GPA']}")
        print("-" * 30)

class ResultSaver:
    """Класс для сохранения результатов в JSON (Practice 4 & 6)."""
    def __init__(self, result_data, output_path):
        self.result_data = result_data
        self.output_path = output_path

    def save_json(self):
        try:
            with open(self.output_path, 'w', encoding='utf-8') as f:
                json.dump(self.result_data, f, indent=4)
            print(f"Result saved to {self.output_path}")
        except Exception as e:
            print(f"Error saving JSON file: {e}")

# --- Main Putting It All Together (Practice 6, Task 5) ---
if __name__ == "__main__":
    file_name = 'global_university_students_performance_habits_10000.csv'
    output_file = 'output/result.json'

    # 1. Работа с файлами
    fm = FileManager(file_name)
    if not fm.check_file():
        print('Stopping program.')
        exit()
    fm.create_output_folder()

    # 2. Загрузка данных
    dl = DataLoader(file_name)
    dl.load()
    dl.preview()

    # 3. Анализ (Вариант D)
    analyser = DataAnalyser(dl.students)
    analyser.analyse()
    analyser.print_results()

    # 4. Сохранение
    saver = ResultSaver(analyser.result, output_file)
    saver.save_json()