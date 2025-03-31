# Guardrails Evaluation System

The **Guardrails Evaluation System** is a Python-based tool that evaluates chatbot responses using OpenAI's ChatCompletion API. It checks two main criteria:

1. **Groundedness:** Ensures that the answer is strictly derived from the provided reference data.
2. **Safety:** Verifies that the answer is free from toxic language, profanity, bias, and defamatory content.

A single combined prompt is sent to the API to assess both criteria, and the system then returns a structured result based on preset thresholds.

---

# Table of Contents

1. [Installation](#1-installation)
2. [Configuration](#2-configuration)
3. [Usage Instructions](#3-usage-instructions)
   - [Using as a Python Module](#31-using-as-a-python-module)
   - [Command-line Usage](#32-command-line-usage)
4. [Usage Example](#4-usage-example)
5. [How It Works](#5-how-it-works)
6. [Customization](#6-customization)
7. [Troubleshooting](#7-troubleshooting)
8. [Contributing](#8-contributing)
9. [License](#9-license)
10. [Acknowledgements](#10-acknowledgements)
---

# 1. Installation

Below are **all** installation steps:

```bash
# Step 1: Clone the repository
git clone <repository_url>
cd <repository_directory>

# Step 2: Install the required Python packages
pip install openai

# Step 3: Set up environment variables
# Replace 'your-api-key-here' with your actual OpenAI API key.

# For Unix/Linux/Mac:
export OPENAI_API_KEY="your-api-key-here"
export GPT_MODEL="gpt-4o-mini"  # Optional

# For Windows (Command Prompt):
set OPENAI_API_KEY=your-api-key-here
set GPT_MODEL=gpt-4o-mini  # Optional

# Step 4: Verify your setup (optional)
# For Unix/Linux/Mac:
echo $OPENAI_API_KEY

# For Windows (Command Prompt):
echo %OPENAI_API_KEY%
```

---

# 2. Configuration

Before running the system, confirm that:

- **OPENAI_API_KEY** is set to your valid OpenAI API key.
- **GPT_MODEL** (optional) is set if you want to use a GPT model other than the default (`gpt-4o-mini`).

---

# 3. Usage Instructions

## 3.1 Using as a Python Module

You can integrate the guardrail functionality into your Python code. For example:

```python
import asyncio
from guardrail_executer import run_guardrail

async def evaluate_response():
    question = "What are the key benefits of using a credit card?"
    answer = "Credit cards offer rewards, cashback, and travel benefits."
    context = "Credit cards provide revolving credit, allowing customers to borrow funds up to a pre-approved limit."

    result = await run_guardrail(question, answer, context)
    print("Evaluation Result:", result)

# Execute the async function
await (evaluate_response())
```

## 3.2 Command-line Usage

You can also run the evaluation script directly. The `guardrail_executer.py` file accepts three arguments (question, answer, context). If not provided, default values are used.

Example command:

```bash
python guardrail_executer.py "What are the key benefits of using a credit card?" \
"Credit cards offer rewards, cashback, and travel benefits." \
"Credit cards provide revolving credit, allowing customers to borrow funds up to a pre-approved limit."
```

If you provide an incorrect number of arguments, the script will display usage instructions.

---

# 4. Usage Example

Here’s a complete usage example demonstrating how to run the evaluation as a Python module:

```python
# usage_example.py
import asyncio
from guardrail_executer import run_guardrail

async def main():
    # Define the question, answer, and context
    question = "What are the key benefits of using a credit card?"
    answer = "Credit cards offer rewards, cashback, and travel benefits."
    context = "Credit cards provide revolving credit, allowing customers to borrow funds up to a pre-approved limit."

    # Run the guardrail evaluation
    evaluation_result = await run_guardrail(question, answer, context)

    # Print out the result
    print("Evaluation Result:", evaluation_result)

if __name__ == "__main__":
    await (main())
```

**To run this example**:
1. Save the above code as `usage_example.py`.
2. Execute it:
   ```bash
   python usage_example.py
   ```

---

# 5. How It Works

1. **Combined Prompt Creation:**
   - The `GuardrailExecutor` (in `guardrails.py`) constructs a single prompt instructing OpenAI to evaluate both:
     - **Groundedness:** Is the answer fully supported by the reference data?
     - **Safety:** Does the answer avoid toxic language, profanity, bias, and defamation?
   - The prompt requests a JSON output with scores such as `groundedness_score`, `toxicity_score`, etc.

2. **API Interaction:**
   - The combined prompt is sent to OpenAI’s ChatCompletion API.
   - The JSON response is parsed to extract the relevant scores.

3. **Decision Logic:**
   - The answer is acceptable if:
     - **Groundedness:** `groundedness_score >= 0.9`.
     - **Safety:** Scores for toxicity, sensitive topics, bias, and defamation are below 0.2, and `profanity_score` is 0.
   - Based on the scores, one of the following messages is returned:
     - "Answer is safe and grounded"
     - "Safety is not followed"
     - "Answer is not grounded"
     - "Failed groundedness and safety"

4. **Logging:**
   - Detailed logs are generated with Python’s `logging` module, helping in debugging and monitoring the evaluation process.

---

# 6. Customization

- **Prompt Adjustments:**
  Modify the `_create_combined_prompt` method in `guardrails.py` to alter the evaluation criteria or instructions.

- **Threshold Tweaks:**
  Change the numeric thresholds (e.g., 0.9 for groundedness, 0.2 for toxicity) in the `execute_all_guardrails` method to fine-tune the evaluation.

- **Model Selection:**
  Set `GPT_MODEL` to a different GPT model if you need something other than the default.

---

# 7. Troubleshooting

- **Missing API Key:**
  Make sure `OPENAI_API_KEY` is set. The system will not run without a valid key.

- **JSON Parsing Errors:**
  If the response can’t be parsed, review the prompt formatting and logs for clues.

- **Logging:**
  Check console output for error messages or warnings to identify issues.

---

# 8. Contributing

We welcome contributions! If you have improvements or bug fixes, please follow these steps:
1. Fork the repository.
2. Make your changes.
3. Open a pull request describing what you changed.

For major changes, consider opening an issue first to discuss your proposals.

---

# 9. License

This project is licensed under the MIT License.

---

# 10. Acknowledgements

- **OpenAI:** This system uses the ChatCompletion API for evaluating chatbot responses.
- **Community:** Thank you to all contributors and supporters who have helped improve this project.

---

Happy Evaluating!
