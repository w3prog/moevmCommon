from django.db import models
from django.contrib.auth.models import User
from manager_tools import filter_by_foreign_fields


class UserProfileManager(models.Manager):
    def filter(self, **filter_fields):
        return filter_by_foreign_fields(super(UserProfileManager, self), **filter_fields)
    
    def create_all(self, username,
               password, email,
               **kwargs):

        user = User(username=username, email=email, password=password)

        user.first_name = kwargs.get('first_name')
        user.last_name = kwargs.get('last_name')
        user.is_superuser = kwargs.get('is_superuser', False)
        user.save()
        print "hell"
        return self.create(
            user=user,
            patronymic=kwargs.get('patronymic'),
            birth_date=kwargs.get('birth_date'),
            study_group=kwargs.get('study_group'),
            github_id=kwargs.get('github_id'),
            stepic_id=kwargs.get('stepic_id'),
            role=kwargs.get('role', 's'),
            election_date=kwargs.get('election_date'),
            position=kwargs.get('position'),
            contract_date=kwargs.get('contract_date'),
            academic_degree=kwargs.get('academic_degree'),
            year_of_academic_degree=kwargs.get('year_of_academic_degree'),
            academic_status=kwargs.get('academic_status'),
            year_of_academic_status=kwargs.get('year_of_academic_status')
        )

    def create_from_user(self,
                         user=None,
                         position=None,
                         contract_date=None,
                         academic_degree=None,
                         year_of_academic_degree=None,
                         academic_status=None,
                         patronymic=None,
                         **params):
        return  self.create(
            user=user,
            patronymic=patronymic,
            type=type,
            position=position,
            contract_date=contract_date,
            academic_degree=academic_degree,
            year_of_academic_degree=year_of_academic_degree,
            academic_status=academic_status,
        )

