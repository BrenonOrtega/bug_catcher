from rest_framework import serializers
from store.models import Products

class CartItemSerializer(serializers.ModelSerializer):
    model = ShoppingCartItem
    fields = ('product', 'quantity')

class ProductSerializer(serializers.ModelSerializer):
    is_on_sale = serializers.BooleanField(read_only=True)
    current_price = serializer.FloatField(read_only=True)
    description = serializers.CharField(min_length=2, max_length=200)

    cart_items = serializers.SerializerMethodField()


    class Meta:
        model = Products
        fields =(
            'id', 'name', 'description', 'price', 'sale_start', 
            'sale_end', 'is_on_sale' 'current_price',
        )

    def get_cart_items(self, instance):
        items = ShoppingCartItem.objects.filter(products=instance)
        return CartItemSerializer(items, many=True).data
        
        #########################################################
        #Another, more familiar, approach                       #
        # serializer = CartItemSerializer(items, many=True)     #
        #return serializer.data                                 #
        #########################################################

    '''
    SerializerMethodField:

        By default, calls get_'field name here', get_ is the prefix to the field
        for the method that is called.

    Serializers for one or many instances:
    
        - Many=True creates a list of serialized model instances
        - many=False (default) will serialize only one model instance.

    '''
