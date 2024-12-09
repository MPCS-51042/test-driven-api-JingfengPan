from fastapi.testclient import TestClient
from main import app
from database import Database

client = TestClient(app)

champions_data = [
    {"name": "Jinx", "region": "Zaun"},
    {"name": "Ahri", "region": "Ionia"},
    {"name": "Darius", "region": "Noxus"}
]

def setup_test_database():
    app.db = Database()  # Inject an instance of Database
    for champion in champions_data:
        app.db.put(champion["name"], champion)

# Test the main endpoint (root endpoint)
def test_main():
    response = client.get('/')
    assert response.status_code == 200
    assert response.json() == {"champion": "region"}

# Test GET to retrieve all champions
def test_list_champions():
    setup_test_database()
    response = client.get('/champions')
    assert response.status_code == 200
    assert response.json() == {champion["name"]: champion for champion in champions_data}

# Test POST to add a new champion
def test_create_champion():
    setup_test_database()
    new_champion = {"name": "Ekko", "region": "Zaun"}
    
    response = client.post('/champions', json=new_champion)
    assert response.status_code == 200
    assert response.json() == new_champion

    # Verify Ekko is added to the database
    response = client.get('/champions')
    assert response.status_code == 200
    assert "Ekko" in response.json()
    assert response.json()["Ekko"] == new_champion

# Test GET to retrieve each specific champion
def test_get_champion():
    setup_test_database()
    for champion in champions_data:
        response = client.get(f'/champions/{champion["name"]}')
        assert response.status_code == 200
        assert response.json() == {champion["name"]: champion}  # Expect full champion data

# Test DELETE to delete each specific champion
def test_delete_champion():
    setup_test_database()
    
    # Delete each champion and check if they were deleted successfully
    for champion in champions_data:
        response = client.delete(f'/champions/{champion["name"]}')
        assert response.status_code == 200
        assert response.json() == {}
        
        # Verify champion is no longer in the database
        response = client.get(f'/champions/{champion["name"]}')
        assert response.status_code == 200
        assert response.json() == {champion["name"]: None}
    
    # Verify the database is empty after deletions
    response = client.get('/champions')
    assert response.status_code == 200
    assert response.json() == {}
