from app import app

def test_home_status_200():
    cliente = app.test_client()
    respuesta = cliente.get('/')
    assert respuesta.status_code == 200 # nosec B101