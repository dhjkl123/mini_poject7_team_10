from django.contrib import admin

# Register your models here.
from .models import *
from django.core.serializers.json import DjangoJSONEncoder
import json

# 관리에서 Result 객체에 대해  기본 CRUD 관리를 한다. 
admin.site.register(Result)
admin.site.register(AiModel)


@admin.register(ModelPerformance)
class ModelPerformanceAdmin(admin.ModelAdmin):
    list_display = ("model_name", "total", "sucesse") 
    
    def changelist_view(self, request, extra_context=None):
        # Aggregate new subscribers per day
        chart_data = (
            ModelPerformance.objects.all().values("model_name","acc")
        )
        
        

        # Serialize and attach the chart data to the template context
        as_json = json.dumps(list(chart_data), cls=DjangoJSONEncoder)
        extra_context = extra_context or {"chart_data": as_json}
        
        print(as_json)

        # Call the superclass changelist_view to render the page
        return super().changelist_view(request, extra_context=extra_context)