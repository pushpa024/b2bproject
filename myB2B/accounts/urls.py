from django.urls import path
from django.conf import settings
from django.conf.urls.static import static 
from . import views

# app_name = 'accounts'
urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login-new'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('register/', views.UserRegistration.as_view(), name='register-new'),
    # path('profile1/', views.UserProfile.as_view(), name='profile1'),
    # path('profile/', views.ProfileView.as_view(), name='profile'),
    # path('businessprofile/', views.BusinessProfile.as_view(), name='businessprofile'),
    path('businessprofile/', views.addBusinessProfile, name='addbusinessprofile'),
    path('franchiseprofile/', views.FranchiseProfile.as_view(), name='franchiseprofile'),
    path('investorbuyer/', views.InvestorBuyerProfile.as_view(), name='investorbuyer'),
    path('successpage/', views.successpage, name='successpage'),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),
    path('business_sale_cust/<int:id>/<str:btype>/', views.BusinessSaleCustomerLoggedIn, name='business_sale_cust'),
    path("<int:id>/<str:btype>/", views.BusinessSaleCustomerLoggedIn, name="business_detail"),
    path('forgetpassword/',views.ForgetPassword, name='forgetpassword'),
    path('changepassword/<token>/',views.ChangePassword, name='changepassword'),
    # path('<slug:post>',views.BusinessSaleCustomerLoggedIn, name='business_sale_cust'), 
    path('payment', views.stripepay, name='stripepay'),
    path('config/', views.stripe_config), 
    path('create-checkout-session/', views.create_checkout_session),
    path('success_payment', views.successStripe, name='successStripe'),
    path('cancel_payment', views.cancelStripe, name='cancelStripe'),
    path('webhook/stripe', views.stripe_webhook_view, name="stripe_webhook_view"),
    path('business_profile_list/',views.HeaderProfile.as_view(), name='business_profile_list'),
    path('load/', views.load_more, name='load')
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
