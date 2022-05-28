from django.shortcuts import render


def hello(request):
    context = {}
    context['hello'] = '走进Django世界！'
    context['太祖'] = '为有牺牲多壮志，敢教日月让换新天'
    context['views_str'] = "<a href='https://www.runoob.com/'>菜鸟首页</a>"
    return render(request, 'hello.html', context)
