from flask import Flask, render_template, request, redirect
import csv
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def page(page_name):
    return render_template(page_name)


def write_to_file(data):
    with open("database.txt",'a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'\n{email}, {subject}, {message}')

def write_to_csv(data):
    with open("database2.csv", newline ='', mode = 'a') as database2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        writer = csv.writer(database2, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        writer.writerow([email,subject,message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit():
    if request.method == 'POST':
        data = request.form.to_dict()
        # write_to_file(data)
        write_to_csv(data)
        return redirect('/thanks.html')
    else:
        return ' Something went wrong. Please try again'
    

