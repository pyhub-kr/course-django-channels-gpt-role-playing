import sys
import openai

API_KEY = ""  # your API key

if not API_KEY:
    print("OPENAI API KEY를 지정해주세요.", file=sys.stderr)
    sys.exit(1)


client = openai.OpenAI(api_key=API_KEY)


response = client.completions.create(
    model="gpt-3.5-turbo-instruct",
    prompt="""
Fix grammar errors:
- I is a boy
- You is a girl""".strip(),
)

print(response)
print(response.choices[0].text.strip())


response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "당신은 지식이 풍부한 도우미입니다."},
        {"role": "user", "content": "세계에서 가장 큰 도시는 어디인가요?"}
    ],
)

print(response)
print(response.choices[0].message.content)
