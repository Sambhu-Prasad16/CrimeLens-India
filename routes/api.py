from flask import Blueprint, jsonify
from services.analytics_service import get_monthly_crime_data

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