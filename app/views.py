from flask import jsonify

def user_view(user):
    return jsonify(user.to_dict())
