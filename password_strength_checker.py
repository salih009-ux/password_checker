
import re

def check_password_strength(password):
    strength = 0
    feedback = []

    # Check length
    if len(password) >= 8:
        strength += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Check for lowercase letters
    if re.search(r"[a-z]", password):
        strength += 1
    else:
        feedback.append("Password should include lowercase letters.")

    # Check for uppercase letters
    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        feedback.append("Password should include uppercase letters.")

    # Check for numbers
    if re.search(r"[0-9]", password):
        strength += 1
    else:
        feedback.append("Password should include numbers.")

    # Check for special characters
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1
    else:
        feedback.append("Password should include special characters.")

    # Provide feedback based on the strength score
    if strength == 5:
        return "Strong password!", feedback
    elif 3 <= strength < 5:
        return "Moderate password", feedback
    else:
        return "Weak password", feedback


# Example usage
password = input("Enter a password to check its strength: ")
result, advice = check_password_strength(password)
print(f"Password Strength: {result}")
if advice:
    print("Feedback:")
    for line in advice:
        print(f"- {line}")
