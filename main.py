class FoodDeliverySystem:
    def __init__(self):
        self.orders_log = []
        self.tax_rate = 0.1  # 10% tax rate

    def add_order(self, order_details):
        self.orders_log.append(order_details)
        return "Order added successfully."

    def update_order_status(self, order_id, status):
        for order in self.orders_log:
            if order['order_id'] == order_id:
                order['status'] = status
                return "Order status updated successfully."
        return "Order not found."

    def modify_order_items(self, order_id, new_items):
        for order in self.orders_log:
            if order['order_id'] == order_id:
                if order['status'] != 'Picked up':
                    order['items'] = new_items
                    return "Order items modified successfully."
                else:
                    return "Cannot modify items. Order already picked up."
        return "Order not found."

    def cancel_order(self, order_id):
        for order in self.orders_log:
            if order['order_id'] == order_id:
                if order['status'] != 'Picked up':
                    self.orders_log.remove(order)
                    return "Order canceled successfully."
                else:
                    return "Cannot cancel order. Order already picked up."
        return "Order not found."

    def generate_bill(self, order_id):
        for order in self.orders_log:
            if order['order_id'] == order_id:
                bill_amount = order['total_amount']
                if bill_amount > 1000:
                    total_bill_amount = bill_amount + (bill_amount * self.tax_rate)
                else:
                    total_bill_amount = bill_amount + (bill_amount * 0.05)
                return total_bill_amount
        return 0.0

# Test cases
food_delivery = FoodDeliverySystem()
print(food_delivery.add_order({'order_id': 1, 'items': ['Pizza', 'Burger'], 'total_amount': 1200}))
print(food_delivery.update_order_status(1, 'Picked up'))
print(food_delivery.modify_order_items(1, ['Sandwich', 'Fries']))
print(food_delivery.cancel_order(1))
print(food_delivery.generate_bill(1))


