from flask import Flask, render_template, request
from datetime import datetime
import csv
import os

app = Flask(__name__)


@app.route('/')
def start():
    with open('assets/data.txt', 'w', encoding='utf-8') as file:
        file.write("")
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def calculate_bmi():
    try:
        weight = request.form.get('weight_input')
        height = request.form.get('height_input')
        weight_input = float(weight)
        height_input = float(height)
        selected_option = request.form.get('radio_button')
        result_man = round(weight_input / (height_input / 100) ** 2, 2)
        result_women = round(weight_input / (height_input / 100) ** 2, 2)

        with open("assets/data.txt", "w", encoding="utf-8") as file:
            file.write(weight + "\n")
            file.write(str(result_man) + "\n")

        if selected_option == 'man_value':
            return render_template('index.html', result_man=result_man)
        elif selected_option == 'women_value':
            return render_template('index.html', result_women=result_women)
        else:
            error = 'Select field Man or Women'
            return render_template('index.html', error=error)
    except ValueError:
        error = 'All position should be fill'
        return render_template('index.html', error=error)


@app.route('/save', methods=['POST'])
def save_data():
    date = datetime.now().strftime("%d/%m/%Y")
    with open("assets/data.txt", "r", encoding="utf-8") as file:
        lst = [line.strip() for line in file.readlines()]

    file_exists = os.path.exists("assets/output.csv")

    with open("assets/output.csv", "a", newline="", encoding="utf-8") as csv_file:
        header = ["Date", "Weight", "BMI"]
        writer = csv.DictWriter(csv_file, fieldnames=header)

        if not file_exists:
            writer.writeheader()

        writer.writerow({"Date": date, "Weight": (lst[0] + "kg"), "BMI": lst[1]})

        with open('assets/data.txt', 'w', encoding='utf-8') as file:
            file.write("")
    
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
