from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def start():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def calculate_bmi():
    try:
        weight = request.form['weight_input']
        height = request.form['height_input']
        weight_input = float(weight)
        height_input = float(height)
        result = round(weight_input / height_input ** 2, 2)
        return render_template('index.html', result=result)
    except ValueError:
        error = 'Only numbers'
        return render_template('index.html', error=error)
    except KeyError:
        error = 'All position should be fill'
        return render_template('index.html', error=error)

if __name__ == '__main__':
    app.run(debug=True)
