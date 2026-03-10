import { Header } from '@components';

export default {
  title: 'Components/Header',
  component: Header,
  parameters: {
    // Remove o padding padrão do Storybook para o header encostar nas bordas
    layout: 'fullscreen',
  },
  decorators: [
    (Story) => (
      <div className="min-h-[150px] w-full bg-gray-100 dark:bg-gray-900">
        <Story />
      </div>
    ),
  ],
};

export const Default = {
  args: {},
};

export const Dark = {
  args: {},
  parameters: {
    theme: 'dark', // Se você tiver o addon de themes configurado
  },
};