import os
import openai


from dotenv import load_dotenv
from openai import Stream
from openai.types.chat import ChatCompletionChunk

load_dotenv()

# OpenAI 클래스 내부에서 OPENAI_API_KEY 환경변수를 참조합니다.
client = openai.OpenAI()  # api_key=os.getenv("OPENAI_API_KEY"))


response: Stream[ChatCompletionChunk] = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "당신은 영어 학습을 도와주는 챗봇입니다."},
        {"role": "user", "content": "대화를 나눠봅시다."},
    ],
    stream=True,
)


chunk: ChatCompletionChunk
for chunk in response:
    content = chunk.choices[0].delta.content
    if content is not None:
        # chunk 메시지를 표준출력 버퍼링없이 즉시 출력하기
        print(content, end='', flush=True)

