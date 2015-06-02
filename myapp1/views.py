from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import MyModel, PairUser, OSPModel1, OSPRole

from django.contrib.auth import authenticate, login

def login_view(request):

    return render(request, 'myapp1/login_form.html')
    

def login_result_view(request):

    print('login_result, request.POST =\n{}\n'.format(request.POST))
    print('login_result, request.user =\n{}\n'.format(request.user))

    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)

    if user is not None:
        if user.is_active:

            login(request, user)

            # Redirect to a success page.
            context = {'result': "Logged in"}
            return render(request, 'myapp1/login_result.html', context)
            

        else:
            # Return a 'disabled account' error message
            context = {'result': "Account disabled"}
            return render(request, 'myapp1/login_result.html', context)

    else:
        # Return an 'invalid login' error message.
        context = {'result': "Invalid login"}
        return render(request, 'myapp1/login_result.html', context)


def list_view(request):

    print('list_view')

    # Pull 1 (not all!) OSPModel1 instance from the db
    osp_model = OSPModel1.objects.all()[:1].get()
    print('list_view, osp_model = {}'.format(osp_model))

    # Pull 1 (not all!) OSPRole instance from the db
    osp_role = OSPRole.objects.all()[:1].get()
    print('list_view, osp_role = {}'.format(osp_role))

    # Fetch permissions from role for osp_model
    perms = osp_role.get_model_permissions(osp_model)
    print('list_view perms = {}'.format(perms))

    my_models_list = MyModel.objects.get_queryset_user(request.user.myuser).all()
    print('list_view, my models list: {}'.format(my_models_list))
    context = {'my_models_list': my_models_list,}
    return render(request, 'myapp1/my_models_list_template.html', context)

def detail_view(request, my_model_id):

    # Get the model
    my_model = get_object_or_404(MyModel, pk=my_model_id)
    print('detail_view, my model: {}'.format(my_model))

    # Get user's role permissions for this model
    user_permissions = []
    user_roles = request.user.myuser.my_roles.all()
    for role in user_roles:

        print('detail_view, examining role: {}'.format(role))
        role_permissions = my_model.get_role_permissions(role)
        user_permissions.extend(role_permissions)

    print('detail_view, found permissions for user:\n{}'.format(user_permissions))

    context = {'my_model': my_model, 'user_permissions': user_permissions}
    return render(request, 'myapp1/my_models_detail_template.html', context)

def list_view_pairholders(request):

    my_ph_user_list = PairUser.objects.all()
    print('list_view_pairholders, list: {}'.format(my_ph_user_list))

    # Print pairs
    for pair_user in my_ph_user_list:

        print('list_view_pairholders, pair_user = {}'.format(pair_user))
        for pair in pair_user.pairs.all():

            print('  list_view_pairholders, pair = {}'.format(pair))

    context = {'my_ph_user_list': my_ph_user_list,}
    return render(request, 'myapp1/my_ph_user_list_template.html', context)
