# Generated by Django 4.2.1 on 2023-06-12 12:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('obra_sociales', '__first__'),
        ('paciente', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fecha',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Hora',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hora', models.CharField(choices=[('16:00', '04:00'), ('16:10', '04:10'), ('16:20', '04:20'), ('16:30', '04:30'), ('16:40', '04:40'), ('16:50', '04:50'), ('17:00', '05:00'), ('17:10', '05:10'), ('17:20', '05:20'), ('17:30', '05:30'), ('17:40', '05:40'), ('17:50', '05:50'), ('18:00', '06:00'), ('18:10', '06:10'), ('18:20', '06:20'), ('18:30', '06:30'), ('18:40', '06:40'), ('18:50', '06:50'), ('19:00', '07:00')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150)),
                ('apellido', models.CharField(max_length=90)),
                ('celular', models.CharField(max_length=12)),
                ('dni', models.IntegerField()),
                ('observaciones', models.TextField(blank=True)),
                ('nombre_completo', models.CharField(default='', editable=False, max_length=200)),
                ('obra_social', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='obra_sociales.obrasocial')),
            ],
        ),
        migrations.CreateModel(
            name='Turno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diagnostico', models.TextField(blank=True, default='', help_text='Ingrese el diagnóstico del paciente', null=True)),
                ('fecha', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='turnos_fecha', to='paciente.fecha')),
                ('hora', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='turnos_hora', to='paciente.hora')),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='turnos_paciente', to='paciente.paciente')),
            ],
        ),
    ]
