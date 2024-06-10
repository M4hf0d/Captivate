from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager,
)
from .utils import file_validation


from cloudinary.models import CloudinaryField

ADVISOR_TYPES = [
        ('FIN', 'Financial'),
        ('TECH', 'Technical'),
        ('STRAT', 'Strategic'),
        ('LEGAL', 'Legal'),
        # Add more types as needed
    ]

ShareholderTypes =[ 
    ("founder", "Founder"),
    ("investor", "Investor"),
    ("advisor", "Advisor"),
]

CompanyStages = [
    ("ideation", "Ideation"),
    ("mvp", "MVP"),
    ("growth", "Growth"),
]

IndustryTypes = [
    ("finTech", "FinTech"),
    ("agriTech", "AgriTech"),
    ("edTech", "EdTech"),
]

CompanyPostions = [
    ("founder", "Founder"),
    ("coFounder", "Co-Founder"),
]

PURPOSE_CHOICES = (
        ("growth", "Long-term Growth"),
        ("income", "Regular Income"),
        ("speculation", "Short-term Speculation"),
        ("diversification", "Portfolio Diversification"),
        ("other", "Other"),
    )

FINANCIAL_SITUATION_CHOICES = (
        ("stable", "Stable"),
        ("moderate", "Moderate"),
        ("volatile", "Volatile"),
        ("other", "Other"),
    )

GENDER_CHOICES = [("M", "Male"), ("F", "Female")]



class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    """
    Update is handeled by djoser
    """

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    # image = models.ImageField(
    #     default="profile_pics/default.png", upload_to="profile_pics"
    # )
    image_path = CloudinaryField(
        "image", default="default", validators=[file_validation]
    )
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    sex = models.CharField(max_length=10, choices=GENDER_CHOICES)
    phone_number = models.CharField(max_length=20)
    onboarded = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    address = models.CharField(max_length=100, blank=True, null=True)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
    


class Industry(models.Model):
    name = models.CharField(max_length=100, null = True, blank = True)
    def __str__(self) :
        return self.name



class Shareholder(AbstractBaseUser):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    role = models.CharField(choices=ShareholderTypes, max_length=150)
    country = models.CharField(max_length=150)
    biography = models.TextField(blank=True, null=True)


    is_active = models.BooleanField(default=False)  # Temperary True
    is_admin = models.BooleanField(default=False)


    def __str__(self):
        return f"{self.email}"


class Investor(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    regain_period = models.DateField(null=True, blank=True)
    best_roi = models.IntegerField(null=True, blank=True)
    maximum_drop_invalue = models.IntegerField(null=True, blank=True)


    purpose = models.CharField(max_length=20, choices=PURPOSE_CHOICES, blank=True)
    other_purpose = models.CharField(max_length=100, blank=True)

    investment_date = models.DateField(null=True, blank=True)
    amount_of_investment = models.IntegerField(null=True, blank=True)
    Networth = models.IntegerField(null=True, blank=True)

    financial_situation = models.CharField(
        max_length=20, choices=FINANCIAL_SITUATION_CHOICES
    )
    other_financial_situation = models.CharField(max_length=100, blank=True)

    industries = models.ManyToManyField('Industry', blank= True , related_name="investors")
    
    other_industries = models.CharField(max_length=100, blank=True)

    def save(self, *args, **kwargs):
        if self.purpose != "other":
            self.other_purpose = (
                ""  # Clear other_purpose field if purpose is not "Other"
            )
        if self.financial_situation != "other":
            self.other_financial_situation = ""  # Clear other_financial_situation field if financial_situation is not "Other"
        if self.industries != "other":
            self.other_industries = (
                ""  # Clear other_industries field if industries is not "Other"
            )
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.email}:{self.user.fullname}"


class Founder(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    failed_stories = models.TextField(blank=True)
    startups_launched = models.IntegerField(default=0)

    industries = models.ManyToManyField('Industry', blank= True,  related_name="founders")
    
    other_industries = models.CharField(max_length=100, blank=True)

    def save(self, *args, **kwargs):
        if self.industries != "other":
            self.other_industries = (
                ""  # Clear other_industries field if industries is not "Other"
            )
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.email}:{self.user.fullname}"
    
class Advisor(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    Type = models.CharField(max_length=5, choices=ADVISOR_TYPES)
    ownership = models.DecimalField(max_digits=5, decimal_places=2)
    
    def __str__(self):
        return f"{self.user.email}:{self.user.fullname}"
# class Company(models.Model):
#     name = models.CharField(max_length=150, unique=True)
#     stage = models.CharField(choices=CompanyStages, max_length=100)
#     entityEnding = models.CharField(max_length=20)
#     country = models.CharField(max_length=150)
#     mainIndustry = models.CharField(choices=IndustryTypes, max_length=100)
#     descreption = models.TextField()


# class ShareholderCompany(models.Model):
#     shareholder = models.ForeignKey(
#         Shareholder, on_delete=models.CASCADE, related_name="companies"
#     )
#     company = models.ForeignKey(
#         Company, on_delete=models.CASCADE, related_name="shreholders"
#     )
#     ownership = models.IntegerField()
#     shares = models.IntegerField()
#     position = models.CharField(choices=CompanyPostions, max_length=150)
