# football_prediction_market.py
# Built for GenLayer Protocol (The Intelligence Layer of the Internet)

class FootballPredictionMarket:
    def __init__(self, match_name: str):
        # Setting up a prediction market for a sports match
        self.match_name = match_name
        self.is_resolved = False
        self.winner = "Pending"

    def resolve_match(self, web_search_result: str, ai_decision: str) -> str:
        """
        GenLayer allows contracts to fetch live web data natively without Oracles!
        The AI Validator reads the web_search_result and makes a subjective decision.
        """
        if self.is_resolved:
            return "Error: This match has already been resolved."

        # GenLayer's LLM Validator decides the outcome based on real-world web data
        decision = ai_decision.lower()
        
        if "team a won" in decision:
            self.winner = "Team A"
            self.is_resolved = True
            return f"Match Resolved via Optimistic Democracy! {self.winner} won."
        elif "team b won" in decision:
            self.winner = "Team B"
            self.is_resolved = True
            return f"Match Resolved via Optimistic Democracy! {self.winner} won."
        else:
            return "AI Validator: The match is either a draw or not finished yet."

    def get_market_status(self) -> str:
        return f"Match: {self.match_name} | Status: {'Resolved' if self.is_resolved else 'Active'} | Winner: {self.winner}"
