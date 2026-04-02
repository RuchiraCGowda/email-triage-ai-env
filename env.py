class EmailEnv:
    def __init__(self, mode="all"):
        self.actions = ["spam", "work", "personal", "urgent"]

        self.easy = [
            ("Win money now!!!", "spam"),
            ("Meeting at 10 AM", "work"),
            ("Hey, how are you?", "personal")
        ]

        self.medium = [
            ("Limited time offer just for you", "spam"),
            ("Project discussion tomorrow", "work"),
            ("Let's catch up soon", "personal"),
            ("URGENT: Submit report", "urgent")
        ]

        self.hard = [
            ("Your account might need attention", "urgent"),
            ("Don't miss this opportunity", "spam"),
            ("Can we reschedule?", "personal"),
            ("Team sync regarding updates", "work")
        ]

        if mode == "easy":
            self.emails = self.easy
        elif mode == "medium":
            self.emails = self.medium
        elif mode == "hard":
            self.emails = self.hard
        else:
            self.emails = self.easy + self.medium + self.hard

        self.index = 0
        self.correct = 0

    def reset(self):
        self.index = 0
        self.correct = 0
        return {"email": self.emails[self.index][0]}

    def step(self, action):
        correct_label = self.emails[self.index][1]

        if action == correct_label:
            reward = 10
            self.correct += 1
        else:
            if correct_label == "urgent":
                reward = -20
            else:
                reward = -5

        self.index += 1
        done = self.index >= len(self.emails)

        if not done:
            next_email = self.emails[self.index][0]
        else:
            next_email = None

        return {"email": next_email}, reward, done