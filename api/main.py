from flask import Flask
from flask_cors import CORS
import requests
import os

app = Flask(__name__)
CORS(app)  # 添加这一行来启用CORS

@app.route('/api/main.py')
def get_data():
    try:
        headers = {
            'Authorization': f'Bearer {os.environ.get("NOTION_TOKEN")}',
            'Notion-Version': '2021-05-13'
        }
        response = requests.post(f'https://api.notion.com/v1/databases/{os.environ.get("NOTION_DATABASE_ID")}/query', headers=headers)
        return response.json()
    except Exception as e:
        print(e)
        return 'Error', 500

if __name__ == '__main__':
    app.run()
