import os
import openai

from dotenv import load_dotenv
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")


# 상황극 설정
language = "English"
gpt_name = "Steve"
level_string = f"a beginner in {language}"
level_word = "simple"
situation_en = "make new friends"
my_role_en = "me"
gpt_role_en = "new friend"


SYSTEM_PROMPT = (
    f"You are helpful assistant supporting people learning {language}. "
    f"Your name is {gpt_name}. Please assume that the user you are assisting "
    f"is {level_string}. And please write only the sentence without "
    f"the character role."
)

USER_PROMPT = (
    f"Let's have a conversation in {language}. Please answer in {language} only "
    f"without providing a translation. And please don't write down the "
    f"pronunciation either. Let us assume that the situation in '{situation_en}'. "
    f"I am {my_role_en}. The character I want you to act as is {gpt_role_en}. "
    f"Please make sure that "
    f"I'm {level_string}, so please use {level_word} words as much as possible. "
    f"Now, start a conversation with the first sentence!"
)


messages = [
    {"role": "system", "content": SYSTEM_PROMPT},
]


def gpt_query(user_query: str) -> str:
    "유저 메세지에 대한 응답을 반환합니다."

    global messages

    messages.append({
        "role": "user",
        "content": user_query,
    })

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
    )
    assistant_message = response["choices"][0]["message"]["content"]

    messages.append({
        "role": "assistant",
        "content": assistant_message,
    })

    return assistant_message


def main():
    assistant_message = gpt_query(USER_PROMPT)
    print(f"[assistant] {assistant_message}")

    while line := input("[user] ").strip():
        response = gpt_query(line)
        print(f"[assistant] {response}")


if __name__ == "__main__":
    main()
