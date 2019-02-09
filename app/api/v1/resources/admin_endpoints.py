# from v1 import version_1

from app.api.v1 import version_1


def func(x):
    return x + 1


@version_1.route("/admin")
def index():
    return "Hello World!"







@version_1.route("/view-two/")
def view_two():
    return "Hello view two"





@version_1.route("/all-parties/")
def all_parties():
    return "All parties"