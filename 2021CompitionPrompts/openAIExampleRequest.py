#https://beta.openai.com/docs/api-reference/completions/create

import os
import openai
openai.api_key = os.getenv("OPENAI_API_KEY")
openai.Completion.create(
  model="text-davinci-003",
  prompt="Say this is a test",
  max_tokens=7,
  temperature=0
)

# {
  # "model": "text-davinci-003",
  # "prompt": "Say this is a test",
  # "max_tokens": 7,
  # "temperature": 0,
  # "top_p": 1,
  # "n": 1,
  # "stream": false,
  # "logprobs": null,
  # "stop": "\n"
# }


# {
  # "id": "cmpl-uqkvlQyYK7bGYrRHQ0eXlWi7",
  # "object": "text_completion",
  # "created": 1589478378,
  # "model": "text-davinci-003",
  # "choices": [
    # {
      # "text": "\n\nThis is indeed a test",
      # "index": 0,
      # "logprobs": null,
      # "finish_reason": "length"
    # }
  # ],
  # "usage": {
    # "prompt_tokens": 5,
    # "completion_tokens": 7,
    # "total_tokens": 12
  # }
# }
