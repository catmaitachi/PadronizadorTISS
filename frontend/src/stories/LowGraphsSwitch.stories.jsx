import { LowGraphsSwitch } from '@components';

export default {
  title: 'Components/LowGraphsSwitch', // Onde ele vai aparecer no menu do Storybook
  component: LowGraphsSwitch,
  parameters: {
    layout: 'centered', // Centraliza o componente na tela de teste
  },
};

// História Principal (Estado Padrão)
export const Default = {};

// História com fundo escuro para testar contraste
export const OnDarkBackground = {
  decorators: [
    (Story) => (
      <div className="p-10 bg-gray-900">
        <Story />
      </div>
    ),
  ],
};