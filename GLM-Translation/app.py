from flask import Flask, request, jsonify
import whisper
import os
from transformers import AutoTokenizer, AutoModel

app = Flask(__name__)


@app.route('/process_audio', methods=['POST'])
def process_audio():

    # 从请求中获取上传的文件
    file_name = request.files['file_path'].filename
    prompt = request.form['prompt']
    # conversation_id = request.form['conversationId']

    # 加载模型并转录音频
    model = whisper.load_model("base")
    result = model.transcribe(file_name)
    text = result["text"]

    # 返回转写内容
    return jsonify({'original_text': text, 'summary_text': '', 'conversationId': ''})


@app.route('/process_summary', methods=['POST'])
def process_summary():

    # 配置代理，保证墙内外网络正常
    os.environ['CURL_CA_BUNDLE'] = ''
    os.environ['HTTP_PROXY'] = "http://127.0.0.1:1080"
    os.environ['HTTPS_PROXY'] = "http://127.0.0.1:1080"

    # 从请求中获取参数
    prompt = request.form['prompt']
    original_text = request.form['original_text']

    # 调用API进行内容整理
    tokenizer = AutoTokenizer.from_pretrained("THUDM/chatglm-6b-int4", trust_remote_code=True)
    model = AutoModel.from_pretrained("THUDM/chatglm-6b-int4", trust_remote_code=True).half().cuda()
    model = model.eval()
    response, history = model.chat(tokenizer, original_text + prompt, history=[])

    # 返回大模型处理内容
    return jsonify({'summary_text': response, 'summary_text': response, 'conversationId': ''})



if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)
