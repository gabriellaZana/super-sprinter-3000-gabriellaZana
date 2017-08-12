from flask import Flask, render_template, redirect, request, session
import csv

app = Flask(__name__)


@app.route('/')
def route_index():
    with open("datas.csv", "r") as csvfile:
        reader = csv.reader(csvfile)
        datas_list = list(reader)
    print(datas_list)
    return render_template('list.html', datas_list=datas_list)


@app.route('/story')
def route_edit():
    return render_template('form.html')


@app.route('/save-story', methods=['POST'])
def route_save():
    print('POST request received!')
    if request.method == 'POST':
        title = request.form['title']
        story = request.form['story']
        accept = request.form['accept']
        value = request.form['value']
        time = request.form['time']
        status = request.form['status']
        fieldnames = ["title", "story", "accept", "value", "time", "status"]
        with open("datas.csv", "a") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow({'title': title, 'story': story, 'accept': accept, 'value': value, 'time': time, 'status': status})
    return redirect('/')


if __name__ == "__main__":
    app.secret_key = 'my_secret_key'  # Change the content of this string
    app.run(
        debug=True,  # Allow verbose error reports
        port=5000  # Set custom port
  )
