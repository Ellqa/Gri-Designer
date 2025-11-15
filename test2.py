from openai import OpenAI


client3 = OpenAI(
    # 更换成自己的 DeepSeek API key
    api_key="sk-1ce6a2c3a41e4238a96374799e4b98e0",
    # DeepSeek 官方 API 地址
    base_url="https://api.deepseek.com"
)

def get_response3(message):
    completion = client3.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {
                "role": "user",
                "content": message,
            }
        ]
    )
    return completion.choices[0].message.content


jap = "この文章は日本語です。"
PROMPT = f"I will give you a sentence in Japanese {jap}. Our goal is to decide if this sentence is dislocated. If this sentence is dislocated, only returen Yes. If not, return No only. do not give any other information."


a= get_response3(PROMPT)
print(a)