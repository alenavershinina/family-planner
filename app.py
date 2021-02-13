from flask import Flask

webapp = Flask(__name__, static_url_path='')


@webapp.route('/health')
def health_check():
    return {'status': 'up'}


@webapp.route('/')
def index():
    return webapp.send_static_file('index.html')


if __name__ == '__main__':
    webapp.run(host='0.0.0.0', port=8080)
