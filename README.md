# App para Manicure (atividade da faculdade)

### Este é um projeto de aplicativo web simples desenvolvido em Python com o framework Flask para auxiliar manicures autônomas a gerenciar seus agendamentos, estoque de materiais e calcular seus ganhos semanais. Trata-se de uma atividade de Extensão da disciplina de Desenvolvimento em Python da minha faculdade de Defesa Cibernética. O projeto principal já foi entregue e era algo mais simples, porém, decidi continuar e fazer implementações (controle de estoque, cálculo de ganhos e etc), porém, precisei executar uma pausa nesse pequeno projeto para seguir com os estudos e carreira em Cibersegurança. 

Funcionalidades:

- Agendamentos:
    - Permite agendar serviços, incluindo nome do cliente, contato, tipo de serviço, data e hora.
    - Exibe a agenda semanal em uma tabela, facilitando a visualização dos compromissos.
    - Permite excluir agendamentos da agenda.
- Controle de Estoque:
    - Controla o estoque de lixas de unha e pares de luvas descartáveis.
    - Permite registrar a entrada de novos materiais no estoque.
    - Exibe o estoque atual de cada material e alerta quando o estoque está baixo.
- Cálculo de Ganhos:
    - Calcula automaticamente os ganhos semanais da manicure, com detalhamento por tipo de serviço.

Como usar:

- Pré-requisitos: 
    - Python 3 instalado 
    - Flask instalado (pip install Flask)
    - Utilize o arquivo index.html dentro da pasta templates (Isso é importante para que o Flask encontre o template corretamente ao renderizar a página.)
- Executar o aplicativo:
    - Abra o terminal na pasta do projeto e execute o comando python app.py.
    - Acesse o aplicativo no seu navegador web através do endereço http://127.0.0.1:5000/.
- Agendar um serviço:
    - Preencha o formulário de "Agendamentos" com o nome do cliente, contato, serviço, data e hora.
    - Clique em "Agendar Serviço". O agendamento será adicionado à agenda semanal e o estoque será atualizado.
- Registrar entrada de materiais:
    - Selecione o material (lixas ou luvas) no formulário "Estoque".
    - Informe a quantidade e clique em "Registrar Entrada". O estoque será atualizado.
- Calcular ganhos semanais:
    - Clique no botão "Calcular Ganhos" para visualizar os ganhos da semana, detalhados por tipo de serviço.
- Excluir agendamento:
    - Clique no botão "X" ao lado do agendamento que deseja excluir. O agendamento será removido da agenda e o estoque será atualizado.

Observações:

- Este é um aplicativo básico e pode ser expandido com mais funcionalidades e melhorias na interface.
- Os dados são armazenados em arquivos JSON locais (agendamentos.json e estoque.json).
- Certifique-se de ter o Python e o Flask instalados antes de executar o aplicativo.

Contribuições:

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests com sugestões de melhorias, correções de bugs ou novas funcionalidades.

Contato:

E-mail: demetriusvf@gmail.com
