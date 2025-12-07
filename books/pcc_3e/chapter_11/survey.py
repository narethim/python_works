class AnonymousSurvey:
    """Collect anonymous answers to a sutvey question."""
    def __init__(self, question):
        """Stor a question, and prepare to store responses."""
        self.question = question
        self.responses = []

    def show_question(self):
        """Show the survey question."""
        print(self.question)

    def store_response(self, new_response):
        """Store a single response to the survey."""
        self.responses.append(new_response)

    def show_result(self):
        """Show all the resonses that have been given."""
        print("Survey result: ")
        for response in self.responses:
            print(f"- {response}")
