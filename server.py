from flask import Flask, render_template, request, redirect, url_for
import csv
app = Flask(__name__)


@app.route('/story', methods=['GET'])
def index(story_id=None):
    return render_template('form.html', story_id=story_id)


@app.route('/story', methods=['POST'])
def add_to_database():
    request_list = ['story_title',
                    'user_story',
                    'acceptance_criteria',
                    'business_value',
                    'estimation',
                    'select']
    new_data_list = [create_id()]
    for name in request_list:
        new_data_list.append(request.form[name])
    with open('database.csv', 'a') as database:
        database.write(';'.join(new_data_list))
        database.write('\n')
    return render_template('form.html')


def create_id():
    database = read_database()
    id_list = [row[0] for row in database]
    new_id = int(max(id_list)) + 1
    return str(new_id)


def read_database():
    with open('database.csv') as database:
        row = database.readlines()
        elements = [item.split(';') for item in row]
        return elements


@app.route('/list', methods=['GET'])
def display_table():
    table_titles = ['ID',
                    'Story Title',
                    'User Story',
                    'Acceptance Criteria',
                    'Business Value',
                    'Estimation',
                    'Status',
                    'Edit',
                    'Delete']
    data_in_database = read_database()
    return render_template('list.html', table_titles=table_titles, data_in_database=data_in_database)


@app.route('/delete', methods=['POST'])
def delete_story():
    datalist = read_database()
    id_to_delete = str(request.form['delete'])
    for line in datalist:
        if line[0] == id_to_delete:
            datalist.remove(line)
    with open('database.csv', 'w') as database:
        for item in datalist:
            line = [element.strip('\n') for element in item]
            writeable_line = ';'.join(line)
            database.write(writeable_line)
            database.write('\n')
    return redirect(url_for('display_table'))


@app.route('/story/<story_id>', methods=['POST'])
def update_story(story_id=None):
    update_list = []
    database = read_database()
    for line in database:
        if line[0] == story_id:
            for item in line:
                update_list.append(item)
    return render_template('form.html', story_id=story_id, update_list=update_list)


if __name__ == '__main__':
    app.run(debug=True)
