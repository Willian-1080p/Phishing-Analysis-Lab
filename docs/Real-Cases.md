# Real Cases

## Caso 001 - Falso Login Microsoft 365

### Cenário

Usuário recebeu e-mail informando expiração de senha.

### Indicadores

- Domínio falso
- Página clonada
- Captura de credenciais

### Resultado

Bloqueio do domínio e redefinição de senha.

---

## Caso 002 - Fatura Maliciosa

### Cenário

Recebimento de PDF com link para download de malware.

### Indicadores

- URL encurtada
- Domínio recém-criado
- Download de executável

### Resultado

IOC adicionados ao SIEM.

---

## Caso 003 - Anexo HTML Phishing

### Cenário

Anexo HTML simulando portal corporativo.

### Indicadores

- Formulário falso
- Exfiltração de credenciais
- Servidor externo

### Resultado

Campanha removida e usuários notificados.

---

## Lições Aprendidas

- Utilizar MFA
- Validar remetentes
- Monitorar novos domínios
- Treinar usuários regularmente