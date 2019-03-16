from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.views.generic import ListView, DeleteView, CreateView, UpdateView, FormView
from django.db.models import Sum, Count
from .models import User, balans, spozHistory, Private_abonent, House, Comercial, gadget_hw, gadget_HW_meter, gadget_HW_meter_max_dem_h, meterDataPrivate
from django.http import JsonResponse
import datetime
from calendar import monthrange
from .forms import UserMeterDate


# def profile_balance(request):
#     users = "Mark"
#     return render(request, 'user/profile.html', {'users':users})
# Create your views here.
def login(request):
    if request.method =='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(request, f'Ласкаво просимо, {username}')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'user/login.html', {'form': form, 'title':'Вхід'})

@login_required
def profile(request):
    users = User.objects.all()
    return render(request, 'user/profile.html', {'users':users})

@login_required
def my_redirect(request):
    if request.user.is_staff == False:
        return redirect('/dashboard/')
    elif request.user.is_staff == True:
        return redirect('/dashboard/')
    elif request.user.is_superuser == True:
        return redirect('/dashboard/')

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Ваш пароль успішно змінено!')
            return redirect('change_password')
        else:
            messages.error(request, 'Будь-ласка, виправте помилкуІ.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'user/change_password.html', {
        'form': form
    })


# def setMeterDate(request):
#     if request.method == "POST":
#         form = UserMeterDate(request.POST, instance=request.user)
#         if form.is_valid():
#             form.save()
#             return redirect('dashboard')
#             messages.success(request, 'Your password was successfully updated!')
#         else:
#             messages.error(request, 'Please correct the error below.')
#     else:
#         form = UserMeterDate()
#     data = {
#         'form': form
#     }
#     return render(request, 'user/forms.html', data)

# def setMeterDate(request):
#     now = datetime.date.today()
#     date=now.strftime("%Y-%m")+'-01'
#     avtoMaterDate = meterDataPrivate.objects.filter(account=self.request.user, date=date).values('pokazT0')
#     if request.method == 'POST':
#         userMeterDate = userMeterDate(request.POST)
#         if form.is_valid():
#             different= avtoMaterDate - userMeterDate
#             if(different<50 and different>(-50)):
#                 userMeterDate.save()
#                 messages.success(request, 'Your password was successfully updated!')
#                 return redirect('dashboard')
#             else:
#                 messages.error(request, 'Please correct the error below.')
#         else:
#             messages.error(request, 'Please correct the error below.')
#     else:
#             form = userMeterDate(request.user)
#
#     return render(request, 'user/dashboard.html', {
#         'form': form
#     })



class ShowDashboard(ListView, FormView):


    model = balans
    form_class = UserMeterDate
    template_name = 'user/dashboard.html'
    ordering = ['-date']



    def get_initial(self):
        if self.request.user.is_staff == False:
            now = datetime.date.today()
            date=now.strftime("%Y-%m")+'-01'
            initial = super(ShowDashboard, self).get_initial()
            lastPokaz = meterDataPrivate.objects.filter(account=self.request.user.username, date='2019-02-01').values('pokazT0')
            if self.request.user.is_authenticated:
                initial.update({'account': self.request.user.username,
                                'pokazT0':lastPokaz[0]['pokazT0'],
                                'date': date })
            return initial

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        pokazT0=form.cleaned_data['pokazT0']
        lastPokaz = meterDataPrivate.objects.filter(account=self.request.user.username, date='2019-02-01').values('pokazT0')
        if(pokazT0<lastPokaz[0]['pokazT0']+10 and pokazT0>lastPokaz[0]['pokazT0']-10):
            form.instance.save()
            return redirect('dashboard')
        else:
            return self.form_invalid(form)

    def form_invalid(self, form):
        pokazT0=form.cleaned_data['pokazT0']
        lastPokaz = meterDataPrivate.objects.filter(account=self.request.user.username, date='2019-02-01').values('pokazT0')
        if(pokazT0>lastPokaz[0]['pokazT0']+10 or pokazT0<lastPokaz[0]['pokazT0']-10):
            messages.info(self.request, "Дані не були надіслані! Показник не може відрізнятись більше ніж на 10 одиниць")
        else:
            messages.info(self.request, "--->"+str(lastPokaz[0]['pokazT0']+10))
        return redirect('dashboard')

    # def _form_view(request, template_name='user/includes/forms.html', form_class=ContactForm):
    #     if request.method == 'POST':
    #         form = form_class(request.POST)
    #         if form.is_valid():
    #             pass  # does nothing, just trigger the validation
    #         else:
    #             form = form_class()
    #             return render(request, template_name, {'form': form})

    def get_context_data(self, **kwards):

        if self.request.user.is_staff == False:
            house = Private_abonent.objects.filter(account=self.request.user).values('house_number')
            ctx = super(ShowDashboard, self).get_context_data(**kwards)
            ctx['title'] = self.request.user
            ctx['usersid'] = self.request.user
            ctx['adress'] = House.objects.filter(number=house[0]['house_number']).values('number', 'street')
            ctx['abonent'] = Private_abonent.objects.filter(account=self.request.user).values('first_name', 'last_name', 'sur_name', 'house_number', 'apartament', 'meter_sn')
            ctx['balans'] = balans.objects.filter(account=self.request.user).values('saldo', 'date', 'comment')
            ctx['balans_sum'] = balans.objects.filter(account=self.request.user).aggregate(Sum('saldo'))
            ctx['history'] = spozHistory.objects.filter(account=self.request.user).values('date', 'pokaz1', 'pokaz2','different', 'uah')
            return ctx

        elif self.request.user.is_staff == True:
            diff = gadget_HW_meter.objects.filter(gadget_HW_id_id='2').values("kWh","meterDate")
            meterDate = gadget_HW_meter.objects.filter(gadget_HW_id_id='2').values("meterDate")
            kwh = []
            kwhM = []

            for i in diff:
                kwh.append((i['kWh'], i['meterDate']))

            now = datetime.date.today()
            date=now.strftime("%y%m")+'0108'

            Max=0
            Min=9999999999
            Count=0
            lastValue=kwh[-1][0]
            dayCount=[]
            dayAverage=[]
            for i in range(len(kwh)):
                strDate=str(kwh[i][1])
                first = datetime.datetime.strptime(str(kwh[i][1]),'%y%m%d%H%M%S')
                second = first.strftime('%Y-%m-%d %H:%M:%S')
                if(str(date)==strDate[0:8]):
                    Count=kwh[i][0]
                if('08'==strDate[6:8]):
                    dayCount.append(kwh[i][0])
                if i+1 == len(kwh):
                    break
                if(kwh[i+1][0]-kwh[i][0]*120>Max):
                    Max = kwh[i+1][0]-kwh[i][0]*120
                if(kwh[i+1][0]-kwh[i][0]*120<Min):
                    Min = kwh[i+1][0]-kwh[i][0]*120
                kwhM.append(((kwh[i+1][0]-kwh[i][0])*120, kwh[i][0]*120, str(datetime.datetime.strptime(str(second),'%Y-%m-%d %H:%M:%S'))))

            Count=(lastValue-Count)*120
            for i in range(len(dayCount)):
                if i+1 == len(dayCount):
                    break
                dayAverage.append((dayCount[i+1]-dayCount[i])*120)
            Average=sum(dayAverage)/len(dayAverage)
            day=monthrange(int(now.strftime("%Y")), int(now.strftime("%m")))
            Forecast=Average*day[1]

            ctx = super(ShowDashboard, self).get_context_data(**kwards)
            ctx['title'] = self.request.user
            ctx['dayAverage'] =Average
            ctx['Forecast'] =Forecast
            ctx['min'] =Min
            ctx['count'] =Count
            ctx['kwhM'] =kwhM
            ctx['GHW'] = gadget_hw.objects.filter(contract='11111111').values('id')
            ctx['GHW_meter'] = gadget_HW_meter.objects.filter(gadget_HW_id_id='2').values('kWh', "kVArh_p", 'kVArh_n', 'kVAh', 'cur_sum_V', 'cur_L1_V', 'cur_L2_V', 'cur_L3_V', 'cur_F', 'meterDate', 'gadget_HW_id')

            return ctx
