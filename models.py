from dataclasses import dataclass
from datetime import date

@dataclass
class Transaction:
    """A data representation of a single financial transaction."""
    transaction_id: int
    user_id: int
    transaction_type: str  # 'Income' or 'Expense'
    category: str
    amount: float
    transaction_date: date

    def is_expense(self) -> bool:
        """Returns True if the transaction is an expense."""
        return self.transaction_type.lower() == 'expense'
        
    def summary(self) -> str:
        """Returns a formatted summary of the transaction."""
        return f"{self.transaction_date}: {self.category} - {self.amount}"
