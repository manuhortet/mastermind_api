from app.api import app as application

application.config.from_object('app.configuration')

if __name__ == '__main__':
    host = application.config['HOST']
    port = application.config['PORT']
    application.run(host=host, port=port)
