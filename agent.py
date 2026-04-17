class Agent:
    def act(self, email):
        email = email.lower()

        if "free" in email or "win" in email or "offer" in email: 
            return "spam"
        elif "urgent" in email or "important" in email:
            return "urgent"
        elif "meeting" in email or "project" in email or "team" in email:
            return "work"
        else:
            return "personal"
