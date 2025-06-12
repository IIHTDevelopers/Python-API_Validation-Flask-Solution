from flask import Flask, request, jsonify

app = Flask(__name__)
JOBS = {"123": "RUNNING", "124": "SUCCESS"}

@app.route("/status")
def status():
    job_id = request.args.get("job_id")
    if not job_id:
        return jsonify({"error": "Missing 'job_id' in query parameters"}), 400
    if job_id not in JOBS:
        return jsonify({"error": f"No job found with job_id '{job_id}'"}), 400
    return jsonify({"job_id": job_id, "state": JOBS[job_id]})


@app.route("/submit", methods=["POST"])
def submit():
    if not request.is_json:
        return jsonify({"error": "Request must be in JSON format"}), 400

    payload = request.get_json()
    job_id = payload.get("job_id")
    if not job_id:
        return jsonify({"error": "Missing 'job_id' in JSON payload"}), 400

    JOBS[job_id] = "PENDING"
    return jsonify({"msg": "job submitted", "job_id": job_id}), 201


@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Internal Server Error", "details": str(error)}), 500


if __name__ == "__main__":
    app.run(debug=True)
