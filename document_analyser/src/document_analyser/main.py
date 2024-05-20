#!/usr/bin/env python
from document_analyser.crew import DocumentAnalyserCrew


def run():
    # Replace with your inputs, it will automatically interpolate any tasks and agents information
    inputs = {
        'topic': 'AI LLMs'
    }
    DocumentAnalyserCrew().crew().kickoff(inputs=inputs)


if __name__ == "__main__":
    #topic = input('Enter a Topic of interest')
    run()