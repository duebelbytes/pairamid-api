from app.extensions import db
from app.models import User, PairingSession, PairingSession
from sqlalchemy.ext.serializer import loads, dumps

def seed():
    eo = User(username='eo', role='HOME')
    nh = User(username='nh', role='HOME')
    bd = User(username='bd', role='HOME')
    jh = User(username='jh', role='HOME')
    ms = User(username='ms', role='HOME')
    es = User(username='es', role='HOME')
    kd = User(username='kd', role='HOME')
    mj = User(username='mj', role='HOME')
    jw = User(username='jw', role='HOME')
    ar = User(username='ar', role='HOME')
    mvs = User(username='mvs', role='HOME')

    cd = User(username='cd', role='VISITOR')
    tp = User(username='tp', role='VISITOR')
    mr = User(username='mr', role='VISITOR')
    rp = User(username='rp', role='VISITOR')
    rj = User(username='rj', role='VISITOR')
    jl = User(username='jl', role='VISITOR')
    cp = User(username='cp', role='VISITOR')

    home = [eo, nh, bd, jh, ms, es, kd]
    solos = [[mvs], [mj], [jw], [ar]]
    visitor = [cd, tp, mr, rp, rj, jl, cp]


    for user in home + visitor:
        db.session.add(user)

    for pair in solos:
        pairing_session = PairingSession(users=list(pair))
        db.session.add(pairing_session)

    for pair in list(zip(home, visitor)):
        pairing_session = PairingSession(users=list(pair))
        db.session.add(pairing_session)

    db.session.commit()

def save_history():
    with open('./app/tests/fixtures/history.bin', 'wb') as f:
        history = PairHistory.query.all()
        f.write(dumps(history))

def load_history():
    with open('./app/tests/fixtures/history.bin', 'rb') as f:
        for row in loads(f.read()):
            db.session.merge(row)

    db.session.commit()