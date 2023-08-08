from app.models.brand import BrandRead, BrandReadWithProducts
from app.models.product import ProductRead, ProductReadWithBrand

BrandReadWithProducts.update_forward_refs(ProductRead=ProductRead)
ProductReadWithBrand.update_forward_refs(BrandRead=BrandRead)
