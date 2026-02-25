import DarkModeSwitch from './DarkModeSwitch'; // Verifique se o nome do arquivo bate

export default {
  title: 'Componentes/DarkModeSwitch', // O nome que vai aparecer no menu do Storybook
  component: DarkModeSwitch,
};

// Esta é a sua "Story"
export const Padrao = {
  render: () => <DarkModeSwitch />,
};