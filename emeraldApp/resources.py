from import_export import resources
from .models import Member


class MemberResource(resources.ModelResource):
    class meta:
        model = Member
