from flask import Flask, render_template, redirect, request, session
import csv


app = Flask(__name__)
id_pos = None

@app.route('/')
def route_index():
    datas_list = []
    with open("datas.csv", "r") as csvfile:
        reader = csv.reader(csvfile)
        datas_list = list(reader)
    return render_template('list.html', datas_list=datas_list)


@app.route('/story')
def route_edit():
    global id_pos
    if id_pos is None:
        id_pos = 1
    else:
        id_pos += 1
    
    return render_template('form.html', id_pos=id_pos)


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
        id_ = request.form.get("id_")
        fieldnames = ["id_", "title", "story", "accept", "value", "time", "status"]
        with open("datas.csv", "a") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow({'id_': id_, 'title': title, 'story': story, 'accept': accept, 'value': value, 'time': time, 'status': status})
    return redirect('/')


if __name__ == "__main__":
    app.secret_key = 'my_secret_key'  # Change the content of this string
    app.run(
        debug=True,  # Allow verbose error reports
        port=5000  # Set custom port
  )
