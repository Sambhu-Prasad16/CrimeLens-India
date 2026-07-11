from flask import Blueprint, render_template
from services.analytics_service import get_dashboard_data

dashboard_bp = Blueprint("dashboard", __name__)


@dashboard_bp.route("/")
def dashboard():

    data = get_dashboard_data()

    return render_template(
        "dashboard.html",
        **data
    )