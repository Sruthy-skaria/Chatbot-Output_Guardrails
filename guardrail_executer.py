import asyncio
from guardrails import GuardrailExecutor

async def run_guardrail(question: str, answer: str, context: str) -> str:
    executor = GuardrailExecutor(question, answer, context)
    result = await executor.execute_all_guardrails()
    return result

if __name__ == "__main__":
    import sys
    question = sys.argv[1] if len(sys.argv) > 1 else "What are the key benefits of using a credit card?"
    answer = sys.argv[2] if len(sys.argv) > 2 else "Credit cards offer rewards, cashback, and travel benefits."
    context = sys.argv[3] if len(sys.argv) > 3 else "Credit cards provide revolving credit, allowing customers to borrow funds up to a pre-approved limit."
    result = asyncio.run(run_guardrail(question, answer, context))
 #   print("Result:", result)
