import pandas as pd
from datetime import datetime

from models import db
from models.crime import Crime


def load_crime_data(csv_file):

    df = pd.read_csv(csv_file)

    inserted = 0
    skipped = 0

    for _, row in df.iterrows():

        # Skip duplicate Crime IDs
        existing = Crime.query.filter_by(
            crime_id=row["Crime_ID"]
        ).first()

        if existing:
            skipped += 1
            continue

        crime = Crime(

            crime_id=row["Crime_ID"],

            fir_date=datetime.strptime(
                row["FIR_Date"],
                "%Y-%m-%d"
            ).date(),

            fir_time=row["FIR_Time"],

            state=row["State"],
            district=row["District"],
            police_station=row["Police_Station"],

            crime_category=row["Crime_Category"],
            crime_subcategory=row["Crime_Subcategory"],

            severity=row["Severity"],

            victim_age=int(row["Victim_Age"]),
            victim_gender=row["Victim_Gender"],

            suspect_age=int(row["Suspect_Age"]),
            suspect_gender=row["Suspect_Gender"],

            weapon_used=row["Weapon_Used"],

            arrest_status=row["Arrest_Status"],

            case_status=row["Case_Status"],

            latitude=float(row["Latitude"]),
            longitude=float(row["Longitude"]),

            estimated_loss=int(row["Estimated_Loss_INR"]),

            description=row["Crime_Description"]

        )

        db.session.add(crime)
        inserted += 1

    db.session.commit()

    print(f"Inserted : {inserted}")
    print(f"Skipped  : {skipped}")