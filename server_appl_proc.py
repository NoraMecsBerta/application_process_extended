from flask import Flask, render_template, redirect, request
#import data_manager
import queries_appl_proc
from datetime import datetime


app = Flask(__name__)


@app.route('/')
def route_index():
    return render_template('index_appl_proc.html')


@app.route('/mentors')
def mentors_school_list():
    mentors_and_schools = queries_appl_proc.read_mentors_and_schools()
    print(mentors_and_schools) #
    return render_template('mentors.html', mentors_and_schools=mentors_and_schools)


@app.route('/all-school')
def all_shool_list():
    all_schools_and_mentors = queries_appl_proc.read_all_schools_and_mentors()
    return render_template('all-school.html', all_schools_and_mentors=all_schools_and_mentors)


@app.route('/mentors-by-country')
def mentors_by_country():
    mentors_by_countries = queries_appl_proc.read_mentors_by_country()
    return render_template('mentors-by-country.html', mentors_by_countries=mentors_by_countries)

'''
@app.route('/mentors-by-country')
def mentorby_country():
    mentors_by_countries = queries_appl_proc.read_all_schools_and_mentors()
    return render_template('all-school.html', all_schools_and_mentors=all_schools_and_mentors)
'''

if __name__ == '__main__':
    app.secret_key = 'dojo'
    app.run(
        debug=True,  # Allow verbose error reports
        port=5000  # Set custom port
    )


