# ==============================================================================
# OOP CONCEPTS DEFINITION & SUMMARY
# ==============================================================================
#
# 1. CONSTRUCTOR (__init__):
#    - Role: Initializes a newly created instance. Sets instance-specific attributes.
#    - Signature: Takes `self` as the first argument.
#    - Trigger: Automatically called when instantiating a class: `obj = MyClass()`.
#
# 2. DESTRUCTOR (__del__):
#    - Role: Performs teardown or cleanup operations (e.g., releasing resources).
#    - Signature: Takes `self` as the first argument.
#    - Trigger: Automatically called when an object's reference count reaches 0 
#      or when explicitly removed via `del obj`.
#
# 3. STATIC VARIABLE (Class Variable):
#    - Role: A variable shared across ALL instances of the class, stored in class state.
#    - Behavior: Changing it via the class (`MyClass.var = x`) updates it for all 
#      instances that haven't overridden it locally.
#
# 4. STATIC METHOD (@staticmethod):
#    - Role: A utility function bound to the class namespace that does NOT access 
#      or modify instance (`self`) or class (`cls`) state.
#    - Decorator: Uses `@staticmethod`. Takes standard arguments (no `self` or `cls`).
#
# 5. CLASS METHOD (@classmethod):
#    - Role: Operates on class-level state. Can modify static variables or act as 
#      alternative factory constructors.
#    - Decorator: Uses `@classmethod`. Takes `cls` as the first argument.
# ==============================================================================


class Student:
    # --------------------------------------------------------------------------
    # STATIC VARIABLES (Shared state across all Student instances)
    # --------------------------------------------------------------------------
    school_name: str = "Global Academy"
    total_students: int = 0

    # --------------------------------------------------------------------------
    # CONSTRUCTOR (__init__)
    # --------------------------------------------------------------------------
    def __init__(self, name: str, grade: float):
        self.name = name          # Instance variable
        self.grade = grade        # Instance variable
        
        # Increment shared static counter upon creation
        Student.total_students += 1
        print(f"[CONSTRUCTOR] Student '{self.name}' enrolled. (Total: {Student.total_students})")

    # --------------------------------------------------------------------------
    # STATIC METHOD (@staticmethod)
    # Utility function: Does not rely on self (instance) or cls (class) state.
    # --------------------------------------------------------------------------
    @staticmethod
    def is_passing_grade(score: float) -> bool:
        """Determines if a given grade score meets passing criteria (>= 50)."""
        return score >= 50.0

    # --------------------------------------------------------------------------
    # CLASS METHOD (@classmethod)
    # Operates on class-level attributes / Alternative factory constructor.
    # --------------------------------------------------------------------------
    @classmethod
    def from_csv_string(cls, data: str) -> "Student":
        """Factory constructor that parses a CSV string 'Name,Grade'."""
        name, grade_str = data.split(",")
        return cls(name=name.strip(), grade=float(grade_str))

    # --------------------------------------------------------------------------
    # DESTRUCTOR (__del__)
    # --------------------------------------------------------------------------
    def __del__(self):
        # Decrement shared static counter upon destruction
        Student.total_students -= 1
        print(f"[DESTRUCTOR] Student '{getattr(self, 'name', 'Unknown')}' removed. (Remaining: {Student.total_students})")


# ==============================================================================
# EXECUTION & DEMONSTRATION
# ==============================================================================
if __name__ == "__main__":
    print("=== 1. STATIC METHOD USAGE ===")
    # Can be called directly on the class without creating an instance
    print(f"Is 75 passing? {Student.is_passing_grade(75)}")
    print(f"Is 42 passing? {Student.is_passing_grade(42)}")

    print("\n=== 2. CONSTRUCTOR & STATIC VARIABLES ===")
    s1 = Student("Alice", 88.5)
    s2 = Student("Bob", 45.0)

    # Accessing static variables from class and instances
    print(f"\nSchool Name (Class access): {Student.school_name}")
    print(f"School Name (Instance access): {s1.school_name}")
    print(f"Total Enrolled Students: {Student.total_students}")

    print("\n=== 3. CLASS METHOD FACTORY CONSTRUCTOR ===")
    s3 = Student.from_csv_string("Charlie, 92.0")

    print("\n=== 4. DESTRUCTOR DEMONSTRATION ===")
    # Explicitly deleting an object triggers __del__ immediately
    print("Deleting 's2' explicitly...")
    del s2

    print(f"\nTotal Enrolled Students after deletion: {Student.total_students}")
    print("\nProgram execution finishing...")