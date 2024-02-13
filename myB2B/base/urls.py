from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static 


urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('progress/', views.InProgressView.as_view(), name='in_progress'),
    path('QA/', views.QuesAnsw.as_view(), name='ques_answ'),
    path('contactus/', views.ContactUs.as_view(), name='contactus'),
    path('buybusiness/', views.BuyBusinessView.as_view(), name='buybusiness'),
    path('franchiesbusiness/', views.FranchiesBusinessView.as_view(), name='franchiesbusiness'),
    path('investinbusiness/', views.InvestInBusinessView.as_view(), name='investinbusiness'),
    path('memorandum/', views.MemorandumView.as_view(), name='memorandum'),
    path('regAdvisor/', views.RegAdvisorView.as_view(), name='regAdvisor'),
    path('sellOurBusiness/', views.SellOurBusinessView.as_view(), name='sellyourBusiness'),
    path('valueBusiness/', views.ValueBusinessView.as_view(), name='valueBusiness'),
    path('findinvestor/', views.FindInvestorView.as_view(), name='findinvestor'),
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),
    path('investor/', views.Sale_InvestorView.as_view(), name='investor_in'),
    path('franchise/', views.Sale_FranchiseView.as_view(), name='franchise_in'),
    path('business/', views.Sale_BusinessView.as_view(), name='business_in'),
    path('setting/', views.User_SettingView.as_view(), name='user_setting'),
    path('testimonial/',views.TestmonialView.as_view(), name='testimonial'),
    path('blog/',views.BlogView.as_view(), name='blog'),
    path('delete_user/<pk>', views.deleteUser,name="delete"), 
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)