from flask import Flask, render_template, redirect, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/<string:page_name>")
def page(page_name):
    return render_template(page_name)

def write_to_database(data):
    with open('database.txt', mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'\nemail:{email},\nsubject:{subject},\nmessage:{message}\n')

@app.route("/form_submitted", methods=['POST','GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_database(data)
        return redirect('/thankyou.html')
    else:
        return 'Something went wrong Try again'