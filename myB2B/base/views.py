from django.shortcuts import render, redirect
from django.views import View
from accounts.models import FullSale, PartialStakeSale, SellOrLeaseAssets
from accounts.models import User
from django.contrib import messages


class HomeView(View):
    template_name = "base/home.html"

    def get(self, request, *args, **kwargs):
        context = {
            "message": "This is Home page",
            "title": "Home | Huntment"
        }
        return render(request, self.template_name, context)


class AboutView(View):
    template_name = "base/about.html"

    def get(self, request, *args, **kwargs):
        context = {
            "message": "This is About Us page",
            "title": "About Us | Huntment"
        }
        return render(request, self.template_name, context)

class InProgressView(View):
    template_name = "base/in_progress_page.html"

    def get(self, request, *args, **kwargs):
        context = {
            "title": "In Progress | Huntment"
        }
        return render(request, self.template_name, context)

class QuesAnsw(View):
    template_name = "base/ques_answ.html"

    def get(self, request, *args, **kwargs):
        context = {
            "message": "This is Q & A page",
            "title": "Q&A | Huntment"
        }
        return render(request, self.template_name, context)

class ContactUs(View):
    template_name = "base/contact_us.html"

    def get(self, request, *args, **kwargs):
        context = {
            "message": "This is Contact us page",
            "title": "Contact Us | Huntment"
        }
        return render(request, self.template_name, context)

class QuesAnsw(View):
    template_name = "base/ques_answ.html"

    def get(self, request, *args, **kwargs):
        context = {
            "message": "This is Q & A page",
            "title": "Q&A | Huntment"
        }
        return render(request, self.template_name, context)

class BuyBusinessView(View):
    template_name = "base/how-to/buybusiness.html"

    def get(self, request, *args, **kwargs):
        context = {
            "message": "How to buy business page",
            "title": "Buy Business | Huntment"
        }
        return render(request, self.template_name, context)

class FranchiesBusinessView(View):
    template_name = "base/how-to/franchiesbusiness.html"

    def get(self, request, *args, **kwargs):
        context = {
            "message": "How to franchiese business page",
            "title": "Franchiese Business | Huntment"
        }
        return render(request, self.template_name, context)

class InvestInBusinessView(View):
    template_name = "base/how-to/investinbusiness.html"

    def get(self, request, *args, **kwargs):
        context = {
            "message": "How to invest in business page",
            "title": "Invest in Business | Huntment"
        }
        return render(request, self.template_name, context)

class MemorandumView(View):
    template_name = "base/how-to/memorandum.html"

    def get(self, request, *args, **kwargs):
        context = {
            "message": "Memorandum page",
            "title": "Memorandum | Huntment"
        }
        return render(request, self.template_name, context) 

class RegAdvisorView(View):
    template_name = "base/how-to/reg-advi.html"

    def get(self, request, *args, **kwargs):
        context = {
            "message": "Advisor register page",
            "title": "Advisor register | Huntment"
        }
        return render(request, self.template_name, context) 

class SellOurBusinessView(View):
    template_name = "base/how-to/sellourbusiness.html"

    def get(self, request, *args, **kwargs):
        context = {
            "message": "Sell our Business page",
            "title": "Sell our Business | Huntment"
        }
        return render(request, self.template_name, context) 

class ValueBusinessView(View):
    template_name = "base/how-to/valuebusiness.html"

    def get(self, request, *args, **kwargs):
        context = {
            "message": "Business value page",
            "title": "Business value | Huntment"
        }
        return render(request, self.template_name, context) 

class FindInvestorView(View):
    template_name = "base/how-to/findinvestor.html"

    def get(self, request, *args, **kwargs):
        context = {
            "message": "Find investor page",
            "title": "find investor | Huntment"
        }
        return render(request, self.template_name, context) 

class DashboardView(View):
    template_name = "base/header-menu/dash.html"

    def get(self, request, *args, **kwargs):
        context = {
            "message": "Dashboard page",
            "title": "Dashboard | Huntment"
        }
        return render(request, self.template_name, context) 

class Sale_InvestorView(View):
    template_name = "base/header-menu/investor_sale.html"

    def get(self, request, *args, **kwargs):
        context = {
            "message": "logged in investor page",
            "title": "logged in investor | Huntment"
        }
        return render(request, self.template_name, context)

class Sale_FranchiseView(View):
    template_name = "base/header-menu/franchise_sale.html"

    def get(self, request, *args, **kwargs):
        context = {
            "message": "logged in franchise_sale page",
            "title": "logged in franchise_sale | Huntment"
        }
        return render(request, self.template_name, context)

class TestmonialView(View):
    template_name = "base/testimonial.html"

    def get(self, request, *args, **kwargs):
        context = {
            "message": "testimonial page",
            "title": "testimonial | Huntment"
        }
        return render(request, self.template_name, context)

class BlogView(View):
    template_name = "base/blog.html"

    def get(self, request, *args, **kwargs):
        context = {
            "message": "Blog page",
            "title": "Blog | Huntment"
        }
        return render(request, self.template_name, context)

class Sale_BusinessView(View):
    template_name = "base/header-menu/business_sale1.html"

    def get(self, request, *args, **kwargs):

        business_list_fs = FullSale.objects.all() 
        business_list_fs_count = FullSale.objects.filter(approved=1).count()
        print(business_list_fs_count)
        business_list_pss = PartialStakeSale.objects.all()
        business_list_pss_count = PartialStakeSale.objects.filter(approved=1).count()
        business_list_sl = SellOrLeaseAssets.objects.all()
        business_list_sl_count = SellOrLeaseAssets.objects.filter(approved=1).count()
        total_business = business_list_sl_count+business_list_pss_count+business_list_fs_count
        print(total_business)
        context = {
            "form_fs": business_list_fs,
            "form_pss": business_list_pss,
            "form_sl": business_list_sl,
            "total_business": total_business,
            "message": "logged in business_sale",
            "title": "logged in business_sale | Huntment"
        }
        return render(request, self.template_name, context)

class User_SettingView(View):
    template_name = "base/components/user_settings_page.html"

    def get(self, request, *args, **kwargs):
        context = {
            "message": "user_settings page",
            "title": "user_settings | Huntment"
        }
        return render(request, self.template_name, context)

def deleteUser(request,pk):
    User.objects.filter(id=pk).delete()
    messages.success(request, "user deleted successfully!")
    return redirect('home')