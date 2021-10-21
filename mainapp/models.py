from django.db import models


class Clients(models.Model):
    passport_series = models.CharField(max_length=100)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    phone = models.PositiveBigIntegerField()
    objects = models.Manager()

    def __str__(self):
        return self.firstname

    @property
    def pay_sum(self):
        a = [item.cars.rent_cost * item.days_count for item in self.client_items.all()]
        return sum(a)


class Cars(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    rent_cost = models.PositiveIntegerField()
    objects = models.Manager()

    # def __str__(self):
    #     return '{} - model {}'.format(self.brand, self.model)

    def __str__(self):
        return '{}'.format(self.id)

    @property
    def car_count_in_order(self):
        a = [item.cars for item in self.car_items.all()]
        return len(a)

    @property
    def total_profit(self):
        a = [item.days_count for item in self.car_items.all()]
        return sum(a) * self.rent_cost


class Orders(models.Model):
    client_id = models.ForeignKey(Clients, on_delete=models.CASCADE, related_name="client_items")
    cars = models.ForeignKey(Cars, on_delete=models.CASCADE, related_name="car_items")
    timestamp = models.DateField(auto_now_add=True)
    from_date = models.DateField()
    to_date = models.DateField()
    objects = models.Manager()

    def __str__(self):
        return '{}'.format(self.id)

    @property
    def extended_days(self):
        a = [item.extended_to for item in self.extend.all()]
        return a

    @property
    def exday(self):
        a = [item.extended_to for item in self.extend.all()]
        if len(a) != 0:
            return (a[-1] - self.to_date).days

    @property
    def days_count(self):
        if self.exday is None:
            return (self.to_date - self.from_date).days
        else:
            self.first = (self.to_date - self.from_date).days
            return self.first + self.exday

    @property
    def extend_order_count(self):
        a = [item.order for item in self.extend.all()]
        return len(a)


class Extended_orders(models.Model):
    order = models.ForeignKey(Orders, on_delete=models.CASCADE, related_name="extend")
    extended_to = models.DateField()
    objects = models.Manager()

    def __str__(self):
        return self.order













