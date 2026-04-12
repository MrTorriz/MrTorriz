<h1 align="center">Hi, I'm Martin Karlsson</h1>

<p align="center">
  <em>Network Security Specialist · Gothenburg, Sweden</em><br>
  Graduating May 2026 from <strong>Folkuniversitetet</strong> — <em>Specialist inom nätverkssäkerhet (SN24)</em>
</p>

<p align="center">
  <a href="https://www.linkedin.com/in/martin-karlsson-557321360/"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn"></a>
  <img src="https://img.shields.io/badge/Location-Gothenburg-4A90E2?style=for-the-badge&logo=googlemaps&logoColor=white" alt="Gothenburg">
  <img src="https://img.shields.io/badge/Open%20to-Work-brightgreen?style=for-the-badge" alt="Open to work">
</p>

---

## About

I build and secure infrastructure — from physical network gear to self-hosted services. My background mixes hands-on networking labs (GNS3, Cisco, Arista, Juniper), Linux server administration, and automation with Puppet. I care about *defense in depth*, least privilege, and things that actually work when you pull the power cable.

Looking for roles in **network security, server administration, or IT infrastructure** in the Gothenburg region after graduation.

---

## Tech Stack

**Networking & Security**
<p>
  <img src="https://img.shields.io/badge/Cisco%20IOS-1BA0D7?style=flat-square&logo=cisco&logoColor=white">
  <img src="https://img.shields.io/badge/Arista%20EOS-F04E23?style=flat-square&logoColor=white">
  <img src="https://img.shields.io/badge/Juniper-84B641?style=flat-square&logo=juniper-networks&logoColor=white">
  <img src="https://img.shields.io/badge/FortiGate-EE3124?style=flat-square&logo=fortinet&logoColor=white">
  <img src="https://img.shields.io/badge/pfSense-212121?style=flat-square&logo=pfsense&logoColor=white">
  <img src="https://img.shields.io/badge/nftables-000?style=flat-square">
  <img src="https://img.shields.io/badge/Wireshark-1679A7?style=flat-square&logo=wireshark&logoColor=white">
  <img src="https://img.shields.io/badge/Suricata-D32F2F?style=flat-square">
  <img src="https://img.shields.io/badge/WireGuard-88171A?style=flat-square&logo=wireguard&logoColor=white">
</p>

**Systems & Virtualization**
<p>
  <img src="https://img.shields.io/badge/Linux-FCC624?style=flat-square&logo=linux&logoColor=black">
  <img src="https://img.shields.io/badge/Debian-A81D33?style=flat-square&logo=debian&logoColor=white">
  <img src="https://img.shields.io/badge/Ubuntu-E95420?style=flat-square&logo=ubuntu&logoColor=white">
  <img src="https://img.shields.io/badge/Fedora-294172?style=flat-square&logo=fedora&logoColor=white">
  <img src="https://img.shields.io/badge/FreeBSD-AB2B28?style=flat-square&logo=freebsd&logoColor=white">
  <img src="https://img.shields.io/badge/KVM-EB0000?style=flat-square">
  <img src="https://img.shields.io/badge/Proxmox-E57000?style=flat-square&logo=proxmox&logoColor=white">
  <img src="https://img.shields.io/badge/CloudStack-72A4D2?style=flat-square&logo=apachecloudstack&logoColor=white">
  <img src="https://img.shields.io/badge/Ceph-EF5B25?style=flat-square&logo=ceph&logoColor=white">
</p>

**Automation & Tools**
<p>
  <img src="https://img.shields.io/badge/Puppet-FFAE1A?style=flat-square&logo=puppet&logoColor=black">
  <img src="https://img.shields.io/badge/Bash-4EAA25?style=flat-square&logo=gnubash&logoColor=white">
  <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white">
  <img src="https://img.shields.io/badge/Git-F05032?style=flat-square&logo=git&logoColor=white">
  <img src="https://img.shields.io/badge/LaTeX-008080?style=flat-square&logo=latex&logoColor=white">
  <img src="https://img.shields.io/badge/GNS3-000?style=flat-square">
</p>

---

## Featured Work

### Thesis — Zero Trust Network Access (2026)
A full ZTNA lab built on open source only, no commercial platforms. A Debian gateway enforces identity-based access as a Policy Enforcement Point.

- **Stack:** Dex (OIDC) · OAuth2-Proxy · Nginx (reverse proxy + PEP) · nftables (default deny) · GNS3
- **Flow:** `Client → Nginx:80 → OAuth2-Proxy → Dex → Nginx PEP → Backend`
- **Principles:** Always verify · Least privilege · Assume breach
- **Outcome:** Five test cases (T1–T5) passed — unauthenticated access denied, microsegmentation logged, OIDC enforced end-to-end.

### LIA-2 — Adeptum Data Center *(in progress, Mar–Apr 2026)*
Designing and automating a real-hardware platform combining **Apache CloudStack**, **Kill Bill** (usage-based billing with Stripe), and **Puppet** across Panasas ActiveStor, HP C7000 blades, and SuperMicro chassis.

- Ceph storage (MON/MGR/MDS/OSD) on Panasas directors + storage blades
- Diskless PXE-boot everywhere — new hardware: plug in, register MAC, boot
- Puppet Roles & Profiles for management, services, director, storage, compute
- Python sync job feeding CloudStack VM usage into Kill Bill for invoicing

### LIA-1 — Adeptum *(Jan–Feb 2026)*
Brought a Panasas ActiveStor cluster to life from bare metal: built the PXE + DHCP + TFTP + NFS provisioning chain, profiled the hardware, deployed Ceph, and wrote the Puppet code (Roles & Profiles) that makes the whole thing reproducible. All nodes boot diskless from NFS-root keyed on MAC address.

### LIA-1 — Movz (Web App Security)
Audited a logistics startup's REST API against OWASP Top 10:2025 — found user enumeration, exposed ports, weak file permissions. Hardened SSH, closed ports, deployed Fail2ban. Wrote the incident and remediation reports.

---

## Homelab

A real, running production-ish environment I maintain and break things on:

- **Server:** Ubuntu 24.04 LTS · i5-9400F · 16 GB RAM · RTX 2060 (Plex transcoding + Immich ML) · 8 TB across two drives
- **~38 Docker containers:** Plex · Immich · Nextcloud · Audiobookshelf · Sonarr/Radarr/Lidarr/Bazarr/Prowlarr · qBittorrent (VPN-bound) · Nginx Proxy Manager · AdGuard Home · UniFi · Homepage · Portainer · Netdata · Scrutiny · CrowdSec · Suricata
- **Security:** UFW default-deny · Mullvad WireGuard lockdown · CrowdSec + Suricata IDS · `no-new-privileges` on every container · SSH key-only · Cloudflare Tunnel + Access (Google OAuth) for the few things exposed
- **Automation:** Puppet for system config · nightly auto-sync to GitHub · scheduled backups and VPN-server rotation

Everything is tracked in a private repo with Docker Compose, scripts, and snapshots — treated like a real deployment, not a toy.

---

## Education Highlights

Two years of intensive network security training covering:

**Networking:** OSI/TCP-IP · OSPFv2/v3 · BGP · VLAN/STP · IPv6 (SLAAC, DHCPv6, NAT64) · QUIC/HTTP-3 · NetFlow/sFlow/IPFIX · LibreNMS
**Security:** TLS 1.3 · IPSec · WireGuard · PKI · SPF/DKIM/DMARC · MITRE ATT&CK · CVSS · Metasploit · John the Ripper · AIDE · AppArmor/SELinux
**Firewalls:** iptables · nftables · PF · FortiGate · Shorewall · UFW · WFAS
**Servers:** LVM · mdadm RAID · LUKS · ZFS · systemd · AD · GPO
**Virtualization & IaC:** Proxmox · KVM · Docker · Ceph · CloudStack · Puppet · ZTP

Full course breakdown: see the [course summary](https://github.com/MrTorriz) (private).

---

## GitHub Stats

<p align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=MrTorriz&show_icons=true&theme=tokyonight&hide_border=true&count_private=true" alt="GitHub stats">
</p>
<p align="center">
  <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=MrTorriz&layout=compact&theme=tokyonight&hide_border=true" alt="Top languages">
</p>

---

<p align="center">
  <em>Open to opportunities in Gothenburg from May 2026 onward.</em><br>
  <a href="https://www.linkedin.com/in/martin-karlsson-557321360/">Let's talk on LinkedIn →</a>
</p>
