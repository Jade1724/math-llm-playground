"""
Quantized version of NVIDIA maths LLM using llama_cpp_python for GGUF format.
"""

from llama_cpp import Llama

llm = Llama.from_pretrained(
	repo_id="DevQuasar/nvidia.AceMath-7B-Instruct-GGUF",
	filename="nvidia.AceMath-7B-Instruct.Q2_K.gguf",
    use_gpu=True,
)

def chat_completion(prompt: str, system_prompt: str) -> str:
    """
    Function to generate a chat completion using the Llama model.
    """
    if system_prompt:
        prompt = f"{system_prompt}\n\n{prompt}"

    response = llm(prompt, max_tokens=2048)
    return response["choices"][0]["text"]