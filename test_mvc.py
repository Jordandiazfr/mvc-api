import mvc
import pytest 

# Model  -- tests
@pytest.fixture
def Model():
    return  mvc.Model()

def test_model_uppper(Model):
    assert Model.modify_inputs("jordan") == "JORDAN"

def test_model_palindrome(Model):
    assert Model.is_palindrome("jordan") == False

#  View -- tests
def test_view():
    vue = mvc.View()
    assert vue

# Controller -- tests 
def test_Controller():
    controller = mvc.Controller(mvc.View(),mvc.Model())
    assert controller
