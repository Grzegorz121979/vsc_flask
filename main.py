from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def start():
    numbers = range(1, 121)
    return render_template('index.html', numbers=numbers)

@app.route('/submit', methods=['POST'])
def calculate_bmi():
    try:
        weight = request.form['weight_input']
        height = request.form['height_input']
        weight_input = float(weight)
        height_input = float(height)
        selected_option = request.form.get('radio_button')
        result_men = round(weight_input / (height_input / 100) ** 2, 2)
        result_women = round(weight_input / (height_input / 100) ** 2, 2)
        if selected_option == 'men_value':
            return render_template('index.html', result_men=result_men)
        elif selected_option == 'women_value':
            return render_template('index.html', result_women=result_women)
        else:
            error = 'Select field Man or Women'
            return render_template('index.html', error=error)
    except ValueError:
        error = 'All position should be fill'
        return render_template('index.html', error=error)

if __name__ == '__main__':
    app.run(debug=True)
