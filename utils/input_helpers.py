def get_clean_integer(prompt_text):
    """Ensures the user inputs a valid number instead of breaking the app with text."""
    while True:
        try:
            value = int(input(prompt_text))
            return value
        except ValueError:
            print("❌ Invalid input! Please enter a valid round number.")