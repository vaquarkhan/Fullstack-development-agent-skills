# BAD — returns model directly, N+1 on list
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
