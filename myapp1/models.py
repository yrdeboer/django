from django.db import models
from django.contrib.auth.models import Permission, User


class MyRole(models.Model):

    def __str__(self):
        return self.name

    name = models.CharField(max_length=40)


class MyUser(models.Model):

    django_user = models.OneToOneField(User)

    my_roles = models.ManyToManyField(MyRole)
    


class MyModelManager(models.Manager):

    role_qs = {
        'Field1 X1 Viewer': models.Q(field1='X1'),
        'Field1 X2 Viewer': models.Q(field1='X2'),
        'Field2 X2 Viewer': models.Q(field2='X2'),
    }
    
    def get_queryset_user(self, my_user):

        print('get_queryset with my_user = {}'.format(my_user))

        # Collect Q's in a list
        q_list = []

        # Get querysets narrowed down for each user's role
        user_roles = my_user.my_roles.all()
        for role in user_roles:

            print('get_queryset, role = {}'.format(role))
            role_q = self.role_qs[role.name]
            print('get_queryset, appending role_q = {}'.format(role_q))
            q_list.append(role_q)

        if (q_list):

            # OR q's together
            q_ored = q_list[0]
            for q in q_list[1:]:
                print('get_queryset, oring q: {}'.format(q))
                q_ored = q_ored | q

            # Return Q objects OR'ed together
            ret_queryset = super(MyModelManager, self).get_queryset().filter(q_ored)

        else:

            # Return empty queryset
            ret_queryset = QuerySet()

        # return super(MyModelManager, self).get_queryset().all()
        return ret_queryset


class MyPermission(Permission):
    pass

class MyModel(models.Model):

    def __str__(self):
        return self.name

    objects = MyModelManager()

    class Meta:

        permissions = (
            ('can_view_field1', 'Can view field1'),
            ('can_view_field2', 'Can view field2'),
        )


    name = models.CharField(max_length=40)
    field1 = models.CharField(max_length=40)
    field2 = models.CharField(max_length=40)

    def get_role_permissions(self, my_role):

        role_permissions = []

        print('\n  get_role_permissions, my_role.name = {}'.format(my_role.name))
        print('  get_role_permissions, self.field1  = {}'.format(self.field1))
        print('  get_role_permissions, self.field2  = {}'.format(self.field2))
        
        if (my_role.name == 'Field1 X1 Viewer' and self.field1 == 'X1'):
            print('  get_role_permissions, getting p ...')
            p = Permission.objects.get(codename='can_view_field1')
            print('  get_role_permissions, p = {}'.format(p))
            print('  get_role_permissions, p.codename = {}'.format(p.codename))
            role_permissions.append(p.codename)

        if (my_role.name == 'Field1 X2 Viewer' and self.field1 == 'X2'):
            print('\n  get_role_permissions, getting p ...')
            p = Permission.objects.get(codename='can_view_field1')
            print('  get_role_permissions, p = {}'.format(p))
            print('  get_role_permissions, p.codename = {}'.format(p.codename))
            role_permissions.append(p.codename)

        if (my_role.name == 'Field2 X2 Viewer' and self.field2 == 'X2'):
            print('\n  get_role_permissions, getting p ...')
            p = Permission.objects.get(codename='can_view_field2')
            print('  get_role_permissions, p = {}'.format(p))
            print('  get_role_permissions, p.codename = {}'.format(p.codename))
            role_permissions.append(p.codename)


        print('  Returning role_permissions: {}'.format(role_permissions))
        
        return role_permissions


