from llama_cpp import Llama

model = Llama(model_path=input("Model path: "))

while True:
    conversation = [
        {"role": "user", "content": input("Message: ")}
    ]

    result = model.create_chat_completion(
        messages=conversation
    )

    print("Title:", result["choices"][0]["message"]["content"])