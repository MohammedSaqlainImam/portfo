from flask import Flask, render_template, request, redirect, url_for, flash
import os
import csv
app = Flask(__name__)
app.secret_key = 'secrect_key'

@app.route("/")
def index():
    return render_template('index.html')


def write_to_file(data):
    with open('database.txt', mode='a') as database:
        Name = data["name"]
        Email = data["email"]
        Subject = data["subject"]
        Message = data["message"]
        file = database.write(f'\n{Name},{Email},{Subject},{Message}')

def write_to_csv(data):
    file_exists = os.path.isfile('database.csv')
    write_header = not file_exists or os.path.getsize('database.csv') ==0 
    with open('database.csv', mode='a', newline='') as database2:
        csv_writer = csv.writer(database2, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        if write_header:
            csv_writerow([Name,Email,Subject,Message])
        Name = data["name"]
        Email = data["email"]
        Subject = data["subject"]
        Message = data["message"]
        csv_writer.writerow([Name,Email,Subject,Message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        print(data)
        write_to_csv(data)
        flash('Thank You, Will contact you shortly!')
        return redirect(url_for('index') + '#contact')
    else:
        flash('Something went wrong. Please try again.')
        return redirect(url_for('index') + '#contact')