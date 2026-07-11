from models import db


class Crime(db.Model):
    __tablename__ = "crimes"

    id = db.Column(db.Integer, primary_key=True)

    crime_id = db.Column(db.String(20), unique=True, nullable=False)

    fir_date = db.Column(db.Date, nullable=False)

    fir_time = db.Column(db.String(10))

    state = db.Column(db.String(100))
    district = db.Column(db.String(100))
    police_station = db.Column(db.String(150))

    crime_category = db.Column(db.String(100))
    crime_subcategory = db.Column(db.String(150))

    severity = db.Column(db.String(20))

    victim_age = db.Column(db.Integer)
    victim_gender = db.Column(db.String(20))

    suspect_age = db.Column(db.Integer)
    suspect_gender = db.Column(db.String(20))

    weapon_used = db.Column(db.String(100))

    arrest_status = db.Column(db.String(50))

    case_status = db.Column(db.String(100))

    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)

    estimated_loss = db.Column(db.Integer)

    description = db.Column(db.Text)

    def __repr__(self):
        return f"<Crime {self.crime_id}>"