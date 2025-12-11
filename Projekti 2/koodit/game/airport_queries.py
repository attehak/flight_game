import random
from app import db

def get_random_large_airport(country_code):
    sql = (
        "SELECT name, iso_country "
        "FROM airport "
        "WHERE iso_country = %s AND type = 'large_airport'"
    )

    cursor = db.cursor()
    cursor.execute(sql, (country_code,))
    data = cursor.fetchall()

    if not data:
        return None

    return random.choice(data)
