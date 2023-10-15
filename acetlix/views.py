from django.shortcuts import render
from django.http import JsonResponse,HttpResponseRedirect
from django.urls import reverse
from django.core.mail import send_mail

def email_home(request):
    if request.method == 'POST':
        name = request.POST['name']
        message = request.POST.get('textarea')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        if name == None or email ==  None:
            return JsonResponse({"message":"SOME ERROR SUBMITTING YOUR FORM, PLEASE CHECK YOUR EMAIL AND NAME"})
        else:
            if 'has_submitted' in request.session:
                return JsonResponse({'message': 'WE HAVE RECEVIED YOUR QUERY!! THANKS'})
            subject = 'New query From Contact Form'
            message_ = f'Name: {name}\nEmail: {email}\nMessage: {message}\nPhoneNumber:{phone}'
            from_email = 'karandeep888singh@gmail.com'  # Replace with your email address
            to_email = ['acetlix0@gmail.com']  # Replace with your email address or a list of email addresses
            send_mail(subject, message_, from_email, to_email, fail_silently=False)
            request.session['has_submitted'] = True
            return JsonResponse({"message":"WE HAVE RECEVIED YOUR QUERY!! THANKS"})
    else:
        return HttpResponseRedirect(reverse('home'))


def home(request):
    return render(request,'home.html')