import DarkModeSwitch from './DarkModeSwitch';

export default {
  title: 'Componentes/DarkModeSwitch',
  component: DarkModeSwitch,
  parameters: {
    layout: 'centered',
  },
};

export const Principal = {
  render: () => (
    /* O container abaixo ajuda a visualizar o componente em qualquer tema */
    <div className="p-12 rounded-xl border-2 border-dashed border-slate-300 dark:border-slate-700 bg-slate-50 dark:bg-slate-900">
      <div className="flex flex-col items-center gap-4">
        <span className="text-sm font-medium text-slate-500 dark:text-slate-400 uppercase tracking-wider">
          Teste de Switch
        </span>
        <DarkModeSwitch />
      </div>
    </div>
  ),
};