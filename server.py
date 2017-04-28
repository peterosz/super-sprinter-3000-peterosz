from flask import Flask, render_template, request
import csv
app = Flask(__name__)


@app.route('/story', methods=['GET'])
def index():
    return render_template('form.html')


@app.route('/story', methods=['POST'])
def add_to_database():
    story_title = request.form['story_title']
    user_story = request.form['user_story']
    acceptance_criteria = request.form['acceptance_criteria']
    business_value = request.form['business_value']
    estimation = request.form['estimation']
    select = request.form['select']
    new_data_list = [create_id(), story_title, user_story, acceptance_criteria, business_value, estimation, select]
    with open('database.csv', 'a') as database:
        database.write(';'.join(new_data_list))
        database.write('\n')
    return render_template('form.html',
                           story_title=story_title,
                           user_story=user_story,
                           acceptance_criteria=acceptance_criteria,
                           business_value=business_value,
                           estimation=estimation,
                           select=select)


def create_id():
    with open('database.csv') as database:
        row_count = 0
        for row in database:
            row_count += 1
        return str(row_count + 1)


def read_database():
    with open('database.csv') as database:
        


def display_table():
    pass


if __name__ == '__main__':
    app.run(debug=True)
