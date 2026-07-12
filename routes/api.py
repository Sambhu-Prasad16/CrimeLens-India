from flask import Blueprint, jsonify, request
from services.analytics_service import (
    get_monthly_crime_data,
    get_top_states,
    get_crime_categories,
    get_arrest_status,
    get_filter_options,
    get_recent_crimes,
    get_dashboard_data
)
from models import db
from models.crime import Crime

api_bp = Blueprint(
    "api",
    __name__,
    url_prefix="/api"
)


@api_bp.route("/monthly-crimes")
def monthly_crimes():

    return jsonify(
        get_monthly_crime_data()
    )

@api_bp.route("/top-states")
def top_states():
    return jsonify(get_top_states())


@api_bp.route("/crime-categories")
def crime_categories():
    return jsonify(get_crime_categories())


@api_bp.route("/arrest-status")
def arrest_status():
    return jsonify(get_arrest_status())

@api_bp.route("/filters")
def get_filters():
    return jsonify(get_filter_options())

@api_bp.route("/recent-crimes")
def recent_crimes():
    return jsonify(get_recent_crimes())

@api_bp.route("/dashboard")
def dashboard_api():

    state = request.args.get("state")
    category = request.args.get("category")
    arrest = request.args.get("arrest")

    return jsonify(
        get_dashboard_data(
            state,
            category,
            arrest
        )
    )

@api_bp.route("/crime-map")
def crime_map():

    crimes = Crime.query.all()

    data = []

    for crime in crimes:

        if crime.latitude and crime.longitude:

            data.append({

                "crime_id": crime.crime_id,

                "state": crime.state,

                "district": crime.district,

                "category": crime.crime_category,

                "lat": crime.latitude,

                "lng": crime.longitude

            })

    return jsonify(data)