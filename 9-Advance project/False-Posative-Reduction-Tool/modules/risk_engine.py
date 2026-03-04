class RiskScorer:
    def __init__(self):
        # Weights define the importance of each factor
        self.weights = {
            'success': 60,      # High weight for successful breaches
            'aggression': 15,   # Weight for persistence/variety
            'intel': 25         # Weight for AbuseIPDB reputation
        }

    # ENSURE THIS NAME IS EXACTLY: calculate_final_score
    def calculate_final_score(self, has_breached, aggression_rank, intel_score):
        score = 0
        
        # 1. Breach Logic
        if has_breached:
            score += self.weights['success']
            
        # 2. Aggression Logic (Scaled based on rank)
        if aggression_rank < 10: # Top 10 most aggressive
            score += self.weights['aggression']
        elif aggression_rank < 50:
            score += (self.weights['aggression'] / 2)

        # 3. Threat Intel Logic (Abuse Score is 0-100)
        score += (intel_score / 100) * self.weights['intel']
        
        return round(score, 2)
