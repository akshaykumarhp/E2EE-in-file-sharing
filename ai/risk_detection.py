def predict_risk(activity_data):
    risk_score = 0
    if activity_data["failed_attempts"] > 3:
        risk_score += 50
    if activity_data["file_size_change"] > 0.2:
        risk_score += 30
    if activity_data["time"] in ["2 AM", "3 AM"]:
        risk_score += 20
    return min(risk_score, 100)