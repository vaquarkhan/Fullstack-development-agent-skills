# GOOD — DRF viewset with serializer and select_related
class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Order.objects.select_related("customer").filter(tenant_id=self.request.tenant.id)
