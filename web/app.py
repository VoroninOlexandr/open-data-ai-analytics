import os
import pandas as pd
from flask import Flask, render_template
from sqlalchemy import create_engine

app = Flask(__name__)


DB_USER = os.getenv('DB_USER', 'admin')
DB_PASS = os.getenv('DB_PASS', 'secretpassword')
DB_HOST = os.getenv('DB_HOST', 'db')
DB_NAME = os.getenv('DB_NAME', 'beer_db')

def get_db_connection():
    engine = create_engine(f'postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:5432/{DB_NAME}')
    return engine

def read_text_file(filepath):

    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    return "Звіт ще не згенеровано або файл не знайдено."

@app.route('/')
def index():

    try:
        engine = get_db_connection()
        df = pd.read_sql("SELECT * FROM beer_data LIMIT 10", engine)
        data_html = df.to_html(classes="table table-striped", index=False)
    except Exception as e:
        data_html = f"<p class='text-danger'>Помилка підключення до БД: {e}</p>"


    quality_report = read_text_file('/app/reports/quality_report.txt')
    research_report = read_text_file('/app/reports/research_report.txt')


    plots = []
    plot_dir = '/app/static/plots'
    if os.path.exists(plot_dir):

        plots = [f"plots/{file}" for file in os.listdir(plot_dir) if file.endswith('.png')]

    return render_template('index.html',
                           data_table=data_html,
                           quality_report=quality_report,
                           research_report=research_report,
                           plots=plots)

if __name__ == '__main__':

    app.run(host='0.0.0.0', port=5000, debug=True)