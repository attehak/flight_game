import random
from database import db

def get_random_large_airport(country_code):
    sql = "SELECT name, iso_country FROM airport WHERE iso_country = %s AND type = 'large_airport'"
    cursor = db.cursor()
    cursor.execute(sql, (country_code,))
    data = cursor.fetchall()
    return random.choice(data) if data else None
