from flask import Flask, request, jsonify

app = Flask(__name__)
JOBS = {"123": "RUNNING", "124": "SUCCESS"}

@app.route("/status")
def status():
    job_id = request.args.get("job_id")
    state = JOBS[job_id]  # KeyError if missing
    return jsonify({"job_id": job_id, "state": state})

@app.route("/submit", methods=["POST"])
def submit():
    payload = request.json
    job_id = payload["job_id"]  # KeyError if missing
    JOBS[job_id] = "PENDING"
    return jsonify({"msg": "job submitted"}), 201

if __name__ == "__main__":
    app.run(debug=True)
