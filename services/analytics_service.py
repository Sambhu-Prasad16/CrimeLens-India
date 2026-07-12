from sqlalchemy import extract, func

from models import db
from models.crime import Crime


def get_dashboard_data():

    total_crimes = Crime.query.count()

    total_states = db.session.query(
        Crime.state
    ).distinct().count()

    total_districts = db.session.query(
        Crime.district
    ).distinct().count()

    total_loss = db.session.query(
        func.sum(Crime.estimated_loss)
    ).scalar() or 0

    return {
        "total_crimes": total_crimes,
        "total_states": total_states,
        "total_districts": total_districts,
        "total_loss": total_loss
    }


def get_monthly_crime_data():

    results = (
        db.session.query(
            extract("month", Crime.fir_date).label("month"),
            func.count(Crime.id).label("count")
        )
        .group_by(extract("month", Crime.fir_date))
        .order_by(extract("month", Crime.fir_date))
        .all()
    )

    month_names = [
        "",
        "Jan", "Feb", "Mar", "Apr", "May", "Jun",
        "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
    ]

    labels = []
    values = []

    for month, count in results:
        labels.append(month_names[int(month)])
        values.append(count)

    return {
        "labels": labels,
        "values": values
    }