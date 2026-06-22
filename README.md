# Phishing Analysis Lab

Laboratório prático para análise de campanhas de phishing, investigação de e-mails suspeitos, extração de IOC (Indicators of Compromise) e validação de mecanismos de autenticação de e-mail.

## Objetivo

Este projeto foi criado para demonstrar técnicas utilizadas por analistas de segurança durante investigações de phishing, incluindo:

* Análise de cabeçalhos de e-mail
* Validação SPF, DKIM e DMARC
* Extração de IOC
* Análise de URLs
* Interpretação de relatórios de Sandbox
* Estudos de casos reais simulados

## Estrutura do Projeto

```text
Phishing-Analysis-Lab/
├─ tools/
├─ samples/
├─ templates/
├─ docs/
└─ cases/
```

## Ferramentas Disponíveis

### Header Analyzer

Analisa cabeçalhos de e-mails para identificar spoofing, remetentes falsificados e inconsistências.

```bash
python tools/header_analyzer.py sample.eml
```

### SPF / DKIM / DMARC Checker

Valida registros DNS relacionados à autenticação de e-mails.

```bash
python tools/spf_dkim_dmarc_checker.py
```

### IOC Extractor

Extrai:

* Endereços IP
* Domínios
* URLs
* Hashes

```bash
python tools/ioc_extractor.py sample.txt
```

### URL Analyzer

Analisa URLs suspeitas em busca de indicadores comuns de phishing.

```bash
python tools/url_analyzer.py
```

### Sandbox Report Parser

Interpreta relatórios exportados de ferramentas de Sandbox.

```bash
python tools/sandbox_report_parser.py report.json
```

## Fluxo de Investigação

1. Receber e-mail suspeito
2. Coletar cabeçalhos
3. Validar SPF, DKIM e DMARC
4. Extrair IOC
5. Analisar URLs
6. Verificar reputação dos indicadores
7. Avaliar anexos em Sandbox
8. Produzir relatório final

## Indicadores de Comprometimento (IOC)

O laboratório trabalha com:

* IPv4
* Domínios
* URLs
* MD5
* SHA1
* SHA256

## Ferramentas Recomendadas

* Microsoft Defender
* VirusTotal
* URLScan
* AbuseIPDB
* Hybrid Analysis
* Any.Run
* Joe Sandbox
* Google Toolbox
* MXToolbox

## Casos Simulados

### Case 001

Fake Microsoft 365 Login Page

### Case 002

Malicious Invoice Delivery

### Case 003

Credential Harvesting via HTML Attachment

## Requisitos

```bash
pip install -r requirements.txt
```

## Uso Educacional

Este projeto possui finalidade exclusivamente educacional e de treinamento em Segurança da Informação.

## Autor

Wellington Santos

## Licença

MIT License
