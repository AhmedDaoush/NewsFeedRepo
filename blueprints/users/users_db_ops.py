from db import get_db_connection


def get_user_by_id(user_id):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        get_user_query = """ 
        SELECT * 
        FROM users
        WHERE user_id = %s
        """
        cursor.execute(get_user_query, (user_id))
        conn.close()
        return cursor.fetchone()
    except Exception as exception:
        print(str(exception))
        return False
