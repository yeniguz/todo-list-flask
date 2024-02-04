from todor import create_app

app = create_app()

if __name__ == '__main__': #este archivo solo se ejecutara si se llama por su nombre directamente osea run
    app.run()