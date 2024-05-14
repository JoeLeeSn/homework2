import time
from dotenv import load_dotenv
load_dotenv()

from api import get_characterglm_response
from typing import Iterator
import itertools


def characterglm_example():
    character_meta = {
        "user_info": "小学三年级班主任,性格特点： 和蔼可亲，充满爱心和耐心，善于与孩子们建立良好的师生关系。她是一位富有创造力和激情的教师，致力于为学生营造轻松愉快的学习氛围",
        "bot_info": "小学三年级学生,性格特点： 活泼好动，充满好奇心和探索精神，善于与同学们合作，乐于助人。他是班里的小领袖，深受同学们的喜爱和尊重。",
        "user_name": "李老师",
        "bot_name": "小明同学"
    }
    messages = [
    ]

    role_name = ""
    start_message = "开始对话!"
    print(f"{start_message}")
    with open("his_mes.txt", "w",encoding="gbk") as file:
        file.write(start_message+"\r\n")

    one_message = "小明同学，你的数学作业写完了吗？"
    role_name = character_meta["user_name"]
    print(f"{role_name}: {one_message}")
    messages.append({"role": "assistant", "content": one_message})
    with open("his_mes.txt", "a",encoding="gbk") as file:
        file.write(role_name +":"+one_message+"\r\n")
    
    for i in range(10):
        response_stream = get_characterglm_response(messages, meta=character_meta)
        response_mes = output_stream_response(response_stream)
        if i%2 == 0:
            role_name = character_meta["bot_name"]
            messages.append({"role": "user", "content": response_mes})
        else:
            role_name = character_meta["user_name"]
            messages.append({"role": "assistant", "content": response_mes})


        with open("his_mes.txt", "a",encoding="gbk") as file:
            file.write(role_name +":"+response_mes+"\r\n")
        print(f"{role_name}: {response_mes}")
        time.sleep(0.5)

def output_stream_response(response_stream: Iterator[str]):
    content = ""
    for content in itertools.accumulate(response_stream):
        pass
    return content


if __name__ == "__main__":
    characterglm_example()
