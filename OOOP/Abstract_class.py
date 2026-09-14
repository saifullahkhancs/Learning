# Abstract classes are typically used when you want to define a common interface
# or behavior that multiple derived classes should adhere to, while leaving the
# implementation details to the derived classes. They act as a contract,  
# that certain methods or attributes are present in the derived classes.ensuring

# In Python, you can create an abstract class using the abc module,
#  which provides the ABC (Abstract Base Class) and abstractmethod
#  decorators.


# @ are called decorators

#  @abstractmethod
#  @staticmethod  as ko hi use kar ka ham factory constructor call karta hain method call kar sakta hain
#  @classmethod
#  

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def display(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius ** 2

    def display(self):
         print(f"Circle with radius {self.radius}")

    def anyy(self):

        print("anyway")

# Attempting to create an instance of the abstract class (Shape)
#shape = Shape()  # Output: TypeError: Can't instantiate abstract class Shape with abstract methods calculate_area, display

# Creating an instance of the derived class (Circle)
circle = Circle(5)
circle.calculate_area()   # Output: 78.5
circle.display()          # Output: Circle with radius 5




from abc import ABC, abstractmethod

# ----------------------------------------------------
# 1. INTERFACE CLASS (Pure Contract)
# Contains ONLY abstract methods. No concrete code or attributes.
# ----------------------------------------------------
class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount: float) -> bool:
        pass

    @abstractmethod
    def refund_payment(self, transaction_id: str) -> bool:
        pass


# ----------------------------------------------------
# 2. ABSTRACT CLASS (Partial Implementation)
# Combines abstract methods with shared concrete logic/attributes.
# ----------------------------------------------------
class BaseNotification(ABC):
    def __init__(self, sender: str):
        self.sender = sender  # Shared state

    # Concrete method (shared behavior across all notifications)
    def log_notification(self, message: str):
        print(f"[LOG] Notification sent from {self.sender}: {message}")

    # Abstract method (contract that concrete subclasses must implement)
    @abstractmethod
    def send(self, recipient: str, message: str):
        pass


# ----------------------------------------------------
# 3. CONCRETE IMPLEMENTATIONS
# ----------------------------------------------------
class CreditCardProcessor(PaymentProcessor):
    def process_payment(self, amount: float) -> bool:
        print(f"Processing ${amount} via Credit Card.")
        return True

    def refund_payment(self, transaction_id: str) -> bool:
        print(f"Refunding transaction {transaction_id} to Credit Card.")
        return True


class EmailNotification(BaseNotification):
    def send(self, recipient: str, message: str):
        print(f"Sending Email to {recipient}: {message}")
        self.log_notification(message)  # Reusing base class method


# Usage
card_payment = CreditCardProcessor()
card_payment.process_payment(150.0)

email = EmailNotification(sender="admin@example.com")
email.send(recipient="user@example.com", message="Welcome to the platform!")