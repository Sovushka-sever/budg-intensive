from datetime import date

from django.db.models import Max

from day_7.queryset_methods.models import ProductCount, Product


def get_top_product_by_total_count_in_period(begin, end):
    """Возвращает товар, купленный в наибольшем объеме за определенный промежуток времени

    Args:
        begin: начало периода
        end: окончание периода

    Returns: возвращает наименование товара и объем
    """
    result = ProductCount.objects.values_list('product').filter(begin=begin, end=end).annotate(poduct='product__name', max_value=Max('value'))

    return result
