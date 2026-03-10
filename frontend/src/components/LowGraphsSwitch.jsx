import { useLowGraphs } from "@hooks";


const LowGraphsSwitch = () => {

    const [isLowGraphs, toggleLowGraphs] = useLowGraphs();

    return (
        <button
            onClick = {toggleLowGraphs}
            className =" relative inline-flex h-8 w-20 items-center rounded-full p-2
            transition-colors focus:outline-none 
            dark:bg-slate-950 bg-gray-400 dark:text-white text-slate-950"
            aria-label="Switch responsável por trocar o modo escuro">
            <span
                className="text-xs">
               {isLowGraphs ? "Modo Leve" : "Modo Completo"}
            </span>
        </button>
    )

}

export default LowGraphsSwitch;