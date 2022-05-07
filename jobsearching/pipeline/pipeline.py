class Pipeline:
    def __init__(self, steps):
        self.steps = steps

    def run(self, inputs):
        data = None
        for step in self.steps:
            data = step.process(data, inputs)
