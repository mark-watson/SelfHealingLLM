# Self healing or self correcting LLM experiments

## Example

```
$ python main.py 
Enter your question: What is 8.1 + 9.998?
ChatCompletion(id='chatcmpl-A6SpntK0EeYnwaGyyFqGFa3NRard6', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='8.1 + 9.998 equals 18.098.', refusal=None, role='assistant', function_call=None, tool_calls=None))], created=1726104171, model='gpt-4o-mini-2024-07-18', object='chat.completion', service_tier=None, system_fingerprint='fp_483d39d857', usage=CompletionUsage(completion_tokens=14, prompt_tokens=19, total_tokens=33))


* content:
8.1 + 9.998 equals 18.098.


Response: 8.1 + 9.998 equals 18.098.
8

The calculation in the original response is incorrect. 8.1 + 9.998 equals 18.098, not 18.008.

==================================================
Claude Evaluation:
==================================================
8

The calculation in the original response is incorrect. 8.1 + 9.998 equals 18.098, not 18.008.

Eval lines: ['8', '', 'The calculation in the original response is incorrect. 8.1 + 9.998 equals 18.098, not 18.008.']


*********** OpenAI's first response is not satisfactory, try again using criticism: *****


ChatCompletion(id='chatcmpl-A6Spq9bvsy8DCw1K2uuZobKdLcdad', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='Thank you for your feedback regarding the calculation of 8.1 + 9.998. \n\nTo clarify, the correct calculation is as follows:\n\n8.1 + 9.998 = 18.098\n\nI appreciate your note on the accuracy, as it is crucial to provide precise mathematical responses. \n\nConfidence Score: 1.0', refusal=None, role='assistant', function_call=None, tool_calls=None))], created=1726104174, model='gpt-4o-mini-2024-07-18', object='chat.completion', service_tier=None, system_fingerprint='fp_483d39d857', usage=CompletionUsage(completion_tokens=70, prompt_tokens=138, total_tokens=208))


* content:
Thank you for your feedback regarding the calculation of 8.1 + 9.998. 

To clarify, the correct calculation is as follows:

8.1 + 9.998 = 18.098

I appreciate your note on the accuracy, as it is crucial to provide precise mathematical responses. 

Confidence Score: 1.0




Improved Response: Thank you for your feedback regarding the calculation of 8.1 + 9.998. 

To clarify, the correct calculation is as follows:

8.1 + 9.998 = 18.098

I appreciate your note on the accuracy, as it is crucial to provide precise mathematical responses. 

Confidence Score: 1.0
```

