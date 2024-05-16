// features/Products/lib/fetchProductsData.ts

import { Product } from '@/entities/Product/model/Product'

export const fetchProductsData = async (): Promise<Product[]> => {
	// Здесь можно сделать запрос к API для получения данных о товарах
	// Возвращаем заглушенные данные в виде массива объектов товаров
	return [
		{
			id: '1',
			name: 'Ноутбук',
			description: 'Мощный ноутбук',
			price: 50000,
			quantity: 10,
		},
		{
			id: '2',
			name: 'Смартфон',
			description: 'Современный смартфон',
			price: 25000,
			quantity: 20,
		},
		{
			id: '3',
			name: 'Планшет',
			description: 'Легкий и компактный планшет',
			price: 30000,
			quantity: 15,
		},
	]
}
