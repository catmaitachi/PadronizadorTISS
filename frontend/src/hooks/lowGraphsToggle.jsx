import { useState, useEffect } from 'react';

const useLowGraphs = () => {

    const [isLowGraphs, setIsLowGraphs] = useState(() => {
        const savedMode = localStorage.getItem('lowGraphs');
        if (savedMode !== null) {
            return JSON.parse(savedMode);
         }
        return false;
    });

    useEffect(() => {
        localStorage.setItem('lowGraphs', JSON.stringify(isLowGraphs));
        if (isLowGraphs) {
            document.documentElement.classList.add('low-graphs');
        } else {
            document.documentElement.classList.remove('low-graphs');
        }
    }, [isLowGraphs]);

    const toggleLowGraphs = () => {
        setIsLowGraphs(prevMode => !prevMode);
    };

    return [isLowGraphs, toggleLowGraphs];

}

export default useLowGraphs;