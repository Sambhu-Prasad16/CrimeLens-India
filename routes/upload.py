import pandas as pd
from models import db

from flask import Blueprint, request, render_template

upload_bp = Blueprint("upload", __name__)

@upload_bp.route("/upload", methods=["GET","POST"])

def upload():

    if request.method=="POST":

        file=request.files["dataset"]

        df=pd.read_csv(file)

        df.to_sql(
            "crimes",
            con=db.engine,
            if_exists="append",
            index=False
        )

    return render_template("upload/upload.html")