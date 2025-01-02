class GenderChoices:
    Male = 'male'
    Female = 'female'
    Other = 'other'
    
    CHOICES = [
        (Male, 'Male'),
        (Female, 'Female'),
        (Other, 'Other'),
    ]
    
    
class StatusChoices:
    Active = 'active'
    Inactive = "inactive"
    Removed = 'removed'
    
    CHOICES = [
        (Active, 'Active'),
        (Inactive, 'Inactive'),
        (Removed, 'Removed'),
    ]
    
class RoleChoices:
    Owner = 'owner'
    Admin = 'admin'
    Manager = 'manager'
    Staff = 'staff'
    
    CHOICES = [
        (Owner, 'Owner'),
        (Admin, 'Admin'),
        (Manager, 'Manager'),
        (Staff, 'Staff'),
    ]
    