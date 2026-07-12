from flask import Blueprint, jsonify
from services.analytics_service import (
    get_monthly_crime_data,
    get_top_states,
    get_crime_categories,
    get_arrest_status
)

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