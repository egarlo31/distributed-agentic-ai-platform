# Data Sources

## SRC-001 — NetsLab-5G-ORAN-IDD

- **Source:** NetsLab-5G-ORAN-IDD
- **Provider:** NetsLab
- **Dataset:** https://www.kaggle.com/datasets/netslabdemo/netslab-5g-oran-idd/data
- **Access date:** 2026-09-27
- **License:** Creative Commons Attribution 4.0 International (CC BY 4.0)  
  https://creativecommons.org/licenses/by/4.0/
- **Failure Family:** F1 — Security / anomalous network activity

### Role in the Project

The dataset provides 5G/O-RAN network traffic and lower-layer telemetry used as
technical evidence for development and evaluation of the DAICP MVP.

### Initial Development Subset

| Category | Network Evidence | Lower-Layer Telemetry |
|---|---|---|
| Benign | `benign.pcap` | `benign.txt` |
| DDoS | `ddos_icmp_hping3.pcap` | `ddos_icmp_hping3.txt` |
| DoS | `icmp_nping.pcap` | `icmp_nping.txt` |
| BruteForce | `ftp_hydra.pcap` | `ftp_hydra.txt` |
| Probe | `portscan_masscan.pcap` | `portscan_masscan.txt` |
| Web | `web_xss.pcap` | `web_xss.txt` |

### Data Interpretation

- `.pcap`: raw network traffic evidence.
- `.txt`: lower-layer 5G/O-RAN telemetry.
- Category/scenario: dataset label used to identify the represented condition.

Only a selected subset is used during initial development. Additional scenarios
may be incorporated during evaluation if required.