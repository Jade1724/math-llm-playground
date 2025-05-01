class Input:
    def __init__(self, question: str, topic: str, year: int, answer: str):
       self.questions = question
       self.topic = topic 
       self.year = year
       self.answer = answer


class Output:
    def __init__(self, score: int, generated: str, topic: str, techniques: list[str], year: int):
        self.score = score
        self.reasoning = generated
        self.topic = topic
        self.techniques = techniques
        self.year = year
