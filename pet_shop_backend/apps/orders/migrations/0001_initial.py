# Generated by Django 4.2.2 on 2023-09-16 16:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("products", "0004_alter_product_recommend"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Order",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_time",
                    models.DateTimeField(auto_now_add=True, verbose_name="创建时间"),
                ),
                (
                    "updated_time",
                    models.DateTimeField(auto_now_add=True, verbose_name="更新时间"),
                ),
                ("is_delete", models.BooleanField(default=False, verbose_name="删除标记")),
                ("address", models.CharField(max_length=200, verbose_name="收货地址")),
                ("order_code", models.CharField(max_length=50, verbose_name="订单编号")),
                (
                    "amount",
                    models.DecimalField(
                        decimal_places=2, max_digits=10, verbose_name="订单金额"
                    ),
                ),
                (
                    "status",
                    models.SmallIntegerField(
                        choices=[
                            (1, "待支付"),
                            (2, "待发货"),
                            (3, "配送中"),
                            (4, "待评价"),
                            (5, "已完成"),
                        ],
                        default=1,
                        verbose_name="订单状态",
                    ),
                ),
                (
                    "pay_type",
                    models.SmallIntegerField(
                        blank=True,
                        choices=[(1, "支付宝"), (2, "微信"), (3, "银行卡"), (4, "货到付款")],
                        default=1,
                        verbose_name="支付方式",
                    ),
                ),
                (
                    "pay_time",
                    models.DateTimeField(blank=True, null=True, verbose_name="支付时间"),
                ),
                (
                    "trade_no",
                    models.CharField(
                        blank=True, max_length=50, null=True, verbose_name="支付单号"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="用户",
                    ),
                ),
            ],
            options={
                "verbose_name": "订单表",
                "verbose_name_plural": "订单表",
                "db_table": "order",
            },
        ),
        migrations.CreateModel(
            name="OrderProducts",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_time",
                    models.DateTimeField(auto_now_add=True, verbose_name="创建时间"),
                ),
                (
                    "updated_time",
                    models.DateTimeField(auto_now_add=True, verbose_name="更新时间"),
                ),
                ("is_delete", models.BooleanField(default=False, verbose_name="删除标记")),
                (
                    "price",
                    models.DecimalField(
                        decimal_places=2, max_digits=10, verbose_name="商品价格"
                    ),
                ),
                ("number", models.IntegerField(default=1, verbose_name="商品数量")),
                (
                    "order",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="orders.order",
                        verbose_name="所属订单",
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="products.product",
                        verbose_name="商品id",
                    ),
                ),
            ],
            options={
                "verbose_name": "订单详情",
                "verbose_name_plural": "订单详情",
                "db_table": "order_products",
            },
        ),
        migrations.CreateModel(
            name="Comment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_time",
                    models.DateTimeField(auto_now_add=True, verbose_name="创建时间"),
                ),
                (
                    "updated_time",
                    models.DateTimeField(auto_now_add=True, verbose_name="更新时间"),
                ),
                ("is_delete", models.BooleanField(default=False, verbose_name="删除标记")),
                (
                    "content",
                    models.CharField(default="", max_length=500, verbose_name="评论内容"),
                ),
                (
                    "rete",
                    models.SmallIntegerField(
                        blank=True,
                        choices=[(1, "好评"), (2, "中评"), (3, "差评")],
                        default=1,
                        verbose_name="评论级别",
                    ),
                ),
                (
                    "star",
                    models.SmallIntegerField(
                        blank=True,
                        choices=[(1, "一星"), (2, "二星"), (3, "三星"), (4, "四星"), (5, "五星")],
                        default=1,
                        verbose_name="评论星级",
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="products.product",
                        verbose_name="所属商品",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="orders.order",
                        verbose_name="所属订单",
                    ),
                ),
            ],
            options={
                "verbose_name": "订单评论",
                "verbose_name_plural": "订单评论",
                "db_table": "comment",
            },
        ),
    ]
