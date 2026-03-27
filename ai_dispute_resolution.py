# ai_dispute_resolution.py
# Built for GenLayer Protocol (Intelligent Contracts)

class AIDisputeResolution:
    def __init__(self, buyer: str, seller: str, escrow_amount: int):
        # Initializing the escrow contract between a buyer and a seller
        self.buyer = buyer
        self.seller = seller
        self.escrow_amount = escrow_amount
        self.status = "ACTIVE"  # States: ACTIVE, DISPUTED, RESOLVED
        self.resolution_winner = "None"

    def raise_dispute(self, initiator: str, evidence: str) -> str:
        """
        Allows either party to raise a dispute by providing natural language evidence.
        """
        if self.status != "ACTIVE":
            return "Error: Contract is not active or already disputed."
        
        self.status = "DISPUTED"
        return f"Dispute officially raised by {initiator}. Evidence submitted to AI Validators for review."

    def resolve_dispute(self, ai_validator_decision: str) -> str:
        """
        In the GenVM environment, an LLM Validator calls this method after evaluating the evidence.
        The AI reads the context and makes a subjective, natural language decision.
        """
        if self.status != "DISPUTED":
            return "Error: No active dispute to resolve."

        # Simulating GenVM LLM decision processing
        decision_text = ai_validator_decision.lower()
        
        if "favor buyer" in decision_text:
            self.resolution_winner = self.buyer
            self.status = "RESOLVED"
            return f"AI Decision: Favorable to Buyer. {self.escrow_amount} tokens returned to {self.buyer}."
        
        elif "favor seller" in decision_text:
            self.resolution_winner = self.seller
            self.status = "RESOLVED"
            return f"AI Decision: Favorable to Seller. {self.escrow_amount} tokens released to {self.seller}."
        
        else:
            return "AI Decision: Inconclusive. Requesting more evidence from both parties."

    def get_contract_status(self) -> str:
        return f"Current Status: {self.status} | Winner: {self.resolution_winner}"
