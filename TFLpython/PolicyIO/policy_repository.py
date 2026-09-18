import json

class PolicyRepository:
    def __init__(self, filename):
        self.filename = filename

    def get_all(self):

        try :
            with open(self.filename, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            return []
        