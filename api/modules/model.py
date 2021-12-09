# --- Model -----
class Model: 
    def __init__(self) -> None:
        self.stock = self.Stock()
    
    def save_inputs(self, user_input: str):
        self.stock.stock_list.append(user_input)
        return True
    
    def modify_inputs(self,user_input: str) -> str:
        return user_input.upper()
        
    def write_file(self):     
        f = open("output.txt", "w")
        for line in self.stock.stock_list:     
            f.write(line + "\n")        
        f.close()
        return True
   
    def is_palindrome(self, user_input: str)-> str:
        return user_input[::-1] == user_input
    
    class Stock:
        def __init__(self) -> None:
            self.stock_list = []
            