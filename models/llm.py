class Input:
    def __init__(self, question: str, topic: str, year: int, answer: str):
       self.questions = question
       self.topic = topic 
       self.year = year
       self.answer = answer

    def get_prompt(self) -> str:
        return f"""
        Question: {self.questions}
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
