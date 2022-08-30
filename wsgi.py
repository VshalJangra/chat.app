from app.main import app, mode, socketio

if __name__ == '__main__' and mode == "PRODUCTION":
    print("Running production server.")
    app.run()

elif __name__ == "__main__" and mode == "DEV":
    print("Running development server.")
    socketio.run(app, debug=True)