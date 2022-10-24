from app import app
from models import db, Cupcake


db.drop_all()
db.create_all()

c1 = Cupcake(
    flavor="cherry",
    size="large",
    rating=5,
)

c2 = Cupcake(
    flavor="chocolate",
    size="small",
    rating=9,
    image="https://www.bakedbyrachel.com/wp-content/uploads/2018/01/chocolatecupcakesccfrosting1_bakedbyrachel.jpg"
)

c3 = Cupcake(
    flavor="cherry 2",
    size="large",
    rating=5,
)

c4 = Cupcake(
    flavor="cherry 3",
    size="large",
    rating=5,
)

c5 = Cupcake(
    flavor="cherr 4",
    size="large",
    rating=5,
)

db.session.add_all([c1, c2, c3, c4, c5])
db.session.commit()
