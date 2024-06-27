from blueprints.users.users_db_ops import get_user_by_id
from blueprints.posts.posts_db_ops import get_post_by_id


def validate_create_post_inputs(request_json):
    if "user_id" in request_json and "content" in request_json:
        if not request_json["user_id"].isdigit():
            raise Exception("User id must be int !")
        if get_user_by_id(request_json["user_id"]) is None:
            raise Exception("User not found !")
    else:
        raise Exception("Missing data !")


def validate_update_post_inputs(request_json):
    if "post_id" in request_json and "content" in request_json:
        if not request_json["post_id"].isdigit():
            raise Exception("Post id must be int !")
        if get_post_by_id(request_json["post_id"]) is None:
            raise Exception("Post not found !")
    else:
        raise Exception("Missing data !")


def validate_delete_post_inputs(post_id):
    if not post_id.isdigit():
        raise Exception("Post id must be int !")
    if get_post_by_id(post_id) is None:
        raise Exception("Post not found !")


def validate_get_post_inputs(post_id):
    if not post_id.isdigit():
        raise Exception("Post id must be int !")
    if get_post_by_id(post_id) is None:
        raise Exception("Post not found !")
