from flask import Flask, request, jsonify
import pandas as pd

def classify_os(value):
    if "Windows" in str(value):
        return "Windows"
    elif "Linux" in str(value):
        return "Linux"
    elif "VMware" in str(value):
        return "VM"
    else:
        return "Other"

@app.route('/classify', methods=['POST'])
app = Flask(__name__)
@app.route('/')
def home():
    return '✅ UPAS 分類 API 已啟動，請使用 POST /classify 上傳 Excel。'
def classify():
    file = request.files['file']
    df = pd.read_excel(file)
    df['分類結果'] = df['OS'].apply(classify_os)
    return df.to_json(orient='records')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
