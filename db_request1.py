global_init(input())
db_sess = create_session()
users = db_sess.query(User).filter(User.address == "module_1", User.speciality.notlike('%engineer%'),
                                   User.speciality.notlike('%engineer%')).all()
for user in users:
    print(user.id)