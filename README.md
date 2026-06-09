# Cloud-Native SIEM & Automated Incident Response (SOAR) Pipeline

An enterprise-grade, cloud-native security orchestration pipeline that converts high-velocity server authentication telemetry into actionable threat intelligence, executing automated infrastructure containment to neutralize active brute-force vectors in sub-seconds.

## 🚀 Architectural Overview

1. **Ingestion Layer:** Linux Host authentication system records standard `/var/log/auth.log` telemetry.
2. **Transport Layer:** Fluent-Bit monitors and parses raw syslog frames utilizing customized regular expressions.
3. **Analytics Engine:** Data is securely streamed to an OpenSearch (Elasticsearch ecosystem) node indexing security metadata.
4. **SOAR Logic Loop:** A modular automation script continuously assesses rolling failure counts against defined thresholds, executing system-level isolation (`iptables`/Network ACL) policies upon rule validation.

## 🛠️ Technology Stack

- **Languages:** Python 3.x, Bash
- **SIEM Core:** OpenSearch / Elasticsearch Engine
- **Data Logistics:** Fluent-Bit Log Shipper
- **Containerization:** Docker / Docker-Compose
- **Environment:** Linux Ubuntu Architecture

## 📦 Directory Blueprint

```text
├── config/
│   └── fluent-bit.conf      # Log engine transport pipeline rules
├── src/
│   ├── attack_simulator.py  # Malicious telemetry generation framework
│   └── auto_blocker.py      # Core automation containment engine
└── docker-compose.yml       # Standardized infrastructure orchestrator
