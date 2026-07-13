import pandas as pd
from datetime import datetime

from app import app
from models import db
from models.crime import Crime

CSV_FILE = "dataset/india_crime_dataset_2025.csv"

with app.app_context():

    db.create_all()

    if Crime.query.count() > 0:
        print("Database already populated.")
        exit()

    df = pd.read_csv(CSV_FILE)

    for _, row in df.iterrows():

        crime = Crime(
            crime_id=row["Crime_ID"],
            fir_date=datetime.strptime(row["FIR_Date"], "%Y-%m-%d").date(),
            fir_time=row["FIR_Time"],
            state=row["State"],
            district=row["District"],
            police_station=row["Police_Station"],
            crime_category=row["Crime_Category"],
            crime_subcategory=row["Crime_Subcategory"],
            severity=row["Severity"],
            victim_age=row["Victim_Age"],
            victim_gender=row["Victim_Gender"],
            suspect_age=row["Suspect_Age"],
            suspect_gender=row["Suspect_Gender"],
            weapon_used=row["Weapon_Used"],
            arrest_status=row["Arrest_Status"],
            case_status=row["Case_Status"],
            latitude=row["Latitude"],
            longitude=row["Longitude"],
            estimated_loss=row["Estimated_Loss_INR"],
            description=row["Crime_Description"]
        )

        db.session.add(crime)

    db.session.commit()

    print("✅ Imported", Crime.query.count(), "records")