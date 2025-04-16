from app import db
from app.models import User, Address

def reset_db():
    try:
        db.drop_all()
        db.create_all()

        u1 = User(username='amy', email='a@b.com', role='Admin')
        u1.set_password('amy.pw')
        u2 = User(username='tom', email='t@b.com', role='Admin')
        u2.set_password('tom.pw')
        u3 = User(username='yin', email='y@b.com', role='Staff')
        u3.set_password('yin.pw')
        u4 = User(username='tariq', email='tariq@b.com',role='Staff')
        u4.set_password('tariq.pw')
        u5 = User(username='jo', email='jo@b.com')
        u5.set_password('jo.pw')
        u6 = User(username='john', email='john@b.com')
        u6.set_password('john.pw')

        u1.addresses.append(Address(tag='home', address='Amy, 22b Baker Street, London SW1', phone='12345678'))
        u1.addresses.append(Address(tag='work', address='Amy, Amy\'s Company, London SW1', phone='23456789'))

        db.session.add_all([u1, u2, u3, u4, u5,u6])
        db.session.commit()
    except:
        print("SORRY GUYS you can't use debug_utils just yet, because I didn't edit it to conform to the new classes")
