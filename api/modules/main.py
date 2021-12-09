from model import Model
from controller import Controller
from view import View


if __name__ == "__main__":   
    app =  Controller(view=View(), model=Model())
    
    if app.manage_inputs(): app.manage_textfile()