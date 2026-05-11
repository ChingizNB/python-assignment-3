import json

class ResultSaver:
    def __init__(self, data, path):
        self.data = data
        self.path = path

    def save_json(self):
        with open(self.path, 'w') as f:
            json.dump(self.data, f, indent=4)
        print(f"Results saved to {self.path}")