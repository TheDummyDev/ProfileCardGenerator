from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form.get('name')
        user_id = request.form.get('user_id')
        email = request.form.get('email')
        return render_template('index.html', name=name, user_id=user_id, email=email)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
