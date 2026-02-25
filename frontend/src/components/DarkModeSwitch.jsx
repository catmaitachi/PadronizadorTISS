import {useState, useEffect} from 'react';
import { useDarkMode } from '@hooks';

const DarkModeSwitch = () => {

    const [darkMode, setDarkMode] = useDarkMode();

    return (
        <button 
        onClick={setDarkMode}
        className=""></button>
    )

}

export default DarkModeSwitch;