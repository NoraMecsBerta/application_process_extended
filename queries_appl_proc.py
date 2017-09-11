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
        '''SELECT mentors.first_name, mentors.last_name, schools.name AS school_name, schools.country
        FROM mentors
        RIGHT OUTER JOIN schools ON mentors.city=schools.city
        ORDER BY mentors.id;'''
        )
    all_schools_and_mentors = cursor.fetchall()
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
