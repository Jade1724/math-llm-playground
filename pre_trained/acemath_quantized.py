"""
Quantized version of NVIDIA maths LLM using llama_cpp_python for GGUF format.
"""

from llama_cpp import Llama

llm = Llama.from_pretrained(
	repo_id="DevQuasar/nvidia.AceMath-7B-Instruct-GGUF",
	filename="nvidia.AceMath-7B-Instruct.Q2_K.gguf",
)


# Define the prompt
prompt = (
    "Jen enters a lottery by picking $4$ distinct numbers from $S=\\{1,2,3,\\cdots,9,10\\}.$ "
    "$4$ numbers are randomly chosen from $S.$ She wins a prize if at least two of her numbers "
    "were $2$ of the randomly chosen numbers, and wins the grand prize if all four of her numbers "
    "were the randomly chosen numbers. The probability of her winning the grand prize given that "
    "she won a prize is $\\tfrac{m}{n}$ where $m$ and $n$ are relatively prime positive integers. "
    "Find $m+n$."
)

# Generate a response
response = llm(prompt, max_tokens=2048)

# Print the response
print(response["choices"][0]["text"])