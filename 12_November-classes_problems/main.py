# class Todolist :
#     def __init__(self):
#         self.tasks = []
    
#     def add_task( self , task_id:int,task : str,status:str ):
#         curr_task = {
#             "task_id" = task_id,
#             "task" = task,
#             "status" = status
#         }
#         self.tasks.append(curr_task)
#     def view_task(self):
#         print(tasks)
#     def delete_task(self,task_id):



class Orders:
    def __init__(self):
        self.cart={}

    def add_item(self,item_id,product_name,quantity,price):
        if item_id in self.cart:
            self.cart[item_id]["qty"] += quantity
        
        else:
            self.cart[item_id] = {
                "name": product_name,
                "qty": quantity,
                "price": price
            }

    def remove_item(self,item_id):
        if item_id in self.cart:
            del self.cart[item_id]

    def total(self):
        total = 0
        for item in self.cart.values():
            total += item["qty"] * item["price"]
        return total
    def show_total(self):
        print(self.total())

o = Orders()
o.add_item(1, "Samosa", 5, 10)
o.add_item(2, "Tea", 2, 15)

o.show_total()