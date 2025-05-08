class Input:
    def __init__(self, question: str, topic: str, year: int, answer: str):
       self.question = question
       self.topic = topic 
       self.year = year
       self.answer = answer

    def get_prompt(self) -> str:
        return f"""
        Question: {self.question}
        Answer: {self.answer}
        """


class Output:
    def __init__(self, score: int, reasoning: str, feedback: str, topic: str, techniques: list[str], year: int):
        self.score = score
        self.reasoning = reasoning
        self.feedback = feedback
        self.topic = topic
        self.techniques = techniques
        self.year = year
