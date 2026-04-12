![header](https://capsule-render.vercel.app/api?type=shark&height=200&color=0:0d1117,100:0a1628&text=Martin%20Karlsson&fontSize=52&fontColor=c0caf5&desc=Network%20Security%20Specialist%20%C2%B7%20Gothenburg%2C%20Sweden&descSize=20&descAlignY=75&animation=fadeIn)

<div align="center">

[![Typing SVG](https://readme-typing-svg.demolab.com?font=Fira+Code&size=15&duration=3000&pause=900&color=7AA2F7&center=true&vCenter=true&width=560&height=32&lines=Network+Security+%7C+Linux+Infrastructure;Zero+Trust+%7C+Defense+in+Depth;Networking+%7C+Automation+%7C+Homelab;Open+to+Work+%E2%80%94+May+2026)](https://git.io/typing-svg)

<br>

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=flat-square&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/martin-karlsson-557321360/)
[![Open to Work](https://img.shields.io/badge/Open%20to%20Work-May%202026-2ea44f?style=flat-square)](https://www.linkedin.com/in/martin-karlsson-557321360/)
[![Profile Views](https://komarev.com/ghpvc/?username=MrTorriz&color=0a1628&style=flat-square&label=profile+views)](https://github.com/MrTorriz)

</div>

---

I build and secure infrastructure — from physical data center hardware to self-hosted home services. My background covers hands-on networking labs (GNS3, Cisco, Arista, Juniper), Linux server administration, bare-metal provisioning, and automation with Puppet. I care about defense in depth, least privilege, and things that actually work when you pull the power cable.

Looking for roles in **network security, server administration, or IT infrastructure** in the Gothenburg region.

---

## Currently

- Finishing my **ZTNA thesis** — open-source Zero Trust lab (Dex + OAuth2-Proxy + nftables + Nginx)
- Building a fully automated **data center platform** at Adeptum: CloudStack + Ceph + Kill Bill + Puppet, on real Panasas and HP C7000 hardware
- Maintaining a ~38-container homelab that I treat like a real deployment

---

## Tech Stack

**Networking & Security**

[![Networking skills](https://skillicons.dev/icons?i=linux,debian,ubuntu,kali,bash,python,docker,git,nginx,grafana,cloudflare&theme=dark)](https://skillicons.dev)

| Protocols & Routing | Firewalls | Security |
|---|---|---|
| OSPF · BGP · EIGRP · RIP | nftables · iptables · PF · UFW | TLS 1.3 · IPSec · WireGuard |
| IPv6 · VLAN · STP · HSRP | FortiGate · Sophos XG · pfSense | OIDC · PKI · SPF/DKIM/DMARC |
| QUIC · HTTP/3 · MPTCP | Shorewall · WFAS | Suricata · CrowdSec · Fail2ban |
| NetFlow · sFlow · IPFIX | Cisco IOS · Arista EOS · Juniper | MITRE ATT&CK · CVSS · Metasploit |

**Systems & Infrastructure**

| Virtualization | Storage | Automation |
|---|---|---|
| KVM / libvirt | Ceph (MON/MGR/MDS/OSD) | Puppet (Roles & Profiles) |
| Proxmox · CloudStack | LVM · mdadm RAID · LUKS · ZFS | Bash · Python · Cron |
| Docker · GNS3 | PXE + DHCP + TFTP + NFS | Git / GitHub |

---

## Featured Work

### Thesis — Zero Trust Network Access *(2026)*

Open-source ZTNA lab in GNS3. A Debian gateway acts as the Policy Enforcement Point — no traffic reaches internal resources without verified identity and explicit policy.

```
Client → Nginx:80 → OAuth2-Proxy:4180 → Dex:5556 (OIDC) → Nginx:8888 (PEP) → Backend
```

Three isolated zones · nftables default-deny · Dex + OAuth2-Proxy as systemd services  
**T1–T5 all passed** — unauthenticated blocked, OIDC enforced, microsegmentation logged.

---

### Internship — Adeptum Data Center *(Mar–Apr 2026)*

Designing and building a fully automated data center platform on physical hardware:

- **Storage:** Ceph cluster on Panasas ActiveStor (directors = MON/MGR/MDS, storage blades = OSD)
- **Compute:** Diskless HP C7000 and SuperMicro blades — PXE-boot → Puppet-run → CloudStack agent, done
- **Orchestration:** Apache CloudStack with Ceph RBD as primary storage
- **Billing:** Kill Bill + Stripe, fed by a Python sync job reading CloudStack VM usage every 15 min
- **IaC:** Puppet Roles & Profiles (`role::management`, `director`, `storage`, `compute`, `services`)

New hardware: plug in, register MAC, power on. Puppet handles the rest.

---

### Internship — Adeptum *(Jan–Feb 2026)*

Brought a Panasas ActiveStor cluster to life from bare metal. Built the full PXE provisioning chain (DHCP + TFTP + NFS-root per MAC), profiled director and storage hardware, deployed Ceph, and wrote the Puppet code that makes all of it reproducible.

---

### Internship — Movz *(Jan–Feb 2026)*

Security audit of a logistics startup's REST API (OWASP Top 10:2025) — found user enumeration, exposed ports, weak file permissions. Hardened SSH, closed ports, deployed Fail2ban. Delivered incident and remediation reports.

---

## Homelab

Ubuntu 24.04 LTS · i5-9400F · 16 GB RAM · RTX 2060 · ~8 TB storage

<details>
<summary>~38 running Docker containers</summary>

| Category | Services |
|---|---|
| Media | Plex (GPU transcode) · Audiobookshelf · Tdarr |
| Photos | Immich (GPU ML face detection) |
| Cloud | Nextcloud |
| *arr stack | Sonarr · Radarr · Lidarr · Bazarr · Prowlarr · qBittorrent (VPN-bound) · Seerr · FlareSolverr |
| Network | AdGuard Home · Nginx Proxy Manager · UniFi · Cloudflared |
| Monitoring | Netdata · Glances · Scrutiny · Dozzle · Speedtest |
| Security | CrowdSec · Suricata |
| Productivity | Miniflux · Ntfy · IT-Tools · Draw.io |
| Management | Portainer · Watchtower · Homepage |

</details>

**Security posture:** UFW default-deny · Mullvad WireGuard lockdown · CrowdSec + Suricata IDS · `no-new-privileges` on every container · SSH key-only · Cloudflare Tunnel + Access (Google OAuth) for external exposure

---

## Education

<details>
<summary>Specialist inom nätverkssäkerhet — Folkuniversitetet Göteborg (Aug 2024 – May 2026)</summary>

| Course | Topics |
|---|---|
| Network Theory | OSI/TCP-IP · Subnetting · DNS · DHCP · ARP · VLANs |
| Virtualization | KVM · Proxmox · Docker · Ceph · GlusterFS · OpenStack |
| Routing & Switching | OSPF · BGP · EIGRP · ACL · NAT · PXE · VLAN/STP |
| Server Administration | LVM · RAID · LUKS · ZFS · systemd · AD · GPO · Fail2ban |
| Firewalls | nftables · iptables · PF · UFW · FortiGate · Sophos XG · Suricata |
| Network Security | TLS · IPSec · WireGuard · PKI · SPF/DKIM/DMARC · Metasploit · MITRE ATT&CK |
| Technical English | Incident reports · CVSS · CVE · CWE · GDPR |
| Advanced Networking | OSPFv3 · BGP path selection · IPv6 · QUIC · QoS · LibreNMS · NetFlow |
| Advanced R&S | Puppet · ZTP · BFD · NAT64 · Arista/Juniper/FRRouting interop |
| Thesis | ZTNA implementation and evaluation |

</details>

---

## Stats

<div align="center">

<table>
<tr>
<td>

[![GitHub Stats](https://github-readme-stats.vercel.app/api?username=MrTorriz&show_icons=true&theme=tokyonight&hide_border=true&count_private=true&rank_icon=github)](https://github.com/MrTorriz)

</td>
<td>

[![Top Languages](https://github-readme-stats.vercel.app/api/top-langs/?username=MrTorriz&layout=compact&theme=tokyonight&hide_border=true)](https://github.com/MrTorriz)

</td>
</tr>
</table>

[![GitHub Streak](https://streak-stats.demolab.com/?user=MrTorriz&theme=tokyonight&hide_border=true)](https://git.io/streak-stats)

</div>

---

<div align="center">
<em>Available for roles in network security, infrastructure, or server administration — Gothenburg, from May 2026.</em>
</div>

![footer](https://capsule-render.vercel.app/api?type=wave&height=100&color=0:0a1628,100:0d1117&section=footer&reversal=true)

