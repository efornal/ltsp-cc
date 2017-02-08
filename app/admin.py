from django.contrib import admin
from app.models import Attribute
from app.models import PossibleAttributeValue
from app.models import Group
from app.models import GroupAttributeValue
from app.models import Node
from app.models import NodeAttributeValue



# Register your models here.
admin.site.register( Attribute )
admin.site.register( PossibleAttributeValue )
admin.site.register( Group )
admin.site.register( GroupAttributeValue )
admin.site.register( Node )
admin.site.register( NodeAttributeValue )



