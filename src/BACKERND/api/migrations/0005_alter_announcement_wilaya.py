# Generated by Django 4.1.4 on 2022-12-29 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_remove_announcement_addressannouncement_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='wilaya',
            field=models.IntegerField(choices=[(1, 'Adrar'), (2, 'Chlef'), (3, 'Laghouat'), (4, 'Oum El Bouaghi'), (5, 'Batna'), (6, 'Béjaïa'), (7, 'Biskra'), (8, 'Béchar'), (9, 'Blida'), (10, 'Bouira'), (11, 'Tamanrasset'), (12, 'Tébessa'), (13, 'Tlemcen'), (14, 'Tiaret'), (15, 'Tizi Ouzou'), (16, 'Alger'), (17, 'Djelfa'), (18, 'Jijel'), (19, 'Sétif'), (20, 'Saïda'), (21, 'Skikda'), (22, 'Sidi Bel Abbès'), (23, 'Annaba'), (24, 'Guelma'), (25, 'Constantine'), (26, 'Médéa'), (27, 'Mostaganem'), (28, 'MSila'), (29, 'Mascara'), (30, 'Ouargla'), (31, 'Oran'), (32, 'El Bayadh'), (33, 'Illizi'), (34, 'Bordj Bou Arreridj'), (35, 'Boumerdès'), (36, 'El Tarf'), (37, 'Tindouf'), (38, 'Tissemsilt'), (39, 'El Oued'), (40, 'Khenchela'), (41, 'Souk Ahras'), (42, 'Tipaza'), (43, 'Mila'), (44, 'Aïn Defla'), (45, 'Naâma'), (46, 'Aïn Témouchent'), (47, 'Ghardaïa'), (48, 'Relizane')], default=6),
        ),
    ]
