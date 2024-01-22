'''
CREATING A NEW DATABASE
-----------------------
Read explanation here: https://flask-sqlalchemy.palletsprojects.com/en/2.x/contexts/

In the terminal navigate to the project folder just above the miltontours package
Type 'python' to enter the python interpreter. You should see '>>>'
In python interpreter type the following (hitting enter after each line):
    from miltontours import db, create_app
    db.create_all(app=create_app())
The database should be created. Exit python interpreter by typing:
    quit()
Use DB Browser for SQLite to check that the structure is as expected before 
continuing.

ENTERING DATA INTO THE EMPTY DATABASE
-------------------------------------

# Option 1: Use DB Browser for SQLite
You can enter data directly into the cities or tours table by selecting it in
Browse Data and clicking the New Record button. The id field will be created
automatically. However be careful as you will get errors if you do not abide by
the expected field type and length. In particular the DateTime field must be of
the format: 2020-05-17 00:00:00.000000

# Option 2: Create a database seed function in an Admin Blueprint
See below. This blueprint needs to be enabled in __init__.py and then can be 
accessed via http://127.0.0.1:5000/admin/dbseed/
Database constraints mean that it can only be used on a fresh empty database
otherwise it will error. This blueprint should be removed (or commented out)
from the __init__.py after use.

Use DB Browser for SQLite to check that the data is as expected before 
continuing.
'''

from flask import Blueprint
from . import db
from .model import Category, Item, Order

bp = Blueprint('admin', __name__, url_prefix='/admin/')

# function to put some seed data in the database
@bp.route('/dbseed/')
def dbseed():

    wheel = Category(name='Wheel', image='Category_Wheel.jpeg')
    exhaustSystem = Category(name='ExhaustSystem', image='Category_ExhaustSystem.jpeg')
    Brake = Category(name='Brake', image='Category_Brake.jpeg')

    try:
        db.session.add(wheel)
        db.session.add(exhaustSystem)
        db.session.add(Brake)
        db.session.commit()
    except:
        return 'There was an issue adding the categories in dbseed function'

    i1 = Item(category_id=wheel.id, image='Wheel_ImpulLine.jpeg', price=870,\
        name='IMPUL TEAM IMPUL RACING LINE GT-06',\
        description= 'An all-rounder, 10-spoke design that matches a variety of car models. The spoke thickness is varied from the rim to the center, creating a dynamic feeling of life and stylish, flowing, edgy lines.') 
    i2 = Item(category_id=wheel.id, image='Wheel_TOMs.jpeg', price=540,\
        name='TOM\'S aluminum wheel TH05',\
        description= 'The elegant contrast of gloss black and polished rims, which beautifully enhance your feet, and the racy taste of the cross spokes give your car a luxurious and sporty look.')
    i3 = Item(category_id=wheel.id, image='Wheel_STIperformance.jpeg', price=640,
        name='STIperformance wheel 18inch black',\
        description= 'Forged aluminum wheels developed in collaboration with RAYS. Unlike the general casting method, forged wheels are characterized by their light weight and high rigidity, as they are formed by heating a base metal material called a billet and pressing it into a metal mold under high pressure. The dense metallic structure ensures strength without compromising weight, and provides high performance in responsiveness to handling.')
    i4 = Item(category_id=exhaustSystem.id, image='Exhaust_TAKEOFF.jpeg', price=740,\
        name='TAKE OFF CROSS STAGE Muffler',\
        description= 'It eliminates the grating sound quality area and produces a pleasant sound at mid to high RPM. The main pipe is 50.8φ (50.8mm), which improves turbine start-up and blow-off at mid-range RPM. This muffler has passed the JQR acceleration noise test and is inspection compliant.')                
    i5 = Item(category_id=exhaustSystem.id, image='Exhaust_Kakimoto.png', price=725,\
        name='Kakimoto Kai Class KR GR bumper',\
        description= 'The new standards are stricter than before, but the Kakimoto sound is still there. Kakimoto\'s unique sound creation was realized so that even under the strict regulations, you can enjoy the fact that the muffler has been replaced. Needless to say, performance was not compromised. Increased power and torque throughout the entire range.')
    i6 = Item(category_id=exhaustSystem.id, image='Exhaust_M\'z.jpeg', price=21888,\
        name='M\'z SPEED exhaust system (MZ99)',\
        description= 'The four-strand style with left and right tail lights that match the aerodynamic shape gives the rear view a sporty appearance. Two different tail colors are available, so you can choose the styling that best suits your taste.') 
    i7 = Item(category_id=Brake.id, image='Brake_Odula.jpeg', price=360,\
        name='Odula Big Caliper Kit BP MAZDA3',\
        description= 'These big brake calipers look great on the MAZDA3\'s undercarriage, contributing to a more sporty appearance and improved braking power. The lightweight and rigid 4POT calipers and 330mm slit rotors make for an easy-to-manage brake kit that offers high braking power and control, and is designed to fit 17-inch wheels.')
    i8 = Item(category_id=Brake.id, image='Brake_Result.jpeg', price=270,\
        name='Result Japan Caliper Cover ZN8 86',\
        description= 'The original brake caliper cover that peeks out from the will not only increase the sense of luxury but also appeal, and its presence will be dramatically increased by installing it.')
    i9 = Item(category_id=Brake.id, image='Brake_Climate.jpeg', price=210,\
        name='CLIMATE Brake Caliper Cover Red',\
        description= 'Pierce bolts and nipples are used to reproduce the texture of brake calipers. Installation is as simple as covering the stock caliper and securing with a spring. When installed, the caliper is almost completely covered by the stock caliper to reduce brake dust. High quality original caliper covers for attractive undercarriage.')

    try:
        db.session.add(i1)
        db.session.add(i2)
        db.session.add(i3)
        db.session.add(i4)
        db.session.add(i5)
        db.session.add(i6)
        db.session.add(i7)
        db.session.add(i8)
        db.session.add(i9)
        db.session.commit()
    except:
        return 'There was an issue adding a item in dbseed function'

    return 'DATA LOADED'