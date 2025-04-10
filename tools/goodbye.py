"""
Goodbye tool implementation for the Hello-Goodbye MCP server.
"""

async def say_goodbye(name: str, formal: bool = False) -> str:
    """
    Say goodbye to someone.
    
    Args:
        name: The name of the person to say goodbye to
        formal: Whether to use formal language
        
    Returns:
        A farewell message
    """
    if formal:
        return f"Farewell, {name}. It was a pleasure to make your acquaintance."
    else:
        return f"Goodbye, {name}! Have a great day!" 