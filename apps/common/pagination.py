from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from django.conf import settings


class CustomPagination(PageNumberPagination):
    # Default qiymat settings.py dan olinadi, agar bo‘lmasa 10
    page_size = getattr(settings, "DEFAULT_PAGE_SIZE", 10)
    page_size_query_param = "page_size"
    max_page_size = 100

    def get_paginated_response(self, data):
        return Response({
            "meta": {
                "current_page": self.page.number,
                "page_size": self.page.paginator.per_page,
                "total_items": self.page.paginator.count,
                "total_pages": self.page.paginator.num_pages,
                "has_next": self.page.has_next(),
                "has_previous": self.page.has_previous(),
            },
            "links": {
                "next": self.get_next_link(),
                "previous": self.get_previous_link(),
            },
            "results": data,
        })
