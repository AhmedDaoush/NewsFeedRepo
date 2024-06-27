from db import get_db_connection


def create_post(user_id, content):
    conn = get_db_connection()
    cursor = conn.cursor()
    insert_post_query = """ INSERT INTO posts (
        user_id,
        content)
        VALUES(
        %s,
        %s
        );
        """
    cursor.execute(insert_post_query, (user_id, content))
    conn.commit()
    conn.close()


def update_post(post_id, content):
    conn = get_db_connection()
    cursor = conn.cursor()
    update_post_query = """ UPDATE posts
        SET
        content = %s
        WHERE post_id = %s;
        """
    cursor.execute(update_post_query, (content, post_id))
    conn.commit()
    conn.close()


def delete_post(post_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    delete_post_query = """ DELETE FROM posts
        WHERE post_id = %s;
        """
    cursor.execute(delete_post_query, (post_id))
    conn.commit()
    conn.close()


def get_post_by_id(post_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    get_post_query = """ select * FROM posts
        WHERE post_id = %s;
        """
    cursor.execute(get_post_query, (post_id))
    conn.commit()
    conn.close()
    return cursor.fetchone()
