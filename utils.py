def format_currency(amount: float) -> str:
    """Formats a float value into a standard Indian Rupee string."""
    return f"₹{amount:,.2f}"

def calculate_percentage(part: float, whole: float) -> str:
    """Calculates percentage safely to avoid division by zero errors."""
    if whole == 0:
        return "0.0%"
    return f"{(part / whole) * 100:.1f}%"

def validate_transaction_amount(amount: float) -> bool:
    """Checks if a transaction amount is valid (greater than zero)."""
    return amount > 0
