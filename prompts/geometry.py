"""
User prompts for LLMs to generate auto grading of math problems and answers pair. 
Topic: Geometry
"""
import json
import re
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from models.llm import Input
from pre_trained.acemath_quantized import chat_completion
from prompts.common import system_prompt

input = Input(
    question="Find the area of the triangle with a base of 8cm and perpendicular height of 4cm. Show your working stesp and final answer using the unit",
    topic="Geometry",
    year=7,
    answer="The formula for the area of a triangle is A = 1/2 * base * height. So, the area of the triangle is A = 1/2 * 8cm * 4cm = 16cm^2. Therefore, the area of the triangle is 16cm^2.",
)

output = chat_completion(prompt=input.get_prompt(), system_prompt=system_prompt)

# Clean up the output text
def clean_output(output: str) -> str:
    # Remove LaTeX-style math expressions
    output = re.sub(r"\\\[.*?\\\]", "", output, flags=re.DOTALL)
    # Remove unnecessary escape characters
    output = output.replace("\\,", "").replace("\\text", "").replace("\\frac", "")
    # Remove extra whitespace
    output = re.sub(r"\s+", " ", output).strip()
    return output

data = {
    "input": {
        "question": input.question,
        "topic": input.topic,
        "year": input.year,
        "answer": input.answer,
    },
    "output": output,
    "sanitised": clean_output(output)
}

with open("data/output/geometry.json", "w") as f:
    json.dump(data, f, indent=4)