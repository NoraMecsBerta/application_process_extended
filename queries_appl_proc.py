import common_appl_proc


@common_appl_proc.connection_handler
def read_mentors_and_schools(cursor):
    cursor.execute(
        '''SELECT mentors.first_name, mentors.last_name, schools.name AS school_name, schools.country 
        FROM mentors
        JOIN schools ON mentors.city=schools.city
        ORDER BY mentors.id;'''
        )
    mentors_and_schools = cursor.fetchall()
    return mentors_and_schools


@common_appl_proc.connection_handler
def read_all_schools_and_mentors(cursor):
    cursor.execute(
        '''SELECT COALESCE (mentors.first_name, 'No data') AS first_name, COALESCE (mentors.last_name, 'No data') AS last_name, schools.name AS school_name, schools.country
        FROM mentors
        RIGHT OUTER JOIN schools ON mentors.city=schools.city
        ORDER BY mentors.id;'''
        )
    all_schools_and_mentors = cursor.fetchall()
    print(all_schools_and_mentors)
    return all_schools_and_mentors


@common_appl_proc.connection_handler
def read_mentors_by_country(cursor):
    cursor.execute(
        '''SELECT schools.country, COUNT(mentors.id)
        FROM mentors
        JOIN schools ON mentors.city=schools.city
        GROUP BY schools.country
        ORDER BY schools.country;'''
        )
    mentors_by_countries = cursor.fetchall()
    return mentors_by_countries


@common_appl_proc.connection_handler
def read_contacts_and_schools(cursor):
    cursor.execute(
        '''SELECT schools.name, mentors.first_name, mentors.last_name
        FROM schools
        JOIN mentors ON schools.contact_person=mentors.id
        ORDER BY schools.name;'''
        )
    contacts_and_schools = cursor.fetchall()
    return contacts_and_schools


@common_appl_proc.connection_handler
def read_applicants(cursor):
    cursor.execute(
        '''SELECT applicants.first_name, applicants.application_code, applicants_mentors.creation_date
        FROM applicants
        JOIN applicants_mentors ON applicants.id=applicants_mentors.applicant_id
        WHERE applicants_mentors.creation_date < '2016-01-01'
        ORDER BY applicants_mentors.creation_date DESC;'''
        )
    applicants = cursor.fetchall()
    return applicants


@common_appl_proc.connection_handler
def read_applicants_and_mentors(cursor):
    cursor.execute(
        '''SELECT applicants.first_name AS applicants_name, applicants.application_code, COALESCE(mentors.first_name, 'No data') AS first_name, COALESCE(mentors.last_name, 'No data') AS last_name
        FROM applicants
        LEFT OUTER JOIN applicants_mentors ON applicants.id=applicants_mentors.applicant_id
        LEFT OUTER JOIN mentors ON applicants_mentors.mentor_id=mentors.id
        ORDER BY applicants.id;'''
        )
    applicants_and_mentors = cursor.fetchall()
    return applicants_and_mentors
