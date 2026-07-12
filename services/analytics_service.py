from sqlalchemy import extract, func
from sqlalchemy import or_
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

def get_top_states():

    results = (
        db.session.query(
            Crime.state,
            func.count(Crime.id)
        )
        .group_by(Crime.state)
        .order_by(func.count(Crime.id).desc())
        .limit(10)
        .all()
    )

    return {
        "labels": [r[0] for r in results],
        "values": [r[1] for r in results]
    }

def get_crime_categories():

    results = (
        db.session.query(
            Crime.crime_category,
            func.count(Crime.id)
        )
        .group_by(Crime.crime_category)
        .all()
    )

    return {
        "labels": [r[0] for r in results],
        "values": [r[1] for r in results]
    }

def get_arrest_status():

    results = (
        db.session.query(
            Crime.arrest_status,
            func.count(Crime.id)
        )
        .group_by(Crime.arrest_status)
        .all()
    )

    return {
        "labels": [r[0] for r in results],
        "values": [r[1] for r in results]
    }

def get_filter_options():

    states = [
        row[0]
        for row in db.session.query(Crime.state)
        .distinct()
        .order_by(Crime.state)
        .all()
    ]

    categories = [
        row[0]
        for row in db.session.query(Crime.crime_category)
        .distinct()
        .order_by(Crime.crime_category)
        .all()
    ]

    arrest_status = [
        row[0]
        for row in db.session.query(Crime.arrest_status)
        .distinct()
        .order_by(Crime.arrest_status)
        .all()
    ]

    return {
        "states": states,
        "categories": categories,
        "arrest_status": arrest_status
    }


def get_recent_crimes(limit=20):

    crimes = (
        Crime.query
        .order_by(Crime.fir_date.desc())
        .limit(limit)
        .all()
    )

    data = []

    for crime in crimes:

        data.append({

            "crime_id": crime.crime_id,

            "date": crime.fir_date.strftime("%d-%m-%Y"),

            "state": crime.state,

            "district": crime.district,

            "category": crime.crime_category,

            "status": crime.case_status,

            "arrest": crime.arrest_status,

            "loss": crime.estimated_loss

        })

    return data

def apply_filters(query, state=None, category=None, arrest=None):

    if state:
        query = query.filter(Crime.state == state)

    if category:
        query = query.filter(Crime.crime_category == category)

    if arrest:
        query = query.filter(Crime.arrest_status == arrest)

    return query

def get_dashboard_data(state=None, category=None, arrest=None):

    query = build_query(state, category, arrest)

    total_crimes = query.count()

    total_loss = query.with_entities(
        func.sum(Crime.estimated_loss)
    ).scalar() or 0

    total_states = query.with_entities(
        Crime.state
    ).distinct().count()

    total_districts = query.with_entities(
        Crime.district
    ).distinct().count()

    return {
        "total_crimes": total_crimes,
        "total_states": total_states,
        "total_districts": total_districts,
        "total_loss": total_loss
    }


def build_query(state=None, category=None, arrest=None):
    query = Crime.query

    if state:
        query = query.filter(Crime.state == state)

    if category:
        query = query.filter(Crime.crime_category == category)

    if arrest:
        query = query.filter(Crime.arrest_status == arrest)

    return query