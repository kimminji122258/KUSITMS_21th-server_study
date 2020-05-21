from flask import Flask, render_template
from database import db, User
from flask_migrate import Migrate

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite3"
db.init_app(app)
migrate = Migrate(app, db)


@app.route("/user")
def user_list():
    users = User.query.all()  #데이터베이스의 모든 것을 가져옴
    return render_template("index.html", users=users)


@app.route("/user/<int:id>")
def user_detail(id):
    user = User.query.filter_by(id=id).first()  #url의 파라미터와 id가 같은 것을 가져오는 것
    return render_template("detail.html", user=user)


if __name__ == "__main__":
    app.run()