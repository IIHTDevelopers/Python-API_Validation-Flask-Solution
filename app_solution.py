from flask import Flask, request, jsonify, abort

app = Flask(__name__)
JOBS = {"123": "RUNNING", "124": "SUCCESS"}

@app.route("/status")
def status():
    job_id = request.args.get("job_id")
    if not job_id:
        abort(400, description="Missing required query parameter: job_id")
    if job_id not in JOBS:
        abort(400, description=f"No job found with job_id: {job_id}")

    state = JOBS[job_id]
    return jsonify({"job_id": job_id, "state": state})

@app.route("/submit", methods=["POST"])
def submit():
    if not request.is_json:
        abort(400, description="Request must be in JSON format")

    payload = request.get_json()
    job_id = payload.get("job_id")

    if not job_id:
        abort(400, description="Missing required field: job_id")

    JOBS[job_id] = "PENDING"
    return jsonify({"msg": "Job submitted"}), 201

# Global error handler for 400 errors
@app.errorhandler(400)
def bad_request(error):
    return jsonify({"error": "Bad Request", "message": error.description}), 400

if __name__ == "__main__":
    app.run(debug=True)
