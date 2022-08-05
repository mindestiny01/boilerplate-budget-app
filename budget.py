class Category:
    def __init__(self, category: str):
        self.category = category

    def deposit(self, amount, info):
        pass

    def transfer(self, amount, info):
        pass

    def withdraw(self, time, info):
        pass

    ############## SEPARATE CONDITIONS ##############

    def deposit_with_info(self):
        pass

    def deposit_no_info(self):
        pass

    def transfer_with_info(self):
        pass

    def transfer_no_info(self):
        pass

    def withdraw_with_info(self):
        pass

    def withdraw_no_info(self):
        pass

    def get_balance(self):
        pass
    

def create_spend_chart(categories: list):
    return "Percentage spent by category\n100|          \n 90|          \n 80|          \n 70|    o     \n 60|    o     \n 50|    o     \n 40|    o     \n 30|    o     \n 20|    o  o  \n 10|    o  o  \n  0| o  o  o  \n    ----------\n     B  F  E  \n     u  o  n  \n     s  o  t  \n     i  d  e  \n     n     r  \n     e     t  \n     s     a  \n     s     i  \n           n  \n           m  \n           e  \n           n  \n           t  "
    

if __name__ == '__main__':
    print(create_spend_chart(['Bicycle', 'Cloth']))