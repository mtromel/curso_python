'''
video aula 308, 309, 310
O módulo requests para requisições HTTP no Python
HTTP (HyperText Transfer Protocol) é um protocolo usado para enviar e receber
dados na Internet. Ele funciona no modo cliente / servidor, onde o cliente
(seu navegador, por exemplo) faz uma requisição ao servidor
(site, por exemplo), que responde com os dados adequados.

A mensagem de requisição do cliente deve incluir dados como:
- O método HTTP
    - leitura (safe) - GET, HEAD (campos), OPTIONS (métodos suportados)
    - escrita - POST, PUT (substituir), PATCH (atualiza), DELETE
- O endereço do recurso a ser acessados
    (www.site.com.br/users/ = "/users" é o recurso)
- Os cabeçalhos HTTP (Content-Type, Authorization)
- O Corpo da mensagem (caso necessário, de acordo com o método HTTP)

A mensagem de resposta do servidor deve incluir dados como:
- o código de status HTTP (200 success, 404 Not Found, 301 Moved Permanently)
    https://developer.mozilla.org/en-US/docs/Web/HTTP/Status
- Os cabeçalhos HTTP (Content-Type, Accept)
- O corpo da mensagem (Pode estar vazio em alguns casos)
'''
