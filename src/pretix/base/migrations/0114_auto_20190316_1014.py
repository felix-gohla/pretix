# Generated by Django 2.1.7 on 2019-03-16 10:14

import django.db.models.deletion
import jsonfallback.fields
from django.db import migrations, models

import pretix.base.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pretixbase', '0113_auto_20190312_0942'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemBundle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.PositiveIntegerField(default=1, verbose_name='Number')),
                ('designated_price', models.DecimalField(blank=True, decimal_places=2, help_text="If set, it will be shown that this bundled item is responsible for the given value of the total price. This might be important in cases of mixed taxation, but can be kept blank otherwise. This value will NOT be added to the base item's price.", max_digits=10, null=True, verbose_name='Designated price part')),
            ],
        ),
        migrations.AddField(
            model_name='cartposition',
            name='is_bundled',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='cartposition',
            name='addon_to',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='addons', to='pretixbase.CartPosition'),
        ),
        migrations.AlterField(
            model_name='orderposition',
            name='addon_to',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='addons', to='pretixbase.OrderPosition'),
        ),
        migrations.AddField(
            model_name='itembundle',
            name='base_item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bundles', to='pretixbase.Item'),
        ),
        migrations.AddField(
            model_name='itembundle',
            name='bundled_item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bundled_with', to='pretixbase.Item', verbose_name='Bundled item'),
        ),
        migrations.AddField(
            model_name='itembundle',
            name='bundled_variation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bundled_with', to='pretixbase.ItemVariation', verbose_name='Bundled variation'),
        ),
        migrations.AddField(
            model_name='item',
            name='require_bundling',
            field=models.BooleanField(default=False, help_text='If this option is set, the product will only be sold as part of bundle products.', verbose_name='Only sell this product as part of a bundle'),
        ),
    ]
