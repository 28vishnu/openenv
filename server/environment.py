class SQLEnv:
    def __init__(self):
        self.tasks = {
            "easy": "SELECT all users from the 'users' table.",
            "medium": "COUNT the number of orders in the 'orders' table.",
            "hard": "JOIN 'users' and 'orders' on 'user_id' to find total spent."
        }
        self.reset()

    def reset(self):
        self.observation = "Connected to Database: tables ['users', 'orders'] available."
        return self.observation

    def step(self, action):
        query = action.strip().upper()
        # Easy Task Logic
        if "SELECT *" in query and "FROM USERS" in query:
            obs, reward, done = "Found 50 users.", 1.0, True
        # Medium Task Logic
        elif "SELECT COUNT" in query and "FROM ORDERS" in query:
            obs, reward, done = "Found 120 orders.", 1.0, True
        else:
            obs, reward, done = "Syntax Error or Incorrect Query.", 0.0, False
        return obs, reward, done