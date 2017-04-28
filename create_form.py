from flask import Flask, render_template, request
import csv
app = Flask(__name__)


@app.route('/story', methods=['GET', 'POST'])
def story():
    return render_template('form.html')

'''def open_database():
    with open(database.csv) as database:
        row = database.readlines('\n')
        items = item.split(';') for item in row
    return items'''


'''def create_id():
    items = open_database()
    row_count = 0
    for row in items:
        row_count += 1
    return row_count += 1'''


'''@app.route('/story')
def add_to_database(*args):
    new_id = 1
    new_line = [new_id, *args[1::]]
    with open(database.csv, 'a') as database:
        database.write(new_line)'''


if __name__ == '__main__':
    app.run(debug=True)
