# SPF, DKIM and DMARC

## Objetivo

Validar mecanismos de autenticação de e-mail.

## SPF

Sender Policy Framework.

Define quais servidores podem enviar mensagens pelo domínio.

### Exemplo

```txt
v=spf1 include:_spf.google.com ~all