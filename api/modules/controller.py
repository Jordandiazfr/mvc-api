# --- Controller ---- 
class Controller:  
    def __init__(self, model, view) -> None:
        self.view = view
        self.model = model
        self.file_name = ""
        
    def manage_inputs(self, view):     
        for _ in range(2):
            # Tell the view to get inputs
            line = self.view.get_input()       
            if line == 0:
                raise ValueError("You must write something")  
            else: 
                # Put them in CAPS
                line_upper = self.model.modify_inputs(line)

                # Show if it is a palyndrome
                print(self.model.is_palindrome(line)) 
                
                # Tell the model to save the inputs
                self.model.save_inputs(line_upper) 
        return True
        
    def manage_textfile(self):
        if self.model.write_file():
            self.view.show_file_content()