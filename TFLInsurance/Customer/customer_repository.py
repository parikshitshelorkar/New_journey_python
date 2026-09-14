import Customer.customer
class CustomerRepository:
    def create_customer(id, name, email):
        Customer(id, name, email)
        return "Sucessfully created customer profile"
    
    def get_customer(id):
        return Customer(id)
    
    def update_customer(id, name, email):
        return Customer(id, name, email)
    
    