import { Badge } from '@/components/ui/badge'
import { Home, LineChart, Package, ShoppingCart, Users } from 'lucide-react'
import Link from 'next/link'

export default function Dashboard() {
	return (
		<aside className='fixed inset-y-0 left-0 z-10 hidden w-[180px] flex-col border-r bg-background sm:flex bg-black/90 p-2 lg:px-4'>
			<div className='h-[56px] mt-5'>
				<h1 className=' text-xl text-white text-center font-bold'>Logo</h1>
			</div>
			<nav className='grid items-start gap-2 text-sm font-medium'>
				<Link
					href='#'
					className='flex items-center gap-3 rounded-xl px-3 py-2 text-white transition-all hover:bg-white/15'
				>
					<Home className='h-4 w-4' />
					Dashboard
				</Link>
				<Link
					href='#'
					className='flex items-center gap-3 rounded-lg px-3 py-2 text-white transition-all hover:bg-white/15'
				>
					<ShoppingCart className='h-4 w-4' />
					Orders
					<Badge className='ml-auto flex h-6 w-6 shrink-0 items-center justify-center rounded-full bg-white text-black'>
						6
					</Badge>
				</Link>
				<Link
					href='#'
					className='flex items-center gap-3 rounded-lg bg-muted px-3 py-2 text-primary transition-all '
				>
					<Package className='h-4 w-4' />
					Products{' '}
				</Link>
				<Link
					href='#'
					className='flex items-center gap-3 rounded-lg px-3 py-2 text-white transition-all hover:bg-white/15'
				>
					<Users className='h-4 w-4' />
					Customers
				</Link>
				<Link
					href='#'
					className='flex items-center gap-3 rounded-lg px-3 py-2 text-white transition-all hover:bg-white/15'
				>
					<LineChart className='h-4 w-4' />
					Analytics
				</Link>
			</nav>
		</aside>
	)
}
