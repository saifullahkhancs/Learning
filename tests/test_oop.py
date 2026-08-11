"""Tests for OOP modules: inheritance, polymorphism, aggregation, composition."""

import io
import os
import sys
from unittest.mock import patch

import pytest

from tests.conftest import load_classes_from_source, load_module_from_path

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# ---------------------------------------------------------------------------
# OOOP/inheritance.py  (Vechicle, Car)
# ---------------------------------------------------------------------------
class TestInheritance:
    """Tests for Vechicle and Car in OOOP/inheritance.py."""

    @pytest.fixture(autouse=True)
    def setup(self):
        path = os.path.join(REPO_ROOT, "OOOP", "inheritance.py")
        mod = load_module_from_path(path, "inheritance")
        self.Vechicle = mod.Vechicle
        self.Car = mod.Car

    def test_vehicle_type(self):
        v = self.Vechicle("truck")
        assert v.type == "truck"

    def test_vehicle_type_info(self, capsys):
        v = self.Vechicle("bike")
        v.type_info()
        captured = capsys.readouterr()
        assert "bike" in captured.out

    def test_car_inherits_vehicle(self):
        car = self.Car("car", "Honda")
        assert isinstance(car, self.Vechicle)

    def test_car_attributes(self):
        car = self.Car("car", "Tesla")
        assert car.type == "car"
        assert car.name == "Tesla"

    def test_car_prod_info(self, capsys):
        car = self.Car("car", "BMW")
        car.prod_info()
        captured = capsys.readouterr()
        assert "BMW" in captured.out
        assert "car" in captured.out

    def test_car_inherits_type_info(self, capsys):
        car = self.Car("sedan", "Audi")
        car.type_info()
        captured = capsys.readouterr()
        assert "sedan" in captured.out

    def test_car_inherits_protected_method(self, capsys):
        car = self.Car("suv", "Jeep")
        car._pro_info()
        captured = capsys.readouterr()
        assert "comapny" in captured.out


# ---------------------------------------------------------------------------
# OOOP/oop_polymorphism.py  (Animal, cat, dog, Calculator)
# ---------------------------------------------------------------------------
class TestPolymorphism:
    """Tests for polymorphism classes in OOOP/oop_polymorphism.py."""

    @pytest.fixture(autouse=True)
    def setup(self):
        path = os.path.join(REPO_ROOT, "OOOP", "oop_polymorphism.py")
        mod = load_module_from_path(path, "oop_polymorphism")
        self.Animal = mod.Animal
        self.cat = mod.cat
        self.dog = mod.dog
        self.Calculator = mod.Calculator
        self.CarPoly = mod.Car
        self.Bike = mod.Bike

    def test_animal_sound(self, capsys):
        a = self.Animal()
        a.sound()
        captured = capsys.readouterr()
        assert "animal" in captured.out.lower()

    def test_cat_overrides_sound(self, capsys):
        c = self.cat()
        c.sound()
        captured = capsys.readouterr()
        assert "meow" in captured.out.lower()

    def test_dog_overrides_sound(self, capsys):
        d = self.dog()
        d.sound()
        captured = capsys.readouterr()
        assert "bahu" in captured.out.lower()

    def test_cat_is_animal(self):
        c = self.cat()
        assert isinstance(c, self.Animal)

    def test_dog_is_animal(self):
        d = self.dog()
        assert isinstance(d, self.Animal)

    def test_calculator_add_two(self, capsys):
        calc = self.Calculator()
        calc.add(2, 3)
        captured = capsys.readouterr()
        assert "5" in captured.out

    def test_calculator_add_three(self, capsys):
        calc = self.Calculator()
        calc.add(2, 3, 4)
        captured = capsys.readouterr()
        assert "9" in captured.out

    def test_car_tyre_info(self, capsys):
        car = self.CarPoly("suzuki", 4)
        car.tyre_info()
        captured = capsys.readouterr()
        assert "4" in captured.out

    def test_bike_tyre_info(self, capsys):
        bike = self.Bike("honda", 2)
        bike.tyre_info()
        captured = capsys.readouterr()
        assert "2" in captured.out


# ---------------------------------------------------------------------------
# OOOP/oop_relation_aggregation.py  (Book, Library)
# ---------------------------------------------------------------------------
class TestAggregation:
    """Tests for Book and Library in OOOP/oop_relation_aggregation.py."""

    @pytest.fixture(autouse=True)
    def setup(self):
        path = os.path.join(REPO_ROOT, "OOOP", "oop_relation_aggregation.py")
        mod = load_module_from_path(path, "oop_relation_aggregation")
        self.Book = mod.Book
        self.Library = mod.Library

    def test_book_creation(self):
        book = self.Book("Clean Code", "Robert C. Martin")
        assert book.title == "Clean Code"
        assert book.author == "Robert C. Martin"

    def test_library_creation(self):
        lib = self.Library("City Library")
        assert lib.name == "City Library"
        assert lib.books == []

    def test_add_book(self):
        lib = self.Library("Test Library")
        book = self.Book("Test", "Author")
        lib.add_book(book)
        assert len(lib.books) == 1
        assert lib.books[0].title == "Test"

    def test_add_multiple_books(self):
        lib = self.Library("Big Library")
        b1 = self.Book("Book1", "Author1")
        b2 = self.Book("Book2", "Author2")
        b3 = self.Book("Book3", "Author3")
        lib.add_book(b1)
        lib.add_book(b2)
        lib.add_book(b3)
        assert len(lib.books) == 3

    def test_display(self, capsys):
        lib = self.Library("My Library")
        lib.add_book(self.Book("Python Crash Course", "Eric Matthes"))
        lib.display()
        captured = capsys.readouterr()
        assert "Python Crash Course" in captured.out
        assert "Eric Matthes" in captured.out
        assert "My Library" in captured.out

    def test_book_exists_independently(self):
        book = self.Book("Standalone", "Author")
        lib = self.Library("Lib")
        lib.add_book(book)
        # Book exists independently of library
        assert book.title == "Standalone"
        del lib
        assert book.title == "Standalone"


# ---------------------------------------------------------------------------
# OOOP/oop_relation_composition.py  (Engine, Car)
# ---------------------------------------------------------------------------
class TestComposition:
    """Tests for Engine and Car in OOOP/oop_relation_composition.py."""

    @pytest.fixture(autouse=True)
    def setup(self):
        path = os.path.join(REPO_ROOT, "OOOP", "oop_relation_composition.py")
        mod = load_module_from_path(path, "oop_relation_composition")
        self.Engine = mod.Engine
        self.Car = mod.Car

    def test_engine_capacity(self):
        engine = self.Engine(2000)
        assert engine.capacity == 2000

    def test_engine_start(self, capsys):
        engine = self.Engine(1000)
        engine.start()
        captured = capsys.readouterr()
        assert "started" in captured.out.lower()

    def test_car_has_engine(self):
        car = self.Car("Tesla", 1000)
        assert car.brand == "Tesla"
        assert isinstance(car.engine, self.Engine)
        assert car.engine.capacity == 1000

    def test_car_start_engine(self, capsys):
        car = self.Car("BMW", 2000)
        car.start_engine()
        captured = capsys.readouterr()
        assert "BMW" in captured.out
        assert "started" in captured.out.lower()

    def test_engine_created_with_car(self):
        car = self.Car("Audi", 3000)
        assert car.engine.capacity == 3000


# ---------------------------------------------------------------------------
# OOOP/oop_relation_assocaiation.py  (Car, Driver, Cars, Person)
# ---------------------------------------------------------------------------
class TestAssociation:
    """Tests for association classes in OOOP/oop_relation_assocaiation.py."""

    @pytest.fixture(autouse=True)
    def setup(self):
        path = os.path.join(REPO_ROOT, "OOOP", "oop_relation_assocaiation.py")
        mod = load_module_from_path(path, "oop_relation_assocaiation")
        self.Car = mod.Car
        self.Driver = mod.Driver
        self.Cars = mod.Cars
        self.Person = mod.Person

    def test_car_creation(self):
        car = self.Car("Mercedes")
        assert car.name == "Mercedes"

    def test_driver_creation(self):
        driver = self.Driver("Alice")
        assert driver.name == "Alice"

    def test_driver_drive_car(self, capsys):
        car = self.Car("Tesla")
        driver = self.Driver("John")
        driver.drive_car(car)
        captured = capsys.readouterr()
        assert "John" in captured.out
        assert "Tesla" in captured.out

    def test_person_belonging(self, capsys):
        car = self.Cars("BMW")
        person = self.Person("Ali")
        person.belonging(car)
        captured = capsys.readouterr()
        assert "BMW" in captured.out
        assert "Ali" in captured.out


# ---------------------------------------------------------------------------
# OOOP/ooop_access_modifier.py  (Super, Sub)
# ---------------------------------------------------------------------------
class TestAccessModifiers:
    """Tests for access modifiers in OOOP/ooop_access_modifier.py."""

    @pytest.fixture(autouse=True)
    def setup(self):
        path = os.path.join(REPO_ROOT, "OOOP", "ooop_access_modifier.py")
        mod = load_module_from_path(path, "ooop_access_modifier")
        self.Super = mod.Super
        self.Sub = mod.Sub

    def test_public_member(self):
        obj = self.Super("pub", "prot", "priv")
        assert obj.var1 == "pub"

    def test_protected_member(self):
        obj = self.Super("pub", "prot", "priv")
        assert obj._var2 == "prot"

    def test_private_member_name_mangling(self):
        obj = self.Super("pub", "prot", "priv")
        assert obj._Super__var3 == "priv"

    def test_display_public(self, capsys):
        obj = self.Super("Hello", "World", "Secret")
        obj.displayPublicMembers()
        captured = capsys.readouterr()
        assert "Hello" in captured.out

    def test_sub_inherits_super(self):
        obj = self.Sub("a", "b", "c")
        assert isinstance(obj, self.Super)

    def test_sub_access_protected(self, capsys):
        obj = self.Sub("x", "y", "z")
        obj.accessProtectedMembers()
        captured = capsys.readouterr()
        assert "y" in captured.out

    def test_sub_access_private_via_public(self, capsys):
        obj = self.Sub("a", "b", "c")
        obj.accessPrivateMembers()
        captured = capsys.readouterr()
        assert "c" in captured.out
