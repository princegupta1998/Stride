from django.shortcuts import render, redirect
from registration.form import players_form,playerssearchform
from registration.models import players
from django.core.mail import send_mail
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from django.views import View
from xhtml2pdf import pisa

def render_to_pdf(template_src, context_dict={}):
	template = get_template(template_src)
	html  = template.render(context_dict)
	result = BytesIO()
	pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
	if not pdf.err:
		return HttpResponse(result.getvalue(), content_type='application/pdf')
	return None

all_players = players.objects.all()
context = {
"all_players": all_players,
}

class ViewPDF(View):
	def get(self, request, *args, **kwargs):
		template = get_template('pdf_template.html')
		# return render(request, 'pdf_template.html', {'all':all_players})

		html = template.render(context)
		pdf = render_to_pdf('pdf_template.html', {'all':all_players})
		if pdf:
			response = HttpResponse(pdf, content_type='application/pdf')
			return response
		return HttpResponse("Not Found")


#Automaticly downloads to PDF file
class DownloadPDF(View):
	def get(self, request, *args, **kwargs):
		template = get_template('pdf_template.html')

		html = template.render(context)
		pdf = render_to_pdf('pdf_template.html', {'all':all_players})
		response = HttpResponse(pdf, content_type='application/pdf')
		filename = "Players_%s.pdf" %("List")
		content = "inline; filename='%s'" %(filename)
		response['Content-Disposition'] = content
		return response


def form(request):
	if request.method == "POST":
		post=players()
		data=request.POST

		name= data.get('Name')
		email= data.get('email')
		team_name= data.get('team_name')
		sports= data.get('sports')
		college_name= data.get('Address')
		city= data.get('City')
		state= data.get('State')
		phone_no= data.get('phone number')

		qa_object = players(name=name,email=email, team_name=team_name, sports=sports,college_name=college_name,city=city, state=state, phone_no=phone_no).save()

		# Send mail
		send_mail(
            'Message from Invertis University-Stride Club', # subject
             'Dear' + ' ' + name + ',\n\nWelcome to AAVEG,the sports fest.You have registered successfully for the event! \n\n We\'ll send you the details regarding the events and sports soon. Please, look forward to our mail. \n\n If you have any question leading up to the AAVEG sports event, feel free to reply to this mail:)\n\nWe look forward to host you soon.\n\nKind Regards,\nPrince Gupta\nitsronaldo.gupta@gmail.com\n7579335722', # message
             'webproject.strideclub@gmail.com', # from email
             [email], # To email
             fail_silently=False,
        )
		return render(request,'thanku.html')
	else:
		return render(request,'form.html')
		#return redirect("show")

		#	except:
		#		pass
	#else:
		#form = players_form()
		#return render(request,"form.html",{'form':form})

def data(request):
	all_players = players.objects.all()
	form = playerssearchform(request.POST or None)
	context = {
	"all_players": all_players,
	"form":form,
	}
	if request.method == 'POST':
		all_players = players.objects.all().filter(sports=form['sports'].value())
		context = {
		"all_players": all_players,
		"form":form,
		}
	return render(request, 'data.html', {'all':all_players})



def show(request):
	return render(request,"thanku.html")


def index(request):
	return render(request,"index.html")


def gallery(request):
	return render(request,"gallery.html")


def events(request):
	return render(request,"events.html")


def about(request):
	return render(request,"about.html")


def contact(request):
	return render(request,"contact.html")








