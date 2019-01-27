
import datetime # for getting current year, month
import matplotlib.pyplot as plt

# get current date
now = datetime.datetime.now()

class UserData(object):

    def __init__(self, username):
        self.username = username
        self.data = self.setup_data()

    def setup_data(self):
        """Creates a blank data dictionary."""
        data = {"Year": [],
                "Month": [],
                "Day": [],
                "Company Name": [],
                "Category": [],
                "Amount": [],
                "is_yearly": [],
                "is_monthly": []
                }
        return data

    def add_item(self, item):
        """Add a purchase to the user data.

        Parameters
        ----------
        item : dict
            Contains categories listed in data.
            Year - of purchase
            Month - of purchase
            Day - of purchase
            Company Name - name of store
            Category - store category (i.e. groceries/piegraph category)
            Amount - expense cost (CAD $)
            is_yearly - bool, yearly cost (bill payment)
            is_monthly - bool, monthly cost (bill payment)

        """
        self.data["Year"].append(item["Year"])
        self.data["Month"].append(item["Month"])
        self.data["Day"].append(item["Day"])
        self.data["Company Name"].append(item["Company Name"])
        self.data["Category"].append(item["Category"])
        self.data["Amount"].append(item["Amount"])
        self.data["is_yearly"].append(item["is_yearly"])
        self.data["is_monthly"].append(item["is_monthly"])

    def monthly_expenses(self, month, year):
        """Determine indices of purchases by given month and year.

        Returns
        -------
        expense_indices : list(indices)
            List of purchases by index that match year and month.

        """
        expense_indices = []
        for i in range(self.num_transactions):
            if self.data["Year"] == year and self.data["Month"] == month:
                expense_indices.append(i)
        return expense_indices

    def yearly_expenses(self, year):
        """Same as monthly_expenses, except for year."""
        expense_indices = []
        for i in range(self.num_transactions):
            if self.data["Year"] == year:
                expense_indices.append(i)
        return expense_indices

    def monthly_piegraph(self, month, year=now.year):
        """Make a piegraph for monthly expenses.

        Parameters
        ----------
        month : str
            Month to make a piegraph for.
        year : int
            Year to make the piegraph for. Defaults
            to the current year (as set by datetime).

        """
        pie = {}
        # t for transaction
        for t in self.monthly_expenses(month, year):
            category = self.data[t]["Category"]
            if category in pie:
                pie[category] += self.data[t]["Amount"]
        labels = pie.keys()
        amounts = list(pie.values())  
        # make piegraph
        fig1, ax1 = plt.subplots()
        ax1.pie(amounts, labels=labels, autopct="%1.1f%%",
                shadow=True, startangle=90)
        ax1.axis("equal")
        plt.show()            

    @property
    def num_transactions(self):
        """Number of purchases."""
        return len(self.data["Year"])
    
