from pollution_thresholds import PH_MIN, PH_MAX, TURBIDITY_MAX, TEMPERATURE_MAX

def pollution_severity(ph, turbidity, temperature):
    if turbidity > 35 or ph < 6 or ph > 9 or temperature > 40:
        return "HIGH"
    elif turbidity > TURBIDITY_MAX or temperature > TEMPERATURE_MAX:
        return "MEDIUM"
    else:
        return "LOW"

def detect_pollution(ph, turbidity, temperature):
    issues = []

    if ph < PH_MIN or ph > PH_MAX:
        issues.append("Abnormal pH")

    if turbidity > TURBIDITY_MAX:
        issues.append("High Turbidity")

    if temperature > TEMPERATURE_MAX:
        issues.append("High Temperature")

    severity = pollution_severity(ph, turbidity, temperature)

    if issues:
        return True, issues, severity
    else:
        return False, ["Water Quality Normal"], "LOW"
