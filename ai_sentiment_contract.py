# ai_sentiment_contract.py
# Built for GenLayer Protocol (Intelligent Contracts)

class AISentimentContract:
    def __init__(self):
        # State variables to track interactions
        self.total_analyses = 0
        self.last_user = "None"
        self.positive_count = 0

    def analyze_message(self, user_address: str, message: str) -> str:
        """
        Users send a message, and the AI evaluates if it is positive or neutral.
        In the GenLayer ecosystem, this utilizes Validator LLMs.
        """
        self.total_analyses += 1
        self.last_user = user_address

        # Simplified logic for GenVM execution
        if "good" in message.lower() or "great" in message.lower() or "awesome" in message.lower():
            self.positive_count += 1
            return "AI Validator: APPROVED. The message from " + user_address + " is POSITIVE."
        elif len(message) < 5:
            return "AI Validator: REJECTED. Message is too short to analyze."
        else:
            return "AI Validator: NEUTRAL. The message has been logged."

    def get_contract_stats(self) -> str:
        """
        Returns the overall statistics of the intelligent contract.
        """
        return "Total Analyses: " + str(self.total_analyses) + " | Positive Messages: " + str(self.positive_count)

    def get_last_user(self) -> str:
        return self.last_user
