from analytics.file_manager import FileManager
from analytics.data_loader import DataLoader
from analytics.analyser import TopStudentsAnalyser
from analytics.report import Report
from analytics.result_saver import ResultSaver

def main():
    CSV_NAME = 'global_university_students_performance_habits_10000.csv'

    # 1. Работа с файлами
    fm = FileManager(CSV_NAME)
    if not fm.check_file(): return
    fm.create_output_folder()

    # 2. Загрузка
    dl = DataLoader(CSV_NAME)
    dl.load()

    # 3. Анализ (Полиморфизм: создаем список объектов базового класса)
    analysers = [TopStudentsAnalyser(dl.students)]

    for a in analysers:
        print(f"Running: {a}") # Вызов __str__

        # 4. Ассоциация (Передаем анализатор в отчет)
        rep = Report(a)
        rep.print_report()

        # 5. Сохранение
        ResultSaver(a.result, 'output/result.json').save_json()

if __name__ == "__main__":
    main()