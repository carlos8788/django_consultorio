# Generated by Django 4.2.1 on 2023-06-07 15:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('paciente', '0003_remove_paciente_fecha_remove_paciente_hora_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='paciente',
            name='nombre_completo',
            field=models.CharField(default='', editable=False, max_length=200),
        ),
        migrations.AlterField(
            model_name='hora',
            name='hora',
            field=models.CharField(choices=[('16:00', '04:00'), ('16:10', '04:10'), ('16:20', '04:20'), ('16:30', '04:30'), ('16:40', '04:40'), ('16:50', '04:50'), ('17:00', '05:00'), ('17:10', '05:10'), ('17:20', '05:20'), ('17:30', '05:30'), ('17:40', '05:40'), ('17:50', '05:50'), ('18:00', '06:00'), ('18:10', '06:10'), ('18:20', '06:20'), ('18:30', '06:30'), ('18:40', '06:40'), ('18:50', '06:50'), ('19:00', '07:00')], max_length=10),
        ),
        migrations.AlterField(
            model_name='turno',
            name='paciente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='turnos_paciente', to='paciente.paciente'),
        ),
    ]