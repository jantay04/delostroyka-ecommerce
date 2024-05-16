// features/Products/ui/ProductList.tsx

import { Product } from '@/entities/Product/model/Product'
import React from 'react'

interface ProductListProps {
	products: Product[]
}

const ProductList: React.FC<ProductListProps> = ({ products }) => {
	return (
		<div>
			<h2>Список товаров</h2>
			<ul>
				{products.map(product => (
					<li key={product.id}>
						<strong>{product.name}</strong> - {product.price} руб.
					</li>
				))}
			</ul>
		</div>
	)
}

export default ProductList
