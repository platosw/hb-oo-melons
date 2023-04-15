"""Classes for melon orders."""
from random import randint
from datetime import datetime


class MelonOrder:
    def __init__(self, species, qty, order_type, tax, is_x_mas=False):
        self.species = species
        self.qty = qty
        self.order_type = order_type
        self.tax = tax
        self.is_x_mas = is_x_mas
        self.shipped = False

    def get_total(self):
        """Calculate price, including tax."""

        def get_base_price():
            price = randint(5, 9)
            time_now = datetime.today()
            hour_now = datetime.today().hour
            day_of_the_week = datetime.weekday(time_now)

            if 8 <= hour_now and hour_now <= 10:
                if 0 <= day_of_the_week and day_of_the_week <= 4:
                    price += 4

            return price

        base_price = get_base_price()

        if self.is_x_mas == True:
            base_price *= 1.5

        total = (1 + self.tax) * self.qty * base_price

        if self.qty < 10 and self.order_type == "international":
            total += 3

        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True


class DomesticMelonOrder(MelonOrder):
    """A melon order within the USA."""

    def __init__(self, species, qty, is_x_mas=False):
        """Initialize melon order attributes."""

        self.order_type = "domestic"
        self.tax = 0.08
        super().__init__(species, qty, self.order_type, self.tax, is_x_mas)


class InternationalMelonOrder(MelonOrder):
    """An international (non-US) melon order."""

    order_type = "international"

    def __init__(self, species, qty, country_code, is_x_mas=False):
        """Initialize melon order attributes."""

        self.country_code = country_code
        self.tax = 0.17
        super().__init__(species, qty, self.order_type, self.tax, is_x_mas)

    def get_country_code(self):
        """Return the country code."""

        return self.country_code


class GovernmentMelonOrder(MelonOrder):
    def __init__(self, species, qty, is_x_mas=False):
        self.passed_inspection = False
        self.tax = 0
        super().__init__(species, qty, self.tax, is_x_mas)

    def mark_inspection(self, passed):
        if (passed):
            self.passed_inspection = True
