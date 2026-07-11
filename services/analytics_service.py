from sqlalchemy import func

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