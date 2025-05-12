# This code is a simple simulation of an LLM (Large Language Model) interaction.
# It defines a class `LLM` with a method `post` that simulates sending a prompt to an LLM and receiving a response.
# The `ask` function takes a prompt as input, creates an instance of the `LLM` class, and calls the `post` method to get a response.
# The response is then returned as a string.

class LLM:
    def post(self, prompt):
        # Simulate a call to an LLM API
        return f"Response to: {prompt}. This is a simulated response from the LLM."


def ask(prompt: str) -> str:
    """
    Ask the LLM a question and get a response.

    Args:
        prompt (str): The question to ask the LLM.

    Returns:
        str: The response from the LLM.
    """
    llm = LLM()
    response = llm.post(prompt)
    return response

if __name__ == "__main__":
    # Example usage
    question = "What is the capital of France?"
    answer = ask(question)
    print(answer)
# This code is a simple simulation of an LLM (Large Language Model) interaction.
# It defines a class `LLM` with a method `post` that simulates sending a prompt to an LLM and receiving a response.
# The `ask` function takes a prompt as input, creates an instance of the `LLM` class, and calls the `post` method to get a response.
# The response is then returned as a string.