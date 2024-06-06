- [Amazon S3 examples using SDK for JavaScript (v3)](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/javascript_s3_code_examples.html)
- Create IAM user and generate keys to create a s3 client in both python and javascript

### GPT Response format
```json
{
  "id": "chatcmpl-9X7mUIWjMcOlFMJ6YspGV4ldoqLEp",
  "object": "chat.completion",
  "created": 1717681762,
  "model": "gpt-4o-2024-05-13",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "This is a test!"
      },
      "logprobs": null,
      "finish_reason": "stop"
    }
  ],
  "usage": {
    "prompt_tokens": 13,
    "completion_tokens": 5,
    "total_tokens": 18
  },
  "system_fingerprint": "fp_319be4768e"
}
```

- The `stream: True` option in Chat is whether or not chunk the response. In streaming mode, responses are chunked, and these chunks do contain a delta field, which differs from the non-streaming response format.