import dynamic from 'next/dynamic'

const Layout = ({ children }) => {

    return(
        <>
        <DynamicMenu />
        <main>{children}</main>
        </>
    )

}

const DynamicMenu = dynamic(() => import('./menu'))

export default Layout