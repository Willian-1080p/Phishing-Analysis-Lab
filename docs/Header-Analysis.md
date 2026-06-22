# Header Analysis

## Objetivo

Analisar cabeçalhos de e-mails para identificar possíveis tentativas de phishing, spoofing ou envio malicioso.

## Campos Importantes

### From

Remetente informado ao usuário.

### Reply-To

Endereço utilizado para resposta.

### Return-Path

Origem real da mensagem.

### Received

Servidores pelos quais o e-mail passou.

### Message-ID

Identificador único da mensagem.

## Indicadores Suspeitos

- Domínio diferente do remetente legítimo
- Reply-To divergente
- IP de origem desconhecido
- SPF Fail
- DKIM Fail
- DMARC Fail

## Ferramentas

- Microsoft Defender
- Google Toolbox
- MXToolbox
- Header Analyzer

## Exemplo
