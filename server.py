from flask import Flask, render_template, redirect, request, session
import csv

app = Flask(__name__)


@app.route('/')
def route_index():
    return render_template('list.html')


@app.route('/story')
def route_edit():
    return render_template('form.html')


@app.route('/save-story', methods=['POST'])
def route_save():
     print('POST request received!')
     headers = ["id", "title", "story", "accept", "value", "time", "status"]
     
     #with open("datas.csv", "a", newline='') as csvfile:

     return redirect('/')


if __name__ == "__main__":
  app.secret_key = 'my_secret_key'  # Change the content of this string
  app.run(
      debug=True,  # Allow verbose error reports
      port=5000  # Set custom port
  )
