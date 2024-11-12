from database import Database

def test_get():
    # GIVEN
    db = Database()
    db._data = {"Jinx": "Zaun"}

    # WHEN
    result = db.get("Jinx")

    # THEN
    assert result == "Zaun"

def test_put():
    # GIVEN
    db = Database()

    # WHEN
    db.put("Ekko", "Zaun")

    # THEN
    assert db._data["Ekko"] == "Zaun"

def test_all():
    # GIVEN
    db = Database()
    dict = {"Jinx": "Zaun", "Ekko": "Zaun"}
    db._data = dict
    # WHEN
    result = db.all()

    # THEN
    assert result == dict

def test_delete():
    # GIVEN
    db = Database()
    db._data = {"Jinx": "Zaun", "Ekko": "Zaun"}

    # WHEN
    db.delete("Jinx")

    # THEN
    assert "Jinx" not in db._data
    assert db._data == {"Ekko": "Zaun"}