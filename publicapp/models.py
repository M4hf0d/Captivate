from django.db import models

from django_tenants.models import TenantMixin, DomainMixin

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

class Client(TenantMixin):

    name = models.CharField(max_length=100)

    created_on = models.DateField(auto_now_add=True)

    stage = models.CharField(choices=COMPANY_STAGES, max_length=100)
    country = models.CharField(max_length=150)
    industry = models.CharField(choices=INDUSTRY_TYPES, max_length=100)
    description = models.TextField()
    
    # founders = models.ManyToManyField('Founding', through='CompanyFounder', related_name='founded_companies')
    # advisors = models.ManyToManyField('Advising', through='CompanyAdvisor', related_name='advised_companies')
    # investors = models.ManyToManyField('Investing', through='CompanyInvestor', related_name='invested_companies')

    def __str__(self):
        return self.name

class Domain(DomainMixin):

    pass