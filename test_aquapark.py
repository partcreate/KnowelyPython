import unittest
from classes.aquapark import IntegerRange, Visitor, ChildrenSlideLimitationValidator, AdultSlideLimitationValidator, Slide


class TestIntegerRange(unittest.TestCase):
    """Test cases for the IntegerRange descriptor class."""
    
    def test_valid_value(self):
        """Test that valid values are accepted."""
        class TestClass:
            value = IntegerRange(1, 10)
            
            def __init__(self, val):
                self.value = val
        
        # Test with valid value
        obj = TestClass(5)
        self.assertEqual(obj.value, 5)
        
        # Test changing to another valid value
        obj.value = 8
        self.assertEqual(obj.value, 8)
    
    def test_invalid_type(self):
        """Test that non-integer values raise TypeError."""
        class TestClass:
            value = IntegerRange(1, 10)
            
            def __init__(self, val):
                self.value = val
        
        # Test with string value
        with self.assertRaises(TypeError):
            TestClass("not an integer")
        
        # Test changing to float
        obj = TestClass(5)
        with self.assertRaises(TypeError):
            obj.value = 5.5
    
    def test_out_of_range(self):
        """Test that values outside the specified range raise ValueError."""
        class TestClass:
            value = IntegerRange(1, 10)
            
            def __init__(self, val):
                self.value = val
        
        # Test with value below minimum
        with self.assertRaises(ValueError):
            TestClass(0)
        
        # Test with value above maximum
        with self.assertRaises(ValueError):
            TestClass(11)
        
        # Test changing to out of range value
        obj = TestClass(5)
        with self.assertRaises(ValueError):
            obj.value = 20


class TestVisitor(unittest.TestCase):
    """Test cases for the Visitor class."""
    
    def test_visitor_creation(self):
        """Test that a Visitor can be created with valid attributes."""
        visitor = Visitor(name="John", age=25, weight=70, height=175)
        
        self.assertEqual(visitor.name, "John")
        self.assertEqual(visitor.age, 25)
        self.assertEqual(visitor.weight, 70)
        self.assertEqual(visitor.height, 175)


class TestChildrenSlideLimitationValidator(unittest.TestCase):
    """Test cases for the ChildrenSlideLimitationValidator class."""
    
    def test_valid_child(self):
        """Test that valid child parameters are accepted."""
        validator = ChildrenSlideLimitationValidator(age=10, weight=35, height=100)
        
        self.assertEqual(validator.age, 10)
        self.assertEqual(validator.weight, 35)
        self.assertEqual(validator.height, 100)
    
    def test_invalid_age(self):
        """Test that invalid age raises ValueError."""
        # Age too young
        with self.assertRaises(ValueError):
            ChildrenSlideLimitationValidator(age=3, weight=35, height=100)
        
        # Age too old
        with self.assertRaises(ValueError):
            ChildrenSlideLimitationValidator(age=15, weight=35, height=100)
    
    def test_invalid_weight(self):
        """Test that invalid weight raises ValueError."""
        # Weight too low
        with self.assertRaises(ValueError):
            ChildrenSlideLimitationValidator(age=10, weight=15, height=100)
        
        # Weight too high
        with self.assertRaises(ValueError):
            ChildrenSlideLimitationValidator(age=10, weight=55, height=100)
    
    def test_invalid_height(self):
        """Test that invalid height raises ValueError."""
        # Height too short
        with self.assertRaises(ValueError):
            ChildrenSlideLimitationValidator(age=10, weight=35, height=75)
        
        # Height too tall
        with self.assertRaises(ValueError):
            ChildrenSlideLimitationValidator(age=10, weight=35, height=125)


class TestAdultSlideLimitationValidator(unittest.TestCase):
    """Test cases for the AdultSlideLimitationValidator class."""
    
    def test_valid_adult(self):
        """Test that valid adult parameters are accepted."""
        validator = AdultSlideLimitationValidator(age=30, weight=80, height=180)
        
        self.assertEqual(validator.age, 30)
        self.assertEqual(validator.weight, 80)
        self.assertEqual(validator.height, 180)
    
    def test_invalid_age(self):
        """Test that invalid age raises ValueError."""
        # Age too young
        with self.assertRaises(ValueError):
            AdultSlideLimitationValidator(age=13, weight=80, height=180)
        
        # Age too old
        with self.assertRaises(ValueError):
            AdultSlideLimitationValidator(age=61, weight=80, height=180)
    
    def test_invalid_weight(self):
        """Test that invalid weight raises ValueError."""
        # Weight too low
        with self.assertRaises(ValueError):
            AdultSlideLimitationValidator(age=30, weight=45, height=180)
        
        # Weight too high
        with self.assertRaises(ValueError):
            AdultSlideLimitationValidator(age=30, weight=125, height=180)
    
    def test_invalid_height(self):
        """Test that invalid height raises ValueError."""
        # Height too short
        with self.assertRaises(ValueError):
            AdultSlideLimitationValidator(age=30, weight=80, height=115)
        
        # Height too tall
        with self.assertRaises(ValueError):
            AdultSlideLimitationValidator(age=30, weight=80, height=225)


class TestSlide(unittest.TestCase):
    """Test cases for the Slide class."""
    
    def test_slide_creation(self):
        """Test that a Slide can be created with valid attributes."""
        slide = Slide(name="Fun Slide", limitation_class=ChildrenSlideLimitationValidator)
        
        self.assertEqual(slide.name, "Fun Slide")
        self.assertEqual(slide.limitation_class, ChildrenSlideLimitationValidator)
    
    def test_can_access_children_slide(self):
        """Test the can_access method for a children's slide."""
        children_slide = Slide(name="Kids Slide", limitation_class=ChildrenSlideLimitationValidator)
        
        # Valid child visitor
        valid_child = Visitor(name="Tommy", age=10, weight=35, height=100)
        self.assertTrue(children_slide.can_access(valid_child))
        
        # Invalid child visitor (too heavy)
        invalid_child = Visitor(name="Heavy Tommy", age=10, weight=55, height=100)
        self.assertFalse(children_slide.can_access(invalid_child))
        
        # Adult visitor (too old)
        adult = Visitor(name="John", age=30, weight=80, height=180)
        self.assertFalse(children_slide.can_access(adult))
    
    def test_can_access_adult_slide(self):
        """Test the can_access method for an adult slide."""
        adult_slide = Slide(name="Extreme Slide", limitation_class=AdultSlideLimitationValidator)
        
        # Valid adult visitor
        valid_adult = Visitor(name="John", age=30, weight=80, height=180)
        self.assertTrue(adult_slide.can_access(valid_adult))
        
        # Invalid adult visitor (too light)
        invalid_adult = Visitor(name="Light John", age=30, weight=45, height=180)
        self.assertFalse(adult_slide.can_access(invalid_adult))
        
        # Child visitor (too young)
        child = Visitor(name="Tommy", age=10, weight=35, height=100)
        self.assertFalse(adult_slide.can_access(child))


if __name__ == "__main__":
    unittest.main()