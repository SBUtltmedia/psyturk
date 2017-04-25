from flask import Flask
from flask import render_template, url_for, request, make_response

app = Flask(__name__)


AMAZON_HOST =  "https://workersandbox.mturk.com/mturk/externalSubmit"

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.args.get("assignmentId") == "ASSIGHMENT_ID_NOT_AVAILABLE":
        pass
    else:
        pass

    render_data = {
            "worker_id": request.args.get("workerId"),
            "assignment_id": request.args.get("assignmentId"),
            "amazon_host": AMAZON_HOST,
            "hit_id": request.args.get("hitId"),
            "some_info_to_pass": request.args.get("someInfoToPass")
            }
    resp = make_response(render_template("index.htm", name=render_data))
    print resp
    return resp 


if __name__ == "__main__":
    app.debug = DEBUG
    app.run() 
