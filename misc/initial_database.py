import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(
    cred,
    {
        "databaseURL": "",
        # database URL
    },
)

ref = db.reference(
    "Students"
)  # reference path to our database... will create student directory in the database

data = {
    "032003": {  # id of student which is a key
        "id": "032003",
        "name": "B.Devesh",
        "password": "Devesh@2003",
        "dob": "2003-12-03",
        "address": "Gujarat, vadodara",
        "phone": "",
        "email": "pentaakhilrock@gmail.com",
        "major": "cse-ai",
        "starting_year": 2021,
        "standing": "G",
        "total_attendance": 0,
        "year": 4,
        "last_attendance_time": "2023-02-21 12:33:10",
        "content": "This section aims to offer essential guidance for students to successfully complete the course. It will be regularly updated \
                to ensure its relevance and usefulness. Stay tuned for valuable \
                insights and tips that will help you excel in your studies.",
    },
}


for key, value in data.items():
    ref.child(key).set(value)
