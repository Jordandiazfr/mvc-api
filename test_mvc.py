from api.modules import model, view, controller
import pytest 
import io

# Model  -- tests
@pytest.fixture
def Model():
    return model.Model()

def test_model_uppper(Model):
    assert Model.modify_inputs("jordan") == "JORDAN"

def test_model_int(Model):
    with pytest.raises(AttributeError):
        Model.modify_inputs(3)

def test_model_palindrome(Model):
    assert Model.is_palindrome("jordan") == False

def test_save_inputs(Model):
    assert Model.stock.stock_list == []
    Model.save_inputs("jordan")
    assert Model.stock.stock_list == ["jordan"]

#  View -- tests
@pytest.fixture
def View():
    return view.View()

def test_get_input(View, monkeypatch):
    assert View.user_input == ""
    monkeypatch.setattr('sys.stdin', io.StringIO('my_input'))
    assert View.get_input() == 'my_input'


# Controller -- tests 
@pytest.fixture
def Controller(Model, View):
    return controller.Controller(Model, View)

def test_manage_inputs(Controller, View, monkeypatch):
    monkeypatch.setattr(View, 'get_input', lambda: 'toto')
    assert View.get_input() == 'toto'
    assert Controller.manage_inputs(View) == True

