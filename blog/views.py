from django.shortcuts import render

# Create your views here.
def post_list(request):
    return render(request, 'blog/post_list.html', {})


def post_list_test(request, msg):
    result = {}
    result['msg'] = msg
    result['msg1'] = 'aaa'
    result['msg2'] = 'bbb'
    result['arr'] = []
    result['arr'].append('1111')
    result['arr'].append('22222')
    result['arr'].append('3333')
    result['arr'].append('4444')
    result['bool'] = False
    print(result)
    return render(request, 'blog/post_list.html', {'result': result})
