import { Product } from '@/entities/Product/model/Product'
import Link from 'next/link'
import React from 'react'

interface ProductListProps {
	products: Product[]
}

const ProductList: React.FC<ProductListProps> = ({ products }) => {
	return (
		<ul>
			{products.map(product => (
				<li key={product.id}>
					<Link href={`/products/${product.id}`}>{product.name}</Link>
				</li>
			))}
		</ul>
	)
}

export default ProductList
