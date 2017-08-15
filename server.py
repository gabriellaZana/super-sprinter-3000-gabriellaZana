from flask import Flask, render_template, redirect, request, session
import csv
import sys


app = Flask(__name__)
id_pos = None
edit = None


def datas_reader():
    with open("datas.csv", "r") as csvfile:
        reader = csv.reader(csvfile)
        datas_list = list(reader)
    return datas_list


@app.route('/')
def route_index():
    global id_pos
    datas_list = datas_reader()
    if datas_list:
        id_pos = int(datas_list[-1][0])
    elif not datas_list:
        id_pos = 0
    return render_template('list.html', datas_list=datas_list)


@app.route('/list')
def route_list():
    return route_index()


@app.route('/delete/<id>')
def route_delete(id=None):
    datas_list = datas_reader()
    id_pos = int(id)
    for line in datas_list:
        if id_pos == int(line[0]):
            datas_list[id_pos-1].append("deleted")
    with open("datas.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(datas_list)
    return redirect('/')


@app.route('/story')
def route_edit():
    global id_pos
    global edit
    edit = False
    if id_pos is None:
        id_pos = 1
    else:
        id_pos += 1
    return render_template('form.html', id_pos=id_pos, edit=edit)


@app.route('/save-story', methods=['POST'])
def route_save():
    print('POST request received!')
    global id_pos
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


@app.route('/edit-story/<id>', methods=['POST'])
def route_edit_story(id=None):
    id_pos = int(id)
    datas_list = datas_reader()
    if request.method == 'POST':
                        title = request.form['title']
                        story = request.form['story']
                        accept = request.form['accept']
                        value = request.form['value']
                        time = request.form['time']
                        status = request.form['status']
                        id_ = request.form.get("id_")
                        fieldnames = ["id_", "title", "story", "accept", "value", "time", "status"]
    for line in datas_list:
        print(line[0])
        if id_pos == int(line[0]):
            datas_list[id_pos-1] = [id_, title, story, accept, value, time, status]
    with open("datas.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(datas_list)
    return redirect('/')


@app.route('/story/<id>')
def route_story_id(id=None):
    id_pos = int(id)
    global edit
    edit = True
    datas_list = datas_reader()
    edit_data_list = (datas_list[id_pos-1])
    fieldnames = ["id_", "title", "story", "accept", "value", "time", "status"]
    return render_template('form.html', id_pos=id_pos, edit=edit, edit_data_list=edit_data_list, fieldname=fieldnames)


if __name__ == "__main__":
    app.secret_key = 'my_secret_key'  # Change the content of this string
    app.run(
        debug=True,  # Allow verbose error reports
        port=5000  # Set custom post
        )
