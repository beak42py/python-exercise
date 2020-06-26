from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django import forms


class IntForm(forms.Form):
    intergerlist = forms.CharField(max_length=420)


def index(request):
    if request.method == 'POST':
        form = IntForm(request.POST)
        if form.is_valid():
            post_data = request.POST['intergerlist']
            col_intergers = []
            col_values = post_data.split(',')
            for i in col_values:
                try:
                    tmpnum = float(i.strip())
                except:
                    tmpnum = 0.1
                if tmpnum.is_integer() == True:
                    col_intergers.append(int(tmpnum))

            pair_list = []
            nonduplicates = list(set(col_intergers))
            sizeofnonduplicates = len(nonduplicates)
            for i in range(sizeofnonduplicates):
                for j in range(i + 1, sizeofnonduplicates):
                    if nonduplicates[i] + nonduplicates[j] == 7:
                        pair_list.append('%s and %s' % (nonduplicates[i], nonduplicates[j]))


            html_out = '<br>'
            for i in pair_list:
                html_out += '%s<br>' % (i)
            return HttpResponse(html_out)

    else:
        form = IntForm()
    return render(request, 'home.html', {'form': form})



