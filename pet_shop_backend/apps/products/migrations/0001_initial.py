# Generated by Django 4.2.2 on 2023-09-15 09:34

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Banner",
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
                    "title",
                    models.CharField(
                        blank=True, default="", max_length=20, verbose_name="轮播图名称"
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        blank=True, null=True, upload_to="banner/", verbose_name="轮播图连接"
                    ),
                ),
                ("status", models.BooleanField(default=False, verbose_name="是否启用")),
                (
                    "sequence",
                    models.IntegerField(blank=True, default=1, verbose_name="顺序"),
                ),
            ],
            options={
                "verbose_name": "首页轮播",
                "verbose_name_plural": "首页轮播",
                "db_table": "banner",
            },
        ),
        migrations.CreateModel(
            name="Category",
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
                ("name", models.CharField(max_length=20, verbose_name="分类")),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="category/",
                        verbose_name="分类图标",
                    ),
                ),
                ("status", models.BooleanField(default=False, verbose_name="是否启用")),
            ],
            options={
                "verbose_name": "商品分类表",
                "verbose_name_plural": "商品分类表",
                "db_table": "category",
            },
        ),
        migrations.CreateModel(
            name="Product",
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
                    "title",
                    models.CharField(default="", max_length=20, verbose_name="标题"),
                ),
                (
                    "description",
                    models.CharField(default="", max_length=29, verbose_name="商品描述"),
                ),
                (
                    "price",
                    models.DecimalField(
                        decimal_places=2, max_digits=10, verbose_name="价格"
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        blank=True, null=True, upload_to="product/", verbose_name="图片连接"
                    ),
                ),
                (
                    "stock",
                    models.IntegerField(blank=True, default=0, verbose_name="库存"),
                ),
                (
                    "sales",
                    models.IntegerField(blank=True, default=0, verbose_name="销量"),
                ),
                (
                    "is_on",
                    models.BooleanField(blank=True, default=False, verbose_name="是否上架"),
                ),
                (
                    "recommend",
                    models.IntegerField(blank=True, default=0, verbose_name="推荐指数"),
                ),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="products.category",
                        verbose_name="分类",
                    ),
                ),
            ],
            options={
                "verbose_name": "商品表",
                "verbose_name_plural": "商品表",
                "db_table": "products",
            },
        ),
        migrations.CreateModel(
            name="Detail",
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
                    "details",
                    ckeditor.fields.RichTextField(blank=True, verbose_name="详情"),
                ),
                (
                    "product",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="products.product",
                        verbose_name="商品",
                    ),
                ),
                (
                    "vender",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="商家",
                    ),
                ),
            ],
            options={
                "verbose_name": "商品详情",
                "verbose_name_plural": "商品详情",
                "db_table": "detail",
            },
        ),
        migrations.CreateModel(
            name="Collect",
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
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="products.product",
                        verbose_name="商品id",
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
                "verbose_name": "收藏商品",
                "verbose_name_plural": "收藏商品",
                "db_table": "collect",
            },
        ),
    ]
