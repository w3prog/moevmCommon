from django.db import models
from django.contrib.auth.models import UserManager
from manager_tools import filter_by_foreign_fields


class UserProfileManager(models.Manager):
    def filter(self, **filter_fields):
        return filter_by_foreign_fields(super(UserProfileManager, self), **filter_fields)

    def create(self, username, password, email, **kwargs):
        user_manager = UserManager()

        user = user_manager.create_user(username=username, password=password, email=email)
        user.first_name = kwargs.get('first_name')
        user.last_name = kwargs.get('last_name')
        user.is_superuser = kwargs.get('is_superuser', False)
        user.save()

        self.create(
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
