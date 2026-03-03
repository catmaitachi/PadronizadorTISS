import { DarkModeSwitch } from '@components';

const Header = () => {

    return (
        <header 
        className="p-5 w-full fixed top-0 left-0 z-10 items-start justify-between flex
        bg-gray-300 dark:bg-gray-800 border-gray-700 dark:border-slate-950 
        border-b-2 shadow-black/20 dark:shadow-slate-950/20 shadow-md">
            <h1 className="text-xl font-bold font-serif">Padronizador TISS</h1>
            <DarkModeSwitch />
        </header>
    )

}

export default Header;