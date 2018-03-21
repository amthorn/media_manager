from app import app


@app.route('/', methods=['GET'])
def index():
    return "main page ava"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9999, debug=True)
