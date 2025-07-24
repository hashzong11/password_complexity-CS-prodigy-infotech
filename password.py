import re

def check_password_strength(password):
    score = 0

    # Check length
    if len(password) >= 8:
        score += 1

    # Check uppercase
    if re.search(r"[A-Z]", password):
        score += 1

    # Check lowercase
    if re.search(r"[a-z]", password):
        score += 1

    # Check digits
    if re.search(r"[0-9]", password):
        score += 1

    # Check special characters
    if re.search(r"[@$!%*?&]", password):
        score += 1

    # Feedback
    if score <= 2:
        return "Weak password"
    elif score == 3:
        return "Moderate password"
    elif score == 4:
        return "Strong password"
    else:
        return "Very strong password"

# Test
password = input("Enter your password: ")
print(check_password_strength(password))
