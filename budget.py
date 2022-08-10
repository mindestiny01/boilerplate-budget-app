class Category:
    def __init__(self, category: str):
        """Constructor for Category"""
        self.category = category
        self.__balance = 0.0
        self.ledger = []

    def get_balance(self) -> float:
        """Latest Balance"""
        return self.__balance

    def __repr__(self):
        """Retrieve the all information based on Category"""

        # Choosed Category info
        category_information = self.category.center(30, "*") + '\n'
        
        # Amount and Description of Choosed Category
        item__amount_information = ""
        for info in self.ledger:
            # Formatting the Presentation
            desc_info = "{:<25}".format(info["description"])
            desc_amount = "{:>7.2f}".format(info["amount"])
            
            # Retrieve all the formatted info
            item__amount_information += f'{desc_info[:23]}{desc_amount[:7]}' + '\n'
        
        # All the balance of Choosed Category
        total_amount = "Total: {:.2f}".format(self.__balance)

        # return the all information
        return category_information + item__amount_information + total_amount


    def deposit(self, amount: float, about = "") -> float:
        """All the deposit activities"""

        # Append the deposit and information to ledger
        self.ledger.append({"amount": amount, "description": about})
        self.__balance += amount

        return self.__balance


    def withdraw(self, amount: float, about = "") -> bool:
        """All the withdraw activities"""
        
        # if the differences are less than 0, return False
        if self.__balance - amount < 0:
            return False
        
        # Otherwise, append the amount and description to the 
        else:
            self.ledger.append({"amount": -1 * amount, "description": about})
            self.__balance -= amount
            return True

        
    def transfer(self, amount: float, category_instances) -> bool:
        """All the Transfer activities"""

        # check the other category for transfer
        # if get the info, transfer it based amount, return True
        if self.withdraw(amount, f'Transfer to {category_instances.category}'):
            category_instances.deposit(amount, f'Transfer from {self.category}')
            return True
        # otherwise return False
        else: return False

    def check_funds(self, amount: float) -> bool:
        """Check the argument"""

        # check the current balance, if more than amount, return True
        if self.__balance >= amount: 
            return True
        # otherwise return False
        else: 
            return False

    

# def create_spend_chart(categories: list):
def create_spend_chart(categories: list) -> str:

    # Retrieve the all amount for each categories
    recorded_amount = []
    for category in categories:
        each_amount = 0
        # Get the ledger methods
        for spent in category.ledger:
            if spent["amount"] < 0:
                # Make the amount to be absolute
                each_amount += abs(spent["amount"])
        recorded_amount.append(round(each_amount, 2))

    # Get nearest 10
    amount_total = round(sum(recorded_amount), 2)
    percentage = list(map(lambda amount: int((((amount / amount_total) * 10) // 1) * 10), recorded_amount))    
    
    header = "Percentage spent by category\n"
    
    # Creating y-axis Cartesian
    visualization_spent = ''
    for spent in range(100, -10, -10):
        y_axis = "{:>3}|".format(spent)
        for percent in percentage:
            if percent >= spent:
                y_axis += " o "
            else: y_axis += "   "

        visualization_spent += "{} \n".format(y_axis)

    # Get the recorded categories and justify 
    vertical_desc = "    " + "-" * ((len(categories) * 3) + 1) + '\n'
    categories_info = list(info for category in categories for info in [category.category])
    longest_str = max(len(str_length) for str_length in categories_info)
    justify = list(desc.ljust(longest_str) for desc in categories_info)

    for x in zip(*justify):
        # vertical_desc += "    " + "".join(map(lambda s: s.center(3), x)) + " \n"
        vertical_desc += "    " + "".join(ready.center(3) for ready in x) + " \n"

    # return the the charts
    return (header + visualization_spent + vertical_desc).rstrip('\n')
