export default function RootLayout({
	children,
}: Readonly<{
	children: React.ReactNode
}>) {
	return (
		<div className='w-screen h-screen flex justify-center items-center '>
			<div>{children}</div>
		</div>
	)
}
