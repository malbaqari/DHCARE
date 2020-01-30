import django_tables2 as tables

from .models import appointment


class appointmentTable(tables.Table):
    department_code = tables.Column(verbose_name='Clinic')
    nid = tables.Column(verbose_name='National ID')
    # id = tables.Column(visible=False)
    id = tables.CheckBoxColumn(accessor='id')

    class Meta:
        model = appointment
        template_name = "django_tables2/bootstrap4.html"
