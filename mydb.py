import json
import os

class Database:

    def __init__(self, path='db.json'):
        self.path = path
        # Ensure file exists and is valid JSON
        if not os.path.exists(self.path) or os.path.getsize(self.path) == 0:
            with open(self.path, 'w') as f:
                json.dump({}, f)

    def _load_database(self):
        """Load JSON database safely."""
        try:
            with open(self.path, 'r') as rf:
                return json.load(rf)
        except (json.JSONDecodeError, FileNotFoundError):
            # If the file is empty or invalid, reset it
            with open(self.path, 'w') as wf:
                json.dump({}, wf)
            return {}

    def add_data(self, name, email, password):
        database = self._load_database()

        if email in database:
            return 0  # Email already exists
        else:
            database[email] = [name, password]
            with open(self.path, 'w') as wf:
                json.dump(database, wf, indent=4)
            return 1

    def search(self, email, password):
        database = self._load_database()

        if email in database and database[email][1] == password:
            return 1  # Login success
        else:
            return 0  # Invalid credentials
