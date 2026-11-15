"""Fictional sample service; deliberately simple for code-review practice."""
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.get("/health")
def health():
    return jsonify({"status": "ok", "service": "northstar-training"})

@app.post("/profile")
def profile():
    payload = request.get_json(silent=True) or {}
    # Training review prompt: validate input types, size and allowed fields.
    display_name = payload.get("display_name", "")
    if not isinstance(display_name, str):
        return jsonify({"error": "display_name must be text"}), 400
    if len(display_name) > 80:
        return jsonify({"error": "display_name too long"}), 400
    return jsonify({"display_name": display_name.strip()})
