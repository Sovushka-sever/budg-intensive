from django.db.models import Count, Q
from day_7.queryset_methods.models import Order


def get_top_customer_in_period(begin, end):
    """Возвращает покупателя, который сделал наибольшее количество заказов за определенный промежуток времени

    Args:
        begin: начало периода
        end: окончание периода

    Returns: возвращает имя покупателя и количество его заказов за указанный период
    """
    queryset = Order.objects.values('customer__name').annotate(
        count_order=Count(
            'number',
            filter=Q(date_formation__range=(begin, end)))
    ).order_by('-count_order').first()

    if queryset['count_order'] == 0:
        return None
    else:
        return queryset['customer__name'], queryset['count_order']
