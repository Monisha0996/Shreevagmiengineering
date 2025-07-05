from flask import Flask, render_template
from flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', active_page='home')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        # You can process/store/send the message here
        return render_template('contact.html', active_page='contact', success=True)
    return render_template('contact.html', active_page='contact')

@app.route('/about', methods= ['GET','POST'])
def about():
    return render_template('about.html', active_page='about')


@app.route('/services', methods= ['GET','POST'])
def services():
    return render_template('services.html', active_page='services')

if __name__ == '__main__':
    app.run(debug=True)
