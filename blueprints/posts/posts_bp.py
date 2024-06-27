from flask import Blueprint, request
from blueprints.posts.posts_inputs_validation import *
from blueprints.posts.posts_db_ops import *
posts_bp = Blueprint("posts", __name__)


@posts_bp.route("/create", methods=["Post"])
def create():
    try:
        request_json = request.get_json()
        validate_create_post_inputs(request_json)
        create_post(**request_json)
        return "Post created !", 201
    except Exception as exception:
        return str(exception), 400


@posts_bp.route("/update", methods=["Put"])
def update():
    try:
        request_json = request.get_json()
        validate_update_post_inputs(request_json)
        update_post(**request_json)
        return "", 204
    except Exception as exception:
        return str(exception), 400


@posts_bp.route("/delete/<post_id>", methods=["Delete"])
def delete(post_id):
    try:
        validate_delete_post_inputs(post_id)
        delete_post(post_id)
        return "", 204
    except Exception as exception:
        return str(exception), 400


@posts_bp.route("/get/<post_id>", methods=["Get"])
def get(post_id):
    try:
        validate_get_post_inputs(post_id)
        return get_post_by_id(post_id), 200
    except Exception as exception:
        return str(exception), 400
