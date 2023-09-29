import Link from "next/link";

const Menu = () => {
    return (
        <>
        <div className="menu">
        <ul>
            <li><Link href="/">Home</Link></li>
            <li><Link href="/company/list">Companys</Link></li>
            <li><Link href="/company/create">Add Company</Link></li>
        </ul>
        </div>
        </>
    )
}

export default Menu
