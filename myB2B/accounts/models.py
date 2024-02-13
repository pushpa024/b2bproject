from django.db import models

from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
import uuid

class User(AbstractUser):

    username = models.CharField(
        _('username'),
        max_length=150,
        help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        error_messages={
            'unique': _("Username already taken."),
        },
    )
    last_name = models.CharField(_('last name'), max_length=50, blank=True)
    email = models.EmailField(_('email address'), unique=True,
                              error_messages={
                                  'unique': _("A user with that email already exists.")
                              })
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
    forget_password_token = models.CharField(max_length =100,null=True, blank=True)

    created_on = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    modified_on = models.DateTimeField(auto_now=True, null=True, blank=True)
    login_count = models.IntegerField(editable=False, default=0)

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

class plan(models.Model):
    planID = models.IntegerField(null=False)
    planName = models.TextField(null=True, blank=True)
    Proposals = models.IntegerField(null=True,blank=True)
    price = models.IntegerField(null=True, blank=True)

class BusinessProfile(models.Model):
    # business_id = models.BigAutoField(primary_key=True)
    #user = models.ForeignKey(User, related_name="businessprofile", on_delete=models.CASCADE)
    inputFname = models.CharField(max_length=50, null=True, blank=True)
    companyName = models.CharField(max_length=50, null=True, blank=True)
    phone = models.CharField(max_length=12, null=True, blank=True)
    inputEmail = models.EmailField(unique=False, null=True, blank=True)

    verificationCall = models.BooleanField(default=False) 
    approved = models.BooleanField(default=False)
    # # email_confirmed = models.BooleanField(default=False)
    
    investor_category = models.CharField(max_length=50, null=True, blank=True)
    interested = models.CharField(max_length=50, null=True, blank=True, error_messages={
                                  'required': _("Please enter your interested business.")
                              })
    start_date = models.CharField(max_length=10, null=True, blank=True)
    interested_industry = models.CharField(max_length=50, null=True, blank=True)
    interested_locations = models.CharField(max_length=50, null=True, blank=True)
    permanent_emp = models.CharField(max_length=50, null=True, blank=True) 
    franchise_industry = models.CharField(max_length=50, null=True, blank=True)
    franchise_location = models.CharField(max_length=50, null=True, blank=True)
    business_singleLine = models.TextField(null=True, blank=True)
    business_highlights = models.TextField(null=True, blank=True)
    business_ListAll = models.TextField(null=True, blank=True)
    business_facility = models.TextField(null=True, blank=True)
    business_avgmonthsales = models.CharField(max_length=10, null=True, blank=True)
    business_yearsales = models.CharField(max_length=10, null=True, blank=True)
    business_opmpercent = models.CharField(max_length=10, null=True, blank=True)
    business_tangible = models.TextField(null=True, blank=True)
    business_phyassets_value = models.CharField(max_length=10, null=True, blank=True)
    # facility_photos = models.FileField(null=True, blank=True)
    # brochure_doc = models.FileField(max_length=10, null=True, blank=True)
    # business_proof = models.FileField(null=True,blank=True)
    uuid = models.UUIDField(default=uuid.uuid4, unique=True, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    plan = models.IntegerField(default=1,null=True, blank=True)

    class Meta:
        abstract = True
        verbose_name = _('BusinessProfile')
        verbose_name_plural = _('BusinessProfiles')    

# class Images(models.Model):
#     business_profile = models.ForeignKey(BusinessProfile, on_delete=models.CASCADE)
#     facility_photos = models.ImageField(null=True, blank=True)

class FullSale(BusinessProfile):
    # facility = models.FileField(null=True, blank=True)
    # uuid = models.UUIDField(default=uuid.uuid4, unique=True)
    
    tentSP = models.CharField(max_length=15, null=True, blank=True)
    saleReason = models.TextField(null=True, blank=True)
    user = models.ForeignKey(User, related_name="fsbusinessprofile", on_delete=models.CASCADE, null=True, blank=True)
    class Meta:
        verbose_name = _('FullSaleBusinessProfile')
        # verbose_name_plural = _('BusinessProfiles')  

    def __str__(self):
        return "%s,%s,%s" %(self.user.email , self.companyName, self.inputFname)

    def get_absolute_url(self):
        return reverse('business_sale_cust', kwargs={[str(self.id)], self.interested})

class FSImages(models.Model):
    business_profile = models.ForeignKey(FullSale, on_delete=models.CASCADE)
    facility_photos = models.ImageField(null=True, blank=True)

    def __str__(self):
        return "%s" %self.business_profile.uuid

class FSDoc(models.Model):
    business_profile = models.ForeignKey(FullSale, on_delete=models.CASCADE)
    brochure_doc = models.FileField(null=True, blank=True)

    def __str__(self):
        return "%s" %self.business_profile.uuid


class FSBusiProof(models.Model):
    business_profile = models.ForeignKey(FullSale, on_delete=models.CASCADE)
    business_proof = models.FileField(null=True,blank=True)

    def __str__(self):
        return "%s" %self.business_profile.uuid


class PartialStakeSale(BusinessProfile):
    # facility_photo = models.FileField(null=True, blank=True)
    # uuidPSS = models.UUIDField(default=uuid.uuid4, null=True, blank=True)
    
    maxStakeSell = models.CharField(max_length=15, null=True, blank=True)
    invAmtSeek = models.CharField(max_length=15, null=True, blank=True)
    investReason = models.TextField(null=True, blank=True)
    user = models.ForeignKey(User, related_name="pssbusinessprofile", on_delete=models.CASCADE, null=True, blank=True)
    class Meta:
        verbose_name = _('PartialSSBusinessProfile')

    def __str__(self):
        return "%s,%s,%s" %(self.user.email , self.companyName, self.inputFname)

    def get_absolute_url(self):
        return reverse("business_detail", args=[str(self.id)])
    

class PSSImages(models.Model):
    business_profile = models.ForeignKey(PartialStakeSale, on_delete=models.CASCADE)
    facility_photos = models.ImageField(null=True, blank=True)

    def __str__(self):
        return "%s" %self.business_profile.uuid

class PSSDoc(models.Model):
    business_profile = models.ForeignKey(PartialStakeSale, on_delete=models.CASCADE)
    brochure_doc = models.FileField(null=True, blank=True)

    def __str__(self):
        return "%s" %self.business_profile.uuid

class PSSBusiProof(models.Model): 
    business_profile = models.ForeignKey(PartialStakeSale, on_delete=models.CASCADE)
    business_proof = models.FileField(null=True,blank=True)

    def __str__(self):
        return "%s" %self.business_profile.uuid


# class LoanForBusiness(BusinessProfile):
#     collaAmount = models.CharField(max_length=15)
#     loanAmtSeek = models.CharField(max_length=15)
#     maxIntPayable = models.CharField(max_length=15)
#     yearsRepayLoan = models.CharField(max_length=8)
#     loanReason = models.TextField()
#     user = models.ForeignKey(User, related_name="loanbusinessprofile", on_delete=models.CASCADE)
#     class Meta:
#         verbose_name = _('LoanBusinessProfile')

class SellOrLeaseAssets(models.Model):
    inputFname = models.CharField(max_length=50, null=True, blank=True)
    companyName = models.CharField(max_length=50, null=True, blank=True)
    phone = models.CharField(max_length=12, null=True, blank=True)
    inputEmail = models.EmailField(unique=False, null=True, blank=True)

    verificationCall = models.BooleanField(default=False) 
    approved = models.BooleanField(default=False)
    # # email_confirmed = models.BooleanField(default=False)
    uuid = models.UUIDField(default=uuid.uuid4, unique=True, null=True, blank=True)
    investor_category = models.CharField(max_length=50, null=True, blank=True)
    interested = models.CharField(max_length=50, null=True, blank=True)
    # facility_photo = models.ImageField(null=True, blank=True)
    # brochure_doc = models.FileField(max_length=10, null=True, blank=True)
    # business_proof = models.FileField(null=True,blank=True)
    sl_assetPurchaseDate = models.CharField(max_length=15, null=True, blank=True)
    sl_indUseAsset = models.CharField(max_length=15, null=True, blank=True)
    sl_assetLocation = models.CharField(max_length=30, null=True, blank=True)
    sl_assetDetails = models.TextField( null=True, blank=True)
    sl_tanIntangible = models.TextField( null=True, blank=True)
    sl_valuePhyAsset = models.CharField(max_length=15, null=True, blank=True)
    sl_sellAtPrice = models.CharField(max_length=15, null=True, blank=True)
    sl_sellWay = models.CharField(max_length=15, null=True, blank=True)
    sl_sellReason = models.TextField( null=True, blank=True)
    user = models.ForeignKey(User, related_name="sellorleasebusinessprofile", on_delete=models.CASCADE)
    class Meta:
        verbose_name = _('SellOrLeaseBusinessProfile')

    def __str__(self):
        return "%s,%s,%s" %(self.user.email , self.companyName, self.inputFname)

    def get_absolute_url(self):
        return reverse("business_detail", kwargs={[str(self.id)], self.interested})

class SLImages(models.Model):
    business_profile = models.ForeignKey(SellOrLeaseAssets, on_delete=models.CASCADE)
    facility_photos = models.ImageField(null=True, blank=True)

    def __str__(self):
        return "%s" %self.business_profile.uuid

class SLDoc(models.Model):
    business_profile = models.ForeignKey(SellOrLeaseAssets, on_delete=models.CASCADE)
    brochure_doc = models.FileField(null=True, blank=True)

    def __str__(self):
        return "%s" %self.business_profile.uuid

class SLBusiProof(models.Model): 
    business_profile = models.ForeignKey(SellOrLeaseAssets, on_delete=models.CASCADE)
    business_proof = models.FileField(null=True,blank=True)

    def __str__(self):
        return "%s" %self.business_profile.uuid


class StripeCustomer(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    stripeCustomerId = models.CharField(max_length=255)
    stripeSubscriptionId = models.CharField(max_length=255)
    plan = models.CharField(max_length=255,null=True,blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2,null=True,blank=True)

    def __str__(self):
        return self.user.username
        

class Profile(models.Model):
    GENDER_MALE = 1
    GENDER_FEMALE = 2
    GENDER_CHOICES = [
        (GENDER_MALE, _("Male")),
        (GENDER_FEMALE, _("Female")),
    ]

    # user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
    # avatar = models.ImageField(upload_to="customers/profiles/avatars/", null=True, blank=True)
    # birthday = models.DateField(null=True, blank=True)
    # gender = models.PositiveSmallIntegerField(choices=GENDER_CHOICES, null=True, blank=True)
    # phone = models.CharField(max_length=32, null=True, blank=True)
    # address = models.CharField(max_length=255, null=True, blank=True)
    # number = models.CharField(max_length=32, null=True, blank=True)
    # city = models.CharField(max_length=50, null=True, blank=True)
    # zip = models.CharField(max_length=30, null=True, blank=True)

    # user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="%(class)s", primary_key=True)
    user = models.ForeignKey(User, related_name="profile", on_delete=models.CASCADE)
    inputFname = models.CharField(max_length=50, null=True, blank=True)
    companyName = models.CharField(max_length=50, null=True, blank=True)
    phone = models.CharField(max_length=12, null=True, blank=True)
    inputEmail = models.EmailField(unique=True, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _('Profile')
        verbose_name_plural = _('Profiles')

    # @property
    # def get_avatar(self):
    #     return self.avatar.url if self.avatar else static('assets/img/team/default-profile-picture.png')

    # def __str__(self):
    #     return self.inputFname

class UserProfile(models.Model):
    """
    This will serve as link to our user class.
    This will also have common attributes across user types.
    """
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    INV_CAT = (
        ('Business Owner / Director', 'Business Owner / Director'),
        ('Management Member', 'Management Member'),
        ('Advisor/Business Broker', 'Advisor/Business Broker'),
        )

    INTERESTED = (
        ('Full sale of business', 'Full sale of business'),
        ('Partial stake sale of business/investment', 'Partial stake sale of business/investment'),
        ('Loan for business','Loan for business'),
        ('Selling or Leasing out Business Assets', 'Selling or Leasing out Business Assets'),
        )

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="%(class)s", primary_key=True)
    input_name = models.CharField(_('input name'), max_length=50, blank=True)
    company_name = models.CharField(_('company name'), max_length=50, blank=True)
    contact_no = models.CharField(_('phone number'), max_length=12, blank=True)
    email = models.EmailField(_('input email'), unique=True)
    # inv_category = models.CharField(options = INV_CAT)
    # interested = models.CharField(options = INTERESTED)
    # start_date = models.CharField()
    # interested_industry = models.CharField()
    # interested_location = models.CharField()
    # inv_loc = models.CharField()
    # franchise_location = models.CharField()
    # single_line = models.TextField()

    
    # class Meta:
    #     abstract = True

    def get_address(self):
        address = "%s, %s, %s %s" % (self.city, self.state, self.country, self.zip)
        return address

    def get_long_gender(self):
        if str(self.gender).upper().strip() == "M":
            return "Male"
        elif str(self.gender).upper().strip() == "F":
            return "Female"
        else:
            return self.gender

