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

class OwnerRoleChoices:
    Admin = 'admin'
    Manager = 'manager'
    Staff = 'staff'
    
    CHOICES = [
        (Admin, 'Admin'),
        (Manager, 'Manager'),
        (Staff, 'Staff'),
    ]
    
class AdminRoleChoices:
    Manager = 'manager'
    Staff = 'staff'
    
    CHOICES = [
        (Manager, 'Manager'),
        (Staff, 'Staff'),
    ]

class ManagerRoleChoices:
    Staff = 'staff'
    
    CHOICES = [
        (Staff, 'Staff'),
    ]

class ProductStockChoices:
    InStock = 'in_stock'
    OutOfStock = 'out_of_stock'
    
    CHOICES = [
        (InStock, 'In Stock'),
        (OutOfStock, 'Out of Stock'),
    ]

class ProductStatusChoices:
    Draft = 'draft'
    Published = 'published'
    
    CHOICES = [
        (Draft, 'Draft'),
        (Published, 'Published'),
    ]
