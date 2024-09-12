import os
import time
from openai_module import send_openai_request
from claude_module import send_claude_request
from utils import format_output


def main():
    question = input("Enter your question: ")
    openai_response = send_openai_request(question)
    print(f"Response: {openai_response}")

    evaluation_prompt = f"""Evaluate the following response to the question '{question}':

Response: {openai_response}

Please rate this response on a scale of 1-10 for each of the following criteria:

  Accuracy

Return only a single number between 0 and 9 on the first line of the reposnse. The second line of the response is a criticism of previous answer."""

    claude_evaluation = send_claude_request(evaluation_prompt)
    print(format_output(f"Claude Evaluation:", claude_evaluation))

    eval_lines = claude_evaluation.split("\n")
    print(f"Eval lines: {eval_lines}")

    score = int(eval_lines[0])

    if score >= 8.5:
        print(f"OpenAI's response is satisfactory")
        return

    print(
        f"\n\n*********** OpenAI's first response is not satisfactory, try again using criticism: *****\n\n"
    )
    # If Claude suggests improvements, get a better response from OpenAI
    improvement_prompt = f"""The original question was: '{question}'
Your previous response was: {openai_response}
Here's feedback on your response:
{eval_lines[1:]}

Please provide an improved response based on this feedback. Make sure to address all the points mentioned in the evaluation and aim for a comprehensive, accurate, and well-structured answer. Also, provide a confidence score between 0 and 1 for your new response."""

    improved_response = send_openai_request(improvement_prompt)
    print(f"\n\nImproved Response: {improved_response}\n")


if __name__ == "__main__":
    main()
