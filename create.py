from application.models import db, Teams

db.drop_all()
db.create_all()

# test = Teams(description = "IT WORKS!!!!")
# db.session.add(test)
# db.session.commit()