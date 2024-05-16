const Sidebar = () => {
	return (
		<div className='flex overflow-hidden bg-white rounded-lg'>
			<div className='hidden md:flex md:flex-shrink-0'>
				<div className='flex flex-col w-64'>
					<div className='flex flex-col flex-grow pt-5 overflow-y-auto border-r bg-neutral-800'>
						<div className='flex flex-col items-center flex-shrink-0 px-4'>
							<a
								href='/groups/sidebar/'
								className='px-8 text-left focus:outline-none'
							>
								<h2 className='block p-2 text-xl font-medium tracking-tighter transition duration-500 ease-in-out transform cursor-pointer text-neutral-200 hover:text-neutral-200'>
									wickedblocks
								</h2>
							</a>
							<button className='hidden rounded-lg focus:outline-none focus:shadow-outline'>
								<svg
									fill='currentColor'
									viewBox='0 0 20 20'
									className='w-6 h-6'
								>
									<path
										fillRule='evenodd'
										d='M3 5a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1zM3 10a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1zM9 15a1 1 0 011-1h6a1 1 0 110 2h-6a1 1 0 01-1-1z'
										clipRule='evenodd'
									></path>
									<path
										fillRule='evenodd'
										d='M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z'
										clipRule='evenodd'
									></path>
								</svg>
							</button>
						</div>
						<div className='flex flex-col flex-grow px-4 mt-5'>
							<nav className='flex-1 space-y-1 bg-neutral-800'>
								<ul>
									<li>
										<a
											href='#'
											className='inline-flex items-center w-full px-4 py-2 mt-1 text-base transition duration-500 ease-in-out transform border rounded-lg text-neutral-200 bg-neutral-900 border-neutral-900 focus:shadow-outline'
										>
											<svg
												xmlns='http://www.w3.org/2000/svg'
												className='w-4 h-4'
												fill='none'
												viewBox='0 0 24 24'
												stroke='currentColor'
											>
												<path
													strokeLinecap='round'
													strokeLinejoin='round'
													strokeWidth='2'
													d='M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z'
												></path>
											</svg>
											<span className='ml-4'> Overview</span>
										</a>
									</li>
									{/* Additional menu items go here */}
								</ul>
								<p className='px-4 pt-4 font-medium uppercase text-neutral-200'>
									Shortcuts
								</p>
								<ul>
									<li>
										<a
											href='#'
											className='inline-flex items-center w-full px-4 py-2 mt-1 text-base transition duration-500 ease-in-out transform border rounded-lg text-neutral-200 border-neutral-800 hover:border-neutral-800 focus:shadow-outline hover:bg-neutral-900'
										>
											<svg
												xmlns='http://www.w3.org/2000/svg'
												className='w-4 h-4'
												fill='none'
												viewBox='0 0 24 24'
												stroke='currentColor'
											>
												<path
													strokeLinecap='round'
													strokeLinejoin='round'
													strokeWidth='2'
													d='M16 11V7a4 4 0 00-8 0v4M5 9h14l1 12H4L5 9z'
												></path>
											</svg>
											<span className='ml-4'> Tasks</span>
										</a>
									</li>
									{/* Additional shortcut items go here */}
								</ul>
							</nav>
						</div>
						<div className='flex flex-shrink-0 p-4 px-4 bg-neutral-900'>
							<a href='#' className='flex-shrink-0 block w-full group'>
								<div className='flex items-center'>
									<div>
										{/* <Image
											className='inline-block rounded-full h-9 w-9'
											src='/assets/images/avatar.png'
											alt=''
										/> */}
									</div>
									<div className='ml-3'>
										<p className='text-sm font-medium text-neutral-200'>
											Wicked Labs
										</p>
									</div>
								</div>
							</a>
						</div>
					</div>
				</div>
			</div>
			<div className='flex flex-col flex-1 w-0 overflow-hidden'>
				<main className='relative flex-1 overflow-y-auto focus:outline-none'>
					<div className='py-6'>
						<div className='px-4 mx-auto max-w-7xl sm:px-6 md:px-8'>
							<h1 className='text-lg text-neutral-600'>
								Here is where you put your stuff
							</h1>
						</div>
						<div className='px-4 mx-auto max-w-7xl sm:px-6 md:px-8'>
							{/* Put your content here */}
							<div className='py-4'>
								<div className='rounded-lg bg-neutral-50 h-96'></div>
							</div>
							{/* Do not cross the closing tag underneath this comment */}
						</div>
					</div>
				</main>
			</div>
		</div>
	)
}

export default Sidebar
