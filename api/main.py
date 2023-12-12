from flask import Flask
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)  # 添加这一行来启用CORS

@app.route('/api/main.py')
def get_data():
    try:
        headers = {
            'Authorization': 'Bearer secret_FuF38QkizWL5lgsK8oQd6IhjX4jVKa4mywyfag6HtJr',
            'Notion-Version': '2021-05-13'
        }
        response = requests.post('https://api.notion.com/v1/databases/e649801ccfa24c59b903148531d60783/query', headers=headers)
        return response.json()
    except Exception as e:
        print(e)
        return 'Error', 500

if __name__ == '__main__':
    app.run()
