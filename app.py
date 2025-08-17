from flask import Flask, jsonify, request
from flask_cors import CORS
from pymongo import MongoClient
from flask import render_template
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)  # Allow frontend to access backend
app.secret_key = os.getenv("SECRET_KEY") 
# --- MongoDB connection ---
client = MongoClient("mongodb://localhost:27017/")  # Local MongoDB
db = client["eco_router"]  # Database name (change if needed)

# ---------- API ENDPOINTS ----------

# 1. Get all routes
@app.route("/routes", methods=["GET"])
def get_routes():
    routes = list(db.routes.find({}, {"_id": 0}))
    return jsonify(routes)

# 2. Get all road segments
@app.route("/road_segments", methods=["GET"])
def get_road_segments():
    segments = list(db.road_segments.find({}, {"_id": 0}))
    return jsonify(segments)

# 3. Get all traffic conditions
@app.route("/traffic_conditions", methods=["GET"])
def get_traffic_conditions():
    traffic = list(db.traffic_conditions.find({}, {"_id": 0}))
    return jsonify(traffic)

# 4. Get all users
@app.route("/users", methods=["GET"])
def get_users():
    users = list(db.users.find({}, {"_id": 0}))
    return jsonify(users)

# 5. Get all vehicles
@app.route("/vehicles", methods=["GET"])
def get_vehicles():
    vehicles = list(db.vehicles.find({}, {"_id": 0}))
    return jsonify(vehicles)

# 6. Example: Get a specific route by ID
@app.route("/routes/<route_id>", methods=["GET"])
def get_route_by_id(route_id):
    route = db.routes.find_one({"routeId": route_id}, {"_id": 0})
    if route:
        return jsonify(route)
    return jsonify({"error": "Route not found"}), 404

@app.route("/")
def home():
    return render_template("index.html")

# ---------- RUN APP ----------
if __name__ == "__main__":
    app.run(debug=True)