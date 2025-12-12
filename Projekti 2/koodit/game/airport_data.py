import random
from database import db 

def get_random_large_airport(country_code):
    sql = (
        "SELECT name, iso_country, municipality "
        "FROM airport "
        "WHERE iso_country = %s AND type = 'large_airport'"
    )
    cursor = db.cursor()
    cursor.execute(sql, (country_code,))
    results = cursor.fetchall()

    if not results:
        return None

    return random.choice(results)