from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
from pymongo import MongoClient

app = Flask(__name__)
CORS(app)

# --- MongoDB connection ---
client = MongoClient("mongodb://localhost:27017/")
db = client["eco_router"]

# ---------- FRONTEND ROUTES ----------
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/routes_page")
def routes_page():
    return render_template("routes.html")

@app.route("/road_segments_page")
def road_segments_page():
    return render_template("road_segments.html")

@app.route("/traffic_page")
def traffic_page():
    return render_template("traffic.html")

@app.route("/users_page")
def users_page():
    return render_template("users.html")

@app.route("/vehicles_page")
def vehicles_page():
    return render_template("vehicles.html")

# ---------- API ENDPOINTS ----------
@app.route("/routes", methods=["GET"])
def get_routes():
    routes = list(db.routes.find({}, {"_id": 0}))
    return jsonify(routes)

@app.route("/road_segments", methods=["GET"])
def get_road_segments():
    segments = list(db.road_segments.find({}, {"_id": 0}))
    return jsonify(segments)

@app.route("/traffic_conditions", methods=["GET"])
def get_traffic_conditions():
    traffic = list(db.traffic_conditions.find({}, {"_id": 0}))
    return jsonify(traffic)

@app.route("/users", methods=["GET"])
def get_users():
    users = list(db.users.find({}, {"_id": 0}))
    return jsonify(users)

@app.route("/vehicles", methods=["GET"])
def get_vehicles():
    vehicles = list(db.vehicles.find({}, {"_id": 0}))
    return jsonify(vehicles)

@app.route("/routes/<route_id>", methods=["GET"])
def get_route_by_id(route_id):
    route = db.routes.find_one({"routeId": route_id}, {"_id": 0})
    if route:
        return jsonify(route)
    return jsonify({"error": "Route not found"}), 404

# ---------- RUN ----------
if __name__ == "__main__":
    app.run(debug=True)
