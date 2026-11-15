"""Northstar local training service with defensive regression controls.

This app is intentionally small and uses synthetic identities for local tests only.
It is not a production authentication implementation.
"""
from flask import Flask, jsonify, request, session


def create_app(test_config=None):
    app = Flask(__name__)
    app.config.update(
        SECRET_KEY="local-training-key-change-before-any-deployment",
        SESSION_COOKIE_HTTPONLY=True,
        SESSION_COOKIE_SAMESITE="Lax",
        SESSION_COOKIE_SECURE=False,  # localhost HTTP training only
    )
    if test_config:
        app.config.update(test_config)

    @app.after_request
    def add_security_headers(response):
        response.headers.setdefault("X-Content-Type-Options", "nosniff")
        response.headers.setdefault("X-Frame-Options", "DENY")
        response.headers.setdefault("Referrer-Policy", "no-referrer")
        response.headers.setdefault("Content-Security-Policy", "default-src 'self'; frame-ancestors 'none'")
        response.headers.setdefault("Cache-Control", "no-store")
        return response

    @app.get("/health")
    def health():
        return jsonify({"status": "ok", "service": "northstar-training"})

    @app.post("/profile")
    def profile():
        payload = request.get_json(silent=True)
        if not isinstance(payload, dict):
            return jsonify({"error": "JSON object required"}), 400
        allowed_fields = {"display_name"}
        if set(payload) - allowed_fields:
            return jsonify({"error": "unexpected field"}), 400
        display_name = payload.get("display_name", "")
        if not isinstance(display_name, str):
            return jsonify({"error": "display_name must be text"}), 400
        display_name = display_name.strip()
        if len(display_name) > 80:
            return jsonify({"error": "display_name too long"}), 400
        return jsonify({"display_name": display_name})

    # Synthetic login route for local role-based access-control regression tests.
    # Do not reuse this demonstration pattern as production authentication.
    @app.post("/login/<role>")
    def login(role):
        if role not in {"user", "admin"}:
            return jsonify({"error": "unknown training role"}), 400
        session.clear()
        session["role"] = role
        return jsonify({"authenticated": True, "role": role})

    @app.post("/logout")
    def logout():
        session.clear()
        return jsonify({"authenticated": False})

    @app.get("/account")
    def account():
        if session.get("role") not in {"user", "admin"}:
            return jsonify({"error": "authentication required"}), 401
        return jsonify({"account": "training-user", "role": session["role"]})

    @app.get("/admin")
    def admin():
        if session.get("role") is None:
            return jsonify({"error": "authentication required"}), 401
        if session.get("role") != "admin":
            return jsonify({"error": "forbidden"}), 403
        return jsonify({"admin": True, "message": "training admin area"})

    return app


app = create_app()

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)
