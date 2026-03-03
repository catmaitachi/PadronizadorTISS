import {useState, useEffect} from 'react';
import { useDarkMode } from '@hooks';

const DarkModeSwitch = () => {

    const [darkMode, setDarkMode] = useDarkMode();

    return (
        <button 
        onClick={setDarkMode}
        className=" relative inline-flex h-8 w-20 items-center rounded-full 
        transition-colors focus:outline-none
        dark:bg-slate-950 bg-gray-400 dark:text-white text-slate-950"
        aria-label="Switch responsável por trocar o modo escuro">

            <span
                className={`${
                darkMode ? 'translate-x-12 bg-slate-950' : 'translate-x-2 bg-gray-300'
        }       flex h-6 w-6 transform items-center justify-center rounded-full transition-transform duration-300 ease-in-out shadow-sm`}>
            </span>
            {darkMode ? (
          <span className="text-xs">🌙</span>
        ) : (
          <span className="text-xs ml-3">☀️</span>
        )}
        </button>
    )

}

export default DarkModeSwitch;