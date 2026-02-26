# PadronizadorTISS


## 📂 Padronização de Nomenclatura

Para manter a consistência do projeto e facilitar a manutenção em dupla, adotamos as seguintes convenções de nomenclatura:

### 1. Componentes e Páginas (React)
Arquivos que exportam componentes visuais devem utilizar **PascalCase**.
- **Extensão:** `.jsx`
- **Exemplos:** - `src/components/BotaoEnviar.jsx`
  - `src/pages/CadastroGuia.jsx`
  - `src/components/HeaderHospitalar.jsx`

### 2. Hooks e Utilitários (Lógica)
Arquivos de lógica pura, funções de suporte ou hooks customizados devem utilizar **camelCase**.
- **Extensão:** `.js` ou `.jsx` (para usar hooks do React)
- **Exemplos:**
  - `src/hooks/useValidacaoTiss.js`
  - `src/utils/formatarData.js`
  - `src/services/apiService.js`

### 3. Arquivos de Estilo e Configuração
Arquivos globais ou de configuração utilizam **kebab-case** ou mantêm o padrão da ferramenta.
- **Exemplos:**
  - `src/styles/index.css`
  - `tailwind.config.js`

### 4. Assets (Imagens e Ícones)
Arquivos de mídia devem utilizar **kebab-case**.
- **Exemplos:**
  - `src/assets/logo-hospital.png`
  - `src/assets/icon-check.svg`

---

> [!IMPORTANT]
> **Por que essa padronização?**
> Seguimos as convenções da comunidade React para garantir que o projeto seja escalável e profissional, facilitando a leitura por outros desenvolvedores dentro do ambiente hospitalar.


## 🔗 Atalhos de Importação (Aliases)

Para evitar caminhos complexos como `../../components/`, configuramos **Aliases** no Vite. Agora, o caractere `@` aponta diretamente para a pasta `src`.

### Como usar:
Sempre que precisar importar algo, utilize os prefixos abaixo:

| Atalho | Pasta Destino | Exemplo de Uso |
| :--- | :--- | :--- |
| `@/` | `src/` | `import App from '@/App';` |
| `@components/` | `src/components/` | `import Botao from '@components/Botao';` |
| `@hooks/` | `src/hooks/` | `import { useTiss } from '@hooks/useTiss';` |
| `@utils/` | `src/utils/` | `import { validar } from '@utils/validar';` |
| `@assets/` | `src/assets/` | `import Logo from '@assets/logo.png';` |

> [!TIP]
> **Dica de Desenvolvimento:** Se o seu editor (VS Code) não reconhecer os atalhos automaticamente, certifique-se de que o arquivo `jsconfig.json` ou `tsconfig.json` na raiz do projeto esteja atualizado com essas rotas.