class GenderChoices:
    Male = 'male'
    Female = 'female'
    Other = 'other'
    
    CHOICES = [
        (Male, 'male'),
        (Female, 'female'),
        (Other, 'other'),
    ]
    
    
class UserStatusChoices:
    Active = 'active'
    Inactive = "inactive"
    Removed = 'removed'
    
    CHOICES = [
        (Active, 'active'),
        (Inactive, 'inactive'),
        (Removed, 'removed'),
    ]