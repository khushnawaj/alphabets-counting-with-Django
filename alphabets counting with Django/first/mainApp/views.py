from django.shortcuts import render

# Create your views here.


def home(Request):
    return render(Request, "index.html")


def contact(Request):
    return render(Request, "contact.html", {
        'name': 'khush',
        'phone': '8417858734',
        'designation': 'trainee',
        'email': 'khushnawaj14@gmail.com'
    })


def resume(Request):
    return render(Request, "resume.html")

# def contact(Request):
#     context = {
#                                         'name':'khush',
#                                         'phone':'8417858734',
#                                         'designation':'trainee',
#                                         'email':'khushnawaj14@gmail.com'
#                                         })


def stringinput(Request):
    lcv = 0
    lcc = 0
    ucc = 0
    ucv = 0
    digit = 0
    sp = 0
    special = 0
    show = False
    data = ""
    if (Request.method == "POST"):
        show = True
        data = Request.POST.get('data')
        for i in data:
            if (i >= 'a' and i <= 'z'):
                if (i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u'):
                    lcv = lcv+1
                else:
                    lcc = lcc+1
            elif (i >= 'A' and i <= 'Z'):
                if (i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U'):
                    ucv = ucv+1
                else:
                    ucc = ucc+1
            elif (i >= '0' and i <= '9'):
                digit = digit+1
            elif (i == ' '):
                sp = sp+1
            else:
                special = special+1
    return render(Request, "stringinput.html", {
        'lcv': lcv,
        'lcc': lcc,
        'ucv': ucv,
        'ucc': ucc,
        'digit': digit,
        'sp': sp,
        'special': special,
        'show': show,
        'data':data

    })
