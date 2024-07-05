from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin

from cloudinary.models import CloudinaryField
from .utils import file_validation

TITLE_CHOICES = [
    ("Mr", "Mr"),
    ("Ms", "Ms"),
    ("Mrs", "Mrs"),
    ("Mx", "Mx"),
    ("Dr", "Dr"),
    ("Prof", "Prof"),
    ("HRH", "HRH"),
    ("Sheikh", "Sheikh"),
]

ADVISOR_TYPES = [
    ('FIN', 'Financial'),
    ('TECH', 'Technical'),
    ('STRAT', 'Strategic'),
    ('LEGAL', 'Legal'),
    ('HR', 'Human Resources'),
    ('MARK', 'Marketing'),
    ('SALES', 'Sales'),
    ('OTHER', 'Other'),
]

SHAREHOLDER_TYPES = [
    ("founder", "Founder"),
    ("investor", "Investor"),
    ("advisor", "Advisor"),
    ("employee", "Employee"),
    ("board", "Board Member"),
]

COMPANY_STAGES = [
    ("ideation", "Ideation"),
    ("mvp", "MVP"),
    ("growth", "Growth"),
]


INDUSTRY_TYPES = [
    ("finTech", "FinTech"),
    ("agriTech", "AgriTech"),
    ("edTech", "EdTech"),
]

INDUSTRY_TYPES = [
    ("finTech", "FinTech"),
    ("agriTech", "AgriTech"),
    ("edTech", "EdTech"),
]

COMPANY_POSITIONS = [
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

GENDER_CHOICES = [
    ("M", "Male"),
    ("F", "Female"),
]

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    image_path = CloudinaryField("image", default="default", validators=[file_validation])
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    title = models.CharField(max_length=10, choices=TITLE_CHOICES, default="Mr")
    phone_number = models.CharField(max_length=20)
    onboarded = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    address = models.CharField(max_length=100, blank=True, null=True)
    Networth = models.IntegerField(null=True, blank=True)
    joined_at = models.DateTimeField(auto_now_add=True)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email


class Industry(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name


class Founding(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING, related_name="founders")
    company = models.ForeignKey("Company", on_delete=models.DO_NOTHING, related_name="founders")
    Role = models.CharField(max_length = 150, null = True, blank = True) 
    Biography = models.TextField(null = True, blank = True)
    ownership = models.DecimalField(max_digits=5, decimal_places=2, blank = True, null = True)

    class Meta:
        verbose_name = "Founding"
        verbose_name_plural = "Foundings"

class Investing(models.Model):
    regain_period = models.DateField(null=True, blank=True)
    best_roi = models.IntegerField(null=True, blank=True)
    maximum_drop_invalue = models.IntegerField(null=True, blank=True)
    purpose = models.CharField(max_length=20, choices=PURPOSE_CHOICES, blank=True)
    other_purpose = models.CharField(max_length=100, blank=True)
    investment_date = models.DateField(auto_now_add=True)
    amount_of_investment = models.IntegerField(null=True, blank=True)
    # financial_situation = models.CharField(max_length=20, choices=FINANCIAL_SITUATION_CHOICES)
    # other_financial_situation = models.CharField(max_length=100, blank=True)
    industries = models.ManyToManyField('Industry', blank=True, related_name="Investings")
    other_industries = models.CharField(max_length=100, blank=True)
    ownership = models.DecimalField(max_digits=5, decimal_places=2, blank = True, null = True)

    def save(self, *args, **kwargs):
        if self.purpose != "other":
            self.other_purpose = ""
        if self.industries != "other":
            self.other_industries = ""
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Investing"
        verbose_name_plural = "Investings"

class Advising(models.Model):
    atype = models.CharField(max_length=5, choices=ADVISOR_TYPES)
    ownership = models.DecimalField(max_digits=5, decimal_places=2, blank = True, null = True)

    class Meta:
        verbose_name = "Advisor"
        verbose_name_plural = "Advisors"




class Company(models.Model):
    name = models.CharField(max_length=150, unique=True)
    stage = models.CharField(choices=COMPANY_STAGES, max_length=100)
    country = models.CharField(max_length=150)
    industry = models.CharField(choices=INDUSTRY_TYPES, max_length=100)
    description = models.TextField()

    # founders = models.ManyToManyField('Founding', through='CompanyFounder', related_name='founded_companies')
    # advisors = models.ManyToManyField('Advising', through='CompanyAdvisor', related_name='advised_companies')
    # investors = models.ManyToManyField('Investing', through='CompanyInvestor', related_name='invested_companies')

    def __str__(self):
        return self.name