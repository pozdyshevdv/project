from django.shortcuts import render, redirect


def favorites_list(request):
    context = {}
    return render(request, 'favorites-list.html', context)


def add_to_favorites(request, pk):
    if request.method == 'POST':
        if not request.session.get('favorites'):
            request.session['favorites'] = list()
        else:
            request.session['favorites'] = list(request.session['favorites'])
        item_exist = next((item for item in request.session['favorites'] if item["type"] == request.POST.get('type') and item["id"] == pk), False)
        add_data = {
            'type': request.POST.get('type'),
            'id': pk,
        }
        if not item_exist:
            request.session['favorites'].append(add_data)
            request.session.modified = True
    return redirect(request.POST.get('url_from'))


def remove_from_favorites(request, pk):
    if request.method == 'POST':
        for item in request.session['favorites']:
            if item['id'] == pk and item['type'] == request.POST.get('type'):
                item.clear()

        while {} in request.session['favorites']:
            request.session['favorites'].remove({})

        if not request.session['favorites']:
            del request.session['favorites']

        request.session.modified = True
    return redirect(request.POST.get('url_from'))


def delete_favorites(request):
    if request.session.get('favorites'):
        del request.session['favorites']
    return redirect(request.POST.get('url_from'))


def delete_favorites(request):
    pass