from django.shortcuts import render
#from contact_us.contact import contact_form
#from contact_us.models import ContactForm
from django.core.mail import send_mail

def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        '''data=request.POST
        name= data.get('name')
        email= data.get('email')
        #subject= data('subject')
        message= data.get('message')
        #qa_object = ContactForm(name=name,email=email, subject=subject, message=message).save()
    '''
        # send an email
        send_mail(
            'Message from ' + name, # subject
             message, # message
             email, # from email
             ['itsprince.cr7@gmail.com'], # To email
             fail_silently=False,
        )

        return render(request,'thanku1.html', {'name': name})
    else:
        return render(request,'contact.html', {})

"""def contact(request):
  return render(request,"contact.html")"""



