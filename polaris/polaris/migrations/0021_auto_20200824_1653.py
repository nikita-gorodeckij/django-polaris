# Generated by Django 2.2.15 on 2020-08-24 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("polaris", "0020_auto_20200805_1650"),
    ]

    operations = [
        migrations.AlterField(
            model_name="asset", name="code", field=models.TextField(),
        ),
        migrations.AlterField(
            model_name="transaction",
            name="status",
            field=models.CharField(
                choices=[
                    ("pending_anchor", "pending_anchor"),
                    ("pending_trust", "pending_trust"),
                    ("pending_user", "pending_user"),
                    ("pending_user_transfer_start", "pending_user_transfer_start"),
                    ("incomplete", "incomplete"),
                    ("no_market", "no_market"),
                    ("too_small", "too_small"),
                    ("too_large", "too_large"),
                    ("pending_sender", "pending_sender"),
                    ("pending_receiver", "pending_receiver"),
                    (
                        "pending_transaction_info_update",
                        "pending_transaction_info_update",
                    ),
                    ("pending_customer_info_update", "pending_customer_info_update"),
                    ("completed", "completed"),
                    ("error", "error"),
                    ("pending_external", "pending_external"),
                    ("pending_stellar", "pending_stellar"),
                ],
                default="pending_external",
                max_length=31,
            ),
        ),
    ]
