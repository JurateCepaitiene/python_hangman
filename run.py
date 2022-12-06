from project import create_app

if __name__=="__main__":
    app, db = create_app()
    # with app.app_context():
        # db.create_all()
        # db.init_app(app)

    app.run(debug=True)