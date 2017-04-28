from flask import Flask, render_template, request
import csv
app = Flask(__name__)


@app.route('/story', methods=['GET'])
def index():
    return render_template('form.html')


@app.route('/story', methods=['POST'])
def add_to_database():
    sotry_title = request.form['sotry_title']
    user_story = request.form['user_story']
    acceptance_criteria = request.form['acceptance_criteria']
    business_value = request.form['business_value']
    estimation = request.form['estimation']
    select = request.form['select']
    new_data_list = [create_id(), story_title, user_story, acceptance_criteria, business_value, estimation, select]
    with open(database.csv, 'a') as database:
        database.write(new_data_list.split(';'))
    return render_template('form.html',
                           story_title=story_title,
                           user_story=user_story,
                           acceptance_criteria=acceptance_criteria,
                           business_value=business_value,
                           estimation=estimation,
                           select=select)


def create_id():
    with open(database.csv) as database:
        row_count = 0
        for row in readlines(database):
            row_count += 1
        return row_count + 1


if __name__ == '__main__':
    app.run(debug=True)
