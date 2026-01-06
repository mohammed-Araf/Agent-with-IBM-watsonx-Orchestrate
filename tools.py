from ibm_watsonx_orchestrate.tools import tool

@tool
def calculate(operation: str, a: float, b: float) -> float:
    """
    Performs basic arithmetic operations.
    
    Args:
        operation: The operation to perform ('add', 'subtract', 'multiply', 'divide').
        a: The first number.
        b: The second number.
        
    Returns:
        The result of the calculation.
    """
    if operation == 'add':
        return a + b
    elif operation == 'subtract':
        return a - b
    elif operation == 'multiply':
        return a * b
    elif operation == 'divide':
        if b == 0:
            return float('inf') # Handle division by zero
        return a / b
    else:
        raise ValueError(f"Unknown operation: {operation}")
