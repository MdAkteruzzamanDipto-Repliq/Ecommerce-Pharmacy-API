class GenderChoices:
    Male = 'male'
    Female = 'female'
    Other = 'other'
    
    CHOICES = [
        (Male, 'Male'),
        (Female, 'Female'),
        (Other, 'Other'),
    ]
    
    
class UserStatusChoices:
    Active = 'active'
    Inactive = "inactive"
    Removed = 'removed'
    
    CHOICES = [
        (Active, 'Active'),
        (Inactive, 'Inactive'),
        (Removed, 'Removed'),
    ]