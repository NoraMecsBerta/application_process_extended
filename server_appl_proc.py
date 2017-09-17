from flask import Flask, render_template, redirect, request
import queries_appl_proc
from datetime import datetime


app = Flask(__name__)


@app.route('/')
def route_index():
    return render_template('index_appl_proc.html')


@app.route('/mentors')
def mentors_school_list():
    mentors_and_schools = queries_appl_proc.read_mentors_and_schools()
    actual_keys = ['first_name', 'last_name', 'school_name', 'country']
    return render_template('mentors.html', list=mentors_and_schools, actual_keys=actual_keys)


@app.route('/all-school')
def all_shool_list():
    all_schools_and_mentors = queries_appl_proc.read_all_schools_and_mentors()
    actual_keys = ['first_name', 'last_name', 'school_name', 'country']
    return render_template('all-school.html', list=all_schools_and_mentors, actual_keys=actual_keys)


@app.route('/mentors-by-country')
def mentors_by_country():
    mentors_by_countries = queries_appl_proc.read_mentors_by_country()
    actual_keys = ['country', 'count']
    return render_template('mentors-by-country.html', list=mentors_by_countries, actual_keys=actual_keys)


@app.route('/contacts')
def contacts():
    contacts_and_schools = queries_appl_proc.read_contacts_and_schools()
    actual_keys = ['name', 'first_name', 'last_name']
    return render_template('contacts.html', list=contacts_and_schools, actual_keys=actual_keys)


@app.route('/applicants')
def applicants_data():
    applicants = queries_appl_proc.read_applicants()
    actual_keys = ['first_name', 'application_code', 'creation_date']
    return render_template('applicants.html', list=applicants, actual_keys=actual_keys)


@app.route('/applicants-and-mentors')
def applicants_with_mentors():
    applicants_and_mentors = queries_appl_proc.read_applicants_and_mentors()
    actual_keys = ['applicants_name', 'application_code', 'first_name', 'last_name']
    return render_template('applicants-and-mentors.html', list=applicants_and_mentors, actual_keys=actual_keys)


if __name__ == '__main__':
    app.secret_key = 'dojo'
    app.run(
        debug=True,  # Allow verbose error reports
        port=5000  # Set custom port
    )


